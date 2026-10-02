#!/usr/bin/env bash
# Build the COMPLETE site locally: the website plus the PDF manuals, exactly as CI publishes it.
#
#   scripts/build_site.sh            # full build → site/ with the PDFs under site/pdf/
#   scripts/build_site.sh --serve    # same, then start `mkdocs serve` so you can click the
#                                    # "Download PDF" buttons at http://localhost:8000
#
# A plain `uv run mkdocs serve` / `mkdocs build` does NOT generate the PDFs (that takes a few
# minutes and needs Chromium), so the "Download PDF" buttons point at files that do not exist
# until this script, or `scripts/build_pdf.py`, has run once. The PDFs are written to docs/pdf/
# (gitignored) and picked up by every following site build.
set -e -u -o pipefail
cd "$(dirname "$0")/.."

if ! uv run python -c "import playwright" 2>/dev/null; then
  echo "Error: run 'uv sync --locked' first." >&2; exit 1
fi
echo "== Making sure Chromium for the PDF generation is installed (downloads ~115 MB the first time) ..."
uv run playwright install chromium

echo "== 1/3 Building the website ..."
uv run mkdocs build --strict -d site
echo "== 2/3 Generating and verifying the PDF manuals (a few minutes) ..."
uv run python scripts/build_pdf.py --site-dir site --out-dir docs/pdf
echo "== 3/3 Rebuilding the website so it includes the PDFs under /pdf/ ..."
uv run mkdocs build --strict -d site
echo "== Done. PDFs: docs/pdf/ and site/pdf/"
ls -la docs/pdf/*.pdf

if [ "${1:-}" = "--serve" ]; then
  echo "== Starting mkdocs serve; open http://localhost:8000 and use the Download PDF buttons"
  exec uv run mkdocs serve
fi
