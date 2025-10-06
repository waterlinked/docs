#!/usr/bin/env python3
import re
import sys
from pathlib import Path

# Regex for Markdown links: [text](target)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

def slugify_heading(text: str) -> str:
    """Convert Markdown heading text to MkDocs anchor format."""
    slug = text.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)  # remove punctuation
    slug = re.sub(r"\s+", "-", slug)      # spaces -> dashes
    return slug


def extract_headings(md_file: Path):
    """Return a set of anchor slugs from headings in md files."""
    headings = set()
    if not md_file.is_file():
        return headings
    for line in md_file.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            heading_text = line.lstrip("#").strip()
            headings.add(slugify_heading(heading_text))
    return headings

def check_md_file(md_file: Path):
    """Check links in md files."""
    errors = []
    if not md_file.is_file():  # <-- add this check
        return errors
    
    for line_number, line in enumerate(md_file.read_text(encoding="utf-8").splitlines(), start=1):

        stripped = line.strip()
        # Skip HTML and python comments
        if stripped.startswith("#"):
            continue
        elif stripped.startswith("<!--") and stripped.endswith("-->"):
            continue
        
        for match in LINK_RE.finditer(line):
            text, target = match.groups()

            # Skip external links
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            
            # Remove leading slash for site-root relative links
            elif target.startswith("/"):
                target = target[1:]

            # Split anchor from file
            if "#" in target:
                if target.startswith("#"):
                    file_part, anchor = md_file, target[1:]
                else:
                    file_part, anchor = target.split("#", 1)
            else:
                file_part, anchor = target, None

            # Resolve relative path'
            target_path = Path(file_part) if isinstance(file_part, Path) else Path(file_part) #Make sure it's a Path object
            target_file = (md_file.parent / target_path).resolve()

            if not target_file.exists() and not target_file.suffix:
                target_file = (md_file.parent / (target_path.name + ".md")).resolve()
                if not target_file.exists():
                    errors.append(f"{md_file}:{line_number}: File not found -> {target}")
                    continue

            if target_file.is_file() and anchor:
                headings = extract_headings(target_file)
                if anchor not in headings:
                    errors.append(f"{md_file}:{line_number}: Anchor not found -> {target}")

            if target_file.is_dir():
                continue
            
    return errors


def main(md_dir):
    md_dir = Path(md_dir)
    all_errors = []
    for md_file in md_dir.rglob("*.md"):
        all_errors.extend(check_md_file(md_file))

    if all_errors:
        print(f'Found {len(all_errors)} internal link errors in md files:')
        for e in all_errors:
            print(e)
        return 1
    print("No internal link errors found.")
    return 0

if __name__ == "__main__":
    exit(main(sys.argv[1]))
