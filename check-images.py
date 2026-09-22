#!/usr/bin/env python3
"""Check that every image referenced by the built site actually exists.

`mkdocs build --strict` only validates Markdown image links (`![alt](../img/x.png)`).
Images written as raw HTML (`<img src="../img/x.png">`) are passed through untouched, so a
wrong path is only noticed when someone looks at the published page. This script closes that
gap: it resolves every image/media reference on every built page the way a browser does and
fails if the file is not there.

Usage:
    python check-images.py <site-dir>        # e.g. the directory from `mkdocs build`

Run from check-links.sh (pre-push hook) and from the GitHub Actions workflow.
"""

from __future__ import annotations

import posixpath
import re
import sys
import urllib.parse
from pathlib import Path

# src/data-src of anything that loads media, plus poster images of <video>.
REF_RE = re.compile(
    r"<(?:img|source|video|embed|object|iframe)\b[^>]*?\b(?:src|data-src|data|poster)=\"([^\"]+)\"",
    re.IGNORECASE,
)
SKIP_RE = re.compile(r"^(?:https?:|data:|blob:|mailto:|//)", re.IGNORECASE)


def resolve(site: Path, page_dir: str, src: str) -> Path:
    """Resolve an image reference to a file path, the way a browser would."""
    path = urllib.parse.unquote(src.split("?")[0].split("#")[0])
    if path.startswith("/"):            # absolute: from the site root
        target = path.lstrip("/")
    else:
        target = posixpath.normpath(posixpath.join(page_dir, path))
        while target.startswith("../"):  # browsers never go above the site root
            target = target[3:]
    return site / target


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    site = Path(argv[1]).resolve()
    if not site.is_dir():
        print(f"Error: '{site}' is not a directory. Build the site first (mkdocs build).")
        return 2

    pages = sorted(site.rglob("*.html"))
    broken: list[tuple[str, str, str]] = []
    checked = 0
    for page in pages:
        page_dir = page.relative_to(site).parent.as_posix()
        for src in REF_RE.findall(page.read_text(encoding="utf-8")):
            src = src.strip()
            if not src or SKIP_RE.match(src):
                continue
            checked += 1
            target = resolve(site, page_dir, src)
            if not target.exists():
                broken.append((page.relative_to(site).as_posix(), src,
                               target.relative_to(site).as_posix()))

    print(f"Checked {checked} image references in {len(pages)} pages.")
    if not broken:
        print("No broken images found.")
        return 0

    print(f"\n{len(broken)} broken image reference(s):")
    for page, src, target in broken:
        print(f"  {page}\n    src=\"{src}\" -> missing {target}")
    print("\nTip: paths in raw HTML <img> tags are relative to the page URL, not to the .md file.")
    print("A page at docs/dvl/foo.md is served as /dvl/foo/, so an image in docs/img/ is '../../img/'.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
