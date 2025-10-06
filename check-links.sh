#!/bin/bash
# Pre-push hook: Custom linkchecker for local links, Build MkDocs locally and run LinkChecker on external links

# Exit on error
set -e

# === Paths ===
PROJECT_ROOT="$(git rev-parse --show-toplevel)"
VENV_BIN="$PROJECT_ROOT/venv/bin"
TMP_BUILD_DIR="$PROJECT_ROOT/.tmp-mkdocs-build"
DOCS_DIR="$PROJECT_ROOT/docs"

# Activate venv if not already activated
if [ -f "$VENV_BIN/activate" ]; then
    . "$VENV_BIN/activate"
fi

#Checking internal links in markdown files only
echo "Checking internal links in markdown files..."

set +e
#Using custom python script for internal link checking:
python "$PROJECT_ROOT/check-internal-links.py" "$DOCS_DIR"
RESULT_INTERNAL=$?

set -e

if [ $RESULT_INTERNAL -ne 0 ]; then
    echo "Internal linkcheck failed! Please fix Markdown links before pushing."
    exit 1
fi

echo "Internal linkcheck passed!"

# Check if linkchecker exists
if ! command -v linkchecker >/dev/null 2>&1; then
    echo "Error: linkchecker executable not found in PATH"
    exit 1
fi

# Remove old temp build if it exists
rm -rf "$TMP_BUILD_DIR"

# Build MkDocs into temporary directory
echo "Building MkDocs locally into $TMP_BUILD_DIR..."
python -m mkdocs build -d "$TMP_BUILD_DIR"

echo "Running LinkChecker on external links against local build..."
set +e
# Only report broken links
linkchecker "file://$TMP_BUILD_DIR/index.html" \
    --no-status \
    --check-extern \
    --recursion-level=2 \
    --ignore-url='sitemap\.xml\.gz' \
    --ignore-url='https://github.com/.*/edit/' \
    --ignore-url='https://www.youtube.com/' \
    --ignore-url='.*/assets/.*' \
    --ignore-url='.*/images/.*'


RESULT_EXTERNAL=$?
set -e

# Clean up
rm -rf "$TMP_BUILD_DIR"

if [ $RESULT_EXTERNAL -ne 0 ]; then
    echo "External linkcheck failed! Please fix broken links before pushing."
    exit 1
fi

echo "External linkcheck passed!"
exit 0