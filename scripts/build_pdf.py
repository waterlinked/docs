#!/usr/bin/env python3
"""Build one PDF manual per top-level product section of the documentation.

The PDFs are generated from the *built* MkDocs site, so they contain exactly the same
content as the website. Page order and grouping follow the `nav` in mkdocs.yml: adding,
removing or renaming a page in the nav is automatically reflected in the next PDF build.

Usage:
    uv run python scripts/build_pdf.py                  # builds the site first, writes to docs/pdf/
    uv run python scripts/build_pdf.py --site-dir site  # reuse an already built site
    uv run python scripts/build_pdf.py --only "Underwater GPS"

Each PDF is verified after it is written; the script exits non-zero if a page from the nav
is missing from a PDF, an internal link cannot be resolved, or an image is missing.

The download button on the website (overrides/partials/pdf-download.html) links to
pdf/waterlinked-<slug>.pdf, where <slug> is made from the section title by pdf_slug() below.
Keep the two in sync.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import logging
import os
import posixpath
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from bs4 import BeautifulSoup, Tag
from PIL import Image
from pypdf import PdfReader, PdfWriter

logging.getLogger("pypdf").setLevel(logging.ERROR)  # Chrome's PDFs trigger harmless trailer warnings

ROOT = Path(__file__).resolve().parent.parent
PDF_CSS = ROOT / "scripts" / "pdf" / "pdf.css"
MARKER = "WLPDFCH"  # invisible text used to find the page number of each chapter
MAX_IMAGE_PX = 1600  # ~230 dpi across the text width of an A4 page


def pdf_slug(title: str) -> str:
    """Same rule as the Jinja expression in overrides/partials/pdf-download.html."""
    return title.lower().replace("/", "").replace(" ", "-")


def pdf_filename(title: str) -> str:
    return f"waterlinked-{pdf_slug(title)}.pdf"


# --------------------------------------------------------------------------------------
# Navigation
# --------------------------------------------------------------------------------------

@dataclass
class Entry:
    """A page or a group in the navigation of one section."""
    title: str
    level: int                      # 0 = directly below the section
    path: tuple[str, ...]           # titles of the parent groups (breadcrumb)
    md: str | None = None           # markdown file for pages, None for groups
    index: int = -1                 # chapter number for pages

    @property
    def is_page(self) -> bool:
        return self.md is not None


@dataclass
class Section:
    title: str
    entries: list[Entry] = field(default_factory=list)

    @property
    def pages(self) -> list[Entry]:
        return [e for e in self.entries if e.is_page]


class _SafeLoader(yaml.SafeLoader):
    """mkdocs.yml may contain !!python/name tags (e.g. for emoji); ignore them."""


_SafeLoader.add_multi_constructor("tag:yaml.org,2002:python/", lambda loader, suffix, node: None)
_SafeLoader.add_multi_constructor("!", lambda loader, suffix, node: None)


def load_config() -> dict:
    with open(ROOT / "mkdocs.yml", encoding="utf-8") as fh:
        return yaml.load(fh, Loader=_SafeLoader)


def load_sections(config: dict) -> list[Section]:
    sections = []
    for item in config["nav"]:
        if not isinstance(item, dict):
            continue  # a top-level page without a section (e.g. "- index.md") has no manual
        (title, value), = item.items()
        if isinstance(value, list):
            section = Section(title)
            _walk(value, section, level=0, path=())
            if section.pages:
                sections.append(section)
    return sections


def _walk(items: list, section: Section, level: int, path: tuple[str, ...]) -> None:
    for item in items:
        if isinstance(item, str):  # nav entry without explicit title
            title, value = Path(item).stem, item
        else:
            (title, value), = item.items()
        if isinstance(value, list):
            section.entries.append(Entry(title, level, path))
            _walk(value, section, level + 1, path + (title,))
        elif isinstance(value, str) and not re.match(r"^[a-z]+://", value):
            section.entries.append(Entry(title, level, path, md=value))
    for i, page in enumerate(section.pages):
        page.index = i


def page_url(md: str) -> str:
    """Site-relative URL of a markdown page (use_directory_urls), e.g. 'dvl/axes/'."""
    md = md.replace(os.sep, "/")
    stem = md[:-3] if md.endswith(".md") else md
    if stem == "index" or stem.endswith("/index"):
        return stem[: -len("index")]
    return stem + "/"


# --------------------------------------------------------------------------------------
# HTML assembly
# --------------------------------------------------------------------------------------

@dataclass
class Problems:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


class ImageCache:
    """Downscaled copies of large images, so the PDFs stay small. The website is unchanged."""

    def __init__(self, work: Path):
        self.dir = work / "images"
        self.dir.mkdir(parents=True, exist_ok=True)
        self.cache: dict[Path, Path] = {}

    def get(self, file: Path) -> Path:
        if file in self.cache:
            return self.cache[file]
        out = file
        if file.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp"}:
            try:
                with Image.open(file) as im:
                    im.seek(0)  # first frame of animated images
                    big = max(im.size) > MAX_IMAGE_PX
                    if big or file.stat().st_size > 400_000 or file.suffix.lower() in {".webp", ".gif"}:
                        im = im.copy()
                        if big:
                            im.thumbnail((MAX_IMAGE_PX, MAX_IMAGE_PX), Image.LANCZOS)
                        transparent = im.mode in ("RGBA", "LA", "P") and im.convert("RGBA").getextrema()[3][0] < 255
                        name = f"{len(self.cache)}-{file.stem}"
                        if transparent:
                            out = self.dir / f"{name}.png"
                            im.convert("RGBA").save(out, optimize=True)
                        else:
                            out = self.dir / f"{name}.jpg"
                            im.convert("RGB").save(out, quality=85, optimize=True, progressive=True)
            except Exception:
                out = file  # unknown format: let the browser deal with it
        self.cache[file] = out
        return out


class ManualBuilder:
    def __init__(self, section: Section, site_dir: Path, site_url: str, cover_images: dict[str, str],
                 images: ImageCache):
        self.images = images
        self.section = section
        self.site_dir = site_dir
        self.site_url = site_url.rstrip("/") + "/"
        self.cover_images = cover_images
        self.problems = Problems()
        # site-relative page URL -> chapter index, for rewriting links between pages
        self.url_to_chapter = {page_url(p.md): p.index for p in section.pages}

    # -- links / resources ------------------------------------------------------------

    def _resolve(self, base_url: str, href: str) -> tuple[str, str]:
        """Resolve a relative href on page `base_url` to (site path, fragment)."""
        parts = urlsplit(href)
        target = posixpath.normpath(posixpath.join(base_url, unquote(parts.path))) if parts.path else base_url
        while target.startswith("../"):  # browsers never go above the site root
            target = target[3:]
        if target in (".", ".."):
            target = ""
        return target, parts.fragment

    def _page_key(self, site_path: str) -> str | None:
        """Map a resolved site path to a page URL key if it is an HTML page."""
        p = site_path
        if p.endswith("index.html"):
            p = p[: -len("index.html")]
        if p and not p.endswith("/") and "." not in posixpath.basename(p):
            p += "/"
        if p == "/":
            p = ""
        return p if (p == "" or p.endswith("/")) else None

    def _rewrite_links(self, root: Tag, chapter: Entry, base_url: str) -> None:
        prefix = f"c{chapter.index}--"
        for tag in root.find_all(id=True):
            tag["id"] = prefix + tag["id"]
        for a in root.find_all("a", href=True):
            href = a["href"].strip()
            if not href or re.match(r"^(mailto:|tel:|javascript:)", href):
                continue
            if re.match(r"^[a-z][a-z0-9+.-]*://", href, re.I):
                continue  # external link, keep as is
            if href.startswith("#"):
                a["href"] = "#" + prefix + href[1:] if len(href) > 1 else "#" + f"chapter-{chapter.index}"
                continue
            target, frag = self._resolve(base_url, href)
            key = self._page_key(target)
            if key is not None and key in self.url_to_chapter:
                j = self.url_to_chapter[key]
                a["href"] = f"#c{j}--{frag}" if frag else f"#chapter-{j}"
            else:
                # Page from another product, or a downloadable file: link to the website.
                exists = (self.site_dir / key / "index.html").exists() if key is not None else (self.site_dir / target).exists()
                if not exists:
                    self.problems.errors.append(f"{chapter.md}: broken link '{href}'")
                a["href"] = self.site_url + (key if key is not None else target) + (f"#{frag}" if frag else "")

    def _fix_resources(self, root: Tag, chapter: Entry, base_url: str) -> None:
        for img in root.find_all("img", src=True):
            src = img["src"]
            img.attrs.pop("srcset", None)
            img.attrs.pop("loading", None)
            if re.match(r"^(https?:|data:)", src):
                continue
            target, _ = self._resolve(base_url, src)
            file = self.site_dir / target
            if not file.exists():
                self.problems.errors.append(f"{chapter.md}: missing image '{src}'")
                continue
            img["src"] = self.images.get(file.resolve()).as_uri()
        for iframe in root.find_all("iframe"):
            src = iframe.get("src", "")
            m = re.search(r"youtube(?:-nocookie)?\.com/embed/([\w-]+)", src)
            url = f"https://www.youtube.com/watch?v={m.group(1)}" if m else src
            title = iframe.get("title") or "Video"
            box = BeautifulSoup(
                f'<div class="pdf-video"><strong>{html.escape(title)}</strong> '
                f'(video, watch online): <a href="{html.escape(url)}">{html.escape(url)}</a></div>',
                "html.parser",
            )
            container = iframe.find_parent("div", class_="responsive-video") or iframe
            container.replace_with(box)

    # -- content transforms -------------------------------------------------------------

    @staticmethod
    def _flatten_tabs(root: Tag, soup: BeautifulSoup) -> None:
        """Content tabs cannot be clicked on paper: show every tab, each under its label."""
        for tabset in root.select("div.tabbed-set"):
            labels = [lbl.get_text(" ", strip=True) for lbl in tabset.select(".tabbed-labels label")]
            blocks = tabset.select(".tabbed-content > .tabbed-block")
            wrapper = soup.new_tag("div", attrs={"class": "pdf-tabs"})
            for i, block in enumerate(blocks):
                tab = soup.new_tag("div", attrs={"class": "pdf-tab"})
                head = soup.new_tag("div", attrs={"class": "pdf-tab__title"})
                head.string = labels[i] if i < len(labels) else f"Tab {i + 1}"
                tab.append(head)
                for child in list(block.contents):
                    tab.append(child.extract())
                wrapper.append(tab)
            tabset.replace_with(wrapper)

    def chapter_html(self, chapter: Entry) -> str:
        base_url = page_url(chapter.md)
        file = self.site_dir / base_url / "index.html"
        if not file.exists():
            self.problems.errors.append(f"{chapter.md}: built page not found at {file}")
            return ""
        soup = BeautifulSoup(file.read_text(encoding="utf-8"), "html.parser")
        article = soup.select_one("article.md-content__inner")
        if article is None:
            self.problems.errors.append(f"{chapter.md}: no <article> content found")
            return ""
        for sel in ["a.headerlink", ".md-content__button", ".md-source-file", "script", "form.md-feedback",
                    ".pdf-download"]:
            for tag in article.select(sel):
                tag.decompose()
        for details in article.find_all("details"):
            details["open"] = ""
        self._flatten_tabs(article, soup)
        self._fix_resources(article, chapter, base_url)
        self._rewrite_links(article, chapter, base_url)

        crumbs = " › ".join(html.escape(t) for t in (self.section.title,) + chapter.path)
        online = self.site_url + base_url
        header = (
            f'<div class="pdf-chapter__meta"><span class="pdf-crumbs">{crumbs}</span>'
            f'<span class="pdf-marker">{MARKER}{chapter.index}X</span>'
            f'<a class="pdf-online" href="{online}">{html.escape(online)}</a></div>'
        )
        body = "".join(str(c) for c in article.contents)
        return f'<section class="pdf-chapter" id="chapter-{chapter.index}">{header}{body}</section>'

    # -- document -------------------------------------------------------------------------

    def toc_html(self, page_numbers: dict[int, int]) -> str:
        rows = []
        for e in self.section.entries:
            cls = f"pdf-toc__row pdf-toc__row--l{min(e.level, 3)}"
            if e.is_page:
                num = page_numbers.get(e.index, "")
                rows.append(
                    f'<a class="{cls}" href="#chapter-{e.index}"><span class="pdf-toc__title">'
                    f'{html.escape(e.title)}</span><span class="pdf-toc__dots"></span>'
                    f'<span class="pdf-toc__num">{num}</span></a>'
                )
            else:
                rows.append(f'<div class="{cls} pdf-toc__group">{html.escape(e.title)}</div>')
        return '<section class="pdf-toc"><h1 class="pdf-toc__heading">Contents</h1>' + "".join(rows) + "</section>"

    def cover_html(self, version: str, date: str) -> str:
        first = page_url(self.section.pages[0].md)
        image = self.cover_images.get(first.split("/")[0], "")
        img_html = f'<img class="pdf-cover__product" src="{image}" alt="">' if image else ""
        logo = (self.site_dir / "img" / "waterlinked_logo.png").resolve().as_uri()
        online = self.site_url + first
        return f"""
<section class="pdf-cover">
  <div class="pdf-cover__band">
    <img class="pdf-cover__logo" src="{logo}" alt="Water Linked">
    <div class="pdf-cover__kicker">Product documentation</div>
    <h1 class="pdf-cover__title">{html.escape(self.section.title)}</h1>
    <div class="pdf-cover__accent"></div>
  </div>
  <div class="pdf-cover__body">
    {img_html}
    <div class="pdf-cover__info">
      <p>This PDF is generated automatically from the online documentation and contains the same
      information. The online version is always the most up to date:</p>
      <p><a href="{online}">{html.escape(online)}</a></p>
      <p class="pdf-cover__version">Content last changed {date} &middot; {html.escape(version)}</p>
    </div>
  </div>
</section>"""

    def document(self, stylesheets: list[str], page_numbers: dict[int, int], version: str, date: str) -> str:
        chapters = "".join(self.chapter_html(p) for p in self.section.pages)
        links = "".join(f'<link rel="stylesheet" href="{s}">' for s in stylesheets)
        title = f"Water Linked {self.section.title} documentation"
        return f"""<!doctype html>
<html lang="en" dir="ltr"><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<meta name="author" content="Water Linked AS">
{links}<link rel="stylesheet" href="{PDF_CSS.resolve().as_uri()}">
<style>@page {{ @top-right {{ content: "{title.replace('"', "'")}"; }} }}</style>
</head>
<body dir="ltr" data-md-color-scheme="default" data-md-color-primary="custom" data-md-color-accent="custom">
{self.cover_html(version, date)}
{self.toc_html(page_numbers)}
<main class="md-typeset pdf-content">{chapters}</main>
</body></html>"""


# --------------------------------------------------------------------------------------
# Rendering and verification
# --------------------------------------------------------------------------------------

def site_stylesheets(site_dir: Path) -> list[str]:
    """The stylesheets the website itself uses (theme, palette, fonts, extra.css)."""
    index = (site_dir / "index.html").read_text(encoding="utf-8")
    sheets = []
    for href in re.findall(r'<link rel="stylesheet" href="([^"]+)"', index):
        if re.match(r"^https?://", href):
            sheets.append(href)
        else:
            sheets.append((site_dir / href).resolve().as_uri())
    return sheets


def cover_images(site_dir: Path) -> dict[str, str]:
    """Product images from the home page cards, keyed by the top-level folder they link to."""
    soup = BeautifulSoup((site_dir / "index.html").read_text(encoding="utf-8"), "html.parser")
    images = {}
    for a in soup.select("article a[href]"):
        img = a.find("img")
        folder = a["href"].strip("./").split("/")[0]
        if img and folder and folder not in images:
            images[folder] = (site_dir / img["src"]).resolve().as_uri()
    return images


def launch_browser(p):
    try:
        return p.chromium.launch()
    except Exception as exc:  # Playwright's own Chromium not installed: try a system Chrome
        for exe in [os.environ.get("PDF_CHROME"), "/usr/bin/google-chrome", "/usr/bin/chromium",
                    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]:
            if exe and Path(exe).exists():
                return p.chromium.launch(executable_path=exe)
        raise SystemExit(
            "No Chromium found. Run `uv run playwright install chromium` or set PDF_CHROME.\n" + str(exc)
        )


def render(browser, html_doc: str, out: Path, work: Path) -> None:
    src = work / (out.stem + ".html")
    src.write_text(html_doc, encoding="utf-8")
    page = browser.new_page()
    page.goto(src.as_uri(), wait_until="networkidle")
    page.emulate_media(media="print")
    page.pdf(path=str(out), prefer_css_page_size=True, print_background=True, outline=True, tagged=True)
    page.close()


def chapter_pages(pdf: Path) -> dict[int, int]:
    """Find the (1-based) PDF page on which each chapter starts, using the hidden markers."""
    found = {}
    for n, page in enumerate(PdfReader(pdf).pages, start=1):
        text = re.sub(r"\s", "", page.extract_text() or "")
        for m in re.finditer(MARKER + r"(\d+)X", text):
            found.setdefault(int(m.group(1)), n)
    return found


def content_version(section: Section, docs_dir: Path) -> tuple[str, str, str]:
    """(date, commit) of the last change to the pages of this section.

    Used on the cover and as the PDF timestamps instead of "now", so a PDF is byte-for-byte
    identical until its own content changes. That keeps the published site's git history small.
    """
    files = [str(docs_dir / p.md) for p in section.pages]
    try:
        out = subprocess.check_output(["git", "log", "-1", "--format=%cs %h %cI", "--", *files],
                                      cwd=ROOT, text=True).strip()
        if subprocess.check_output(["git", "status", "--porcelain", "--", *files], cwd=ROOT, text=True).strip():
            out = ""  # uncommitted changes: the last commit does not describe the content
    except Exception:
        out = ""
    if not out:
        now = dt.datetime.now(dt.timezone.utc)
        return now.date().isoformat(), "local changes", now.isoformat(timespec="seconds")
    date, commit, iso = out.split(" ")
    return date, commit, iso


def finalize(pdf: Path, title: str, iso_time: str) -> None:
    """Fixed metadata and timestamps, so identical content gives an identical file."""
    stamp = dt.datetime.fromisoformat(iso_time).astimezone(dt.timezone.utc).strftime("D:%Y%m%d%H%M%S+00'00'")
    writer = PdfWriter(clone_from=PdfReader(pdf))
    writer.add_metadata({
        "/Title": title,
        "/Author": "Water Linked AS",
        "/Creator": "docs.waterlinked.com (scripts/build_pdf.py)",
        "/Producer": "Chromium",
        "/CreationDate": stamp,
        "/ModDate": stamp,
    })
    with open(pdf, "wb") as fh:
        writer.write(fh)


def build_site(target: Path) -> None:
    subprocess.run([sys.executable, "-m", "mkdocs", "build", "--quiet", "-d", str(target)], cwd=ROOT, check=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site-dir", type=Path, help="already built site (default: build one in a temp dir)")
    ap.add_argument("--out-dir", type=Path, default=ROOT / "docs" / "pdf", help="where to write the PDFs")
    ap.add_argument("--only", action="append", help="only build this section (nav title); repeatable")
    args = ap.parse_args()

    from playwright.sync_api import sync_playwright

    config = load_config()
    sections = load_sections(config)
    if args.only:
        unknown = set(args.only) - {s.title for s in sections}
        if unknown:
            print(f"Unknown section(s): {', '.join(sorted(unknown))}", file=sys.stderr)
            return 2
        sections = [s for s in sections if s.title in args.only]

    with tempfile.TemporaryDirectory(prefix="wl-pdf-") as tmp:
        work = Path(tmp)
        site_dir = args.site_dir.resolve() if args.site_dir else work / "site"
        if not args.site_dir:
            print("Building site ...")
            build_site(site_dir)
        args.out_dir.mkdir(parents=True, exist_ok=True)
        if not args.only:  # remove manuals of products that no longer exist
            for old_pdf in args.out_dir.glob("waterlinked-*.pdf"):
                old_pdf.unlink()
        sheets = site_stylesheets(site_dir)
        covers = cover_images(site_dir)
        images = ImageCache(work)
        failed = False

        with sync_playwright() as p:
            browser = launch_browser(p)
            for section in sections:
                out = args.out_dir / pdf_filename(section.title)
                builder = ManualBuilder(section, site_dir, config.get("site_url", ""), covers, images)
                date, version, iso_time = content_version(section, ROOT / config.get("docs_dir", "docs"))
                # Pass 1 finds on which page each chapter starts, pass 2 prints those numbers in
                # the table of contents (the numbers take the same space, so layout is unchanged).
                placeholder = {p.index: "000" for p in section.pages}
                render(browser, builder.document(sheets, placeholder, version, date), out, work)
                numbers = chapter_pages(out)
                builder.problems = Problems()
                render(browser, builder.document(sheets, numbers, version, date), out, work)

                # Verification: every page in the nav must be present in the final PDF.
                final = chapter_pages(out)
                missing = [p.md for p in section.pages if p.index not in final]
                if missing:
                    builder.problems.errors += [f"page missing from PDF: {m}" for m in missing]
                if final != numbers:
                    builder.problems.errors.append("table of contents page numbers do not match the PDF")
                finalize(out, f"Water Linked {section.title} documentation", iso_time)
                n_pages = len(PdfReader(out).pages)
                size_mb = out.stat().st_size / 1e6
                status = "OK" if not builder.problems.errors else "FAILED"
                print(f"[{status}] {out.name}: {len(section.pages)} doc pages -> {n_pages} PDF pages, {size_mb:.1f} MB")
                for w in builder.problems.warnings:
                    print(f"  warning: {w}")
                for e in builder.problems.errors:
                    print(f"  error: {e}")
                failed |= bool(builder.problems.errors)
            browser.close()

        # Verification: every "Download PDF" link on the website must point to a generated PDF.
        if not args.only:
            generated = {p.name for p in args.out_dir.glob("*.pdf")}
            linked = set()
            for page in site_dir.rglob("*.html"):
                linked |= set(re.findall(r'pdf/(waterlinked-[\w.-]+\.pdf)"', page.read_text(encoding="utf-8")))
            dangling = sorted(linked - generated)
            if dangling:
                failed = True
                print("error: website links to PDFs that were not generated: " + ", ".join(dangling))
            else:
                print(f"All {len(linked)} PDF links on the website point to generated PDFs.")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
