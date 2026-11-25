#!/bin/bash
# Pre-push hook: Custom linkchecker for local links, Build MkDocs locally and run LinkChecker on external links

# Exit on error
set -e

# === Paths ===
PROJECT_ROOT="$(git rev-parse --show-toplevel)"
TMP_BUILD_DIR="$PROJECT_ROOT/.tmp-mkdocs-build"
DOCS_DIR="$PROJECT_ROOT/docs"

if ! command -v uv >/dev/null 2>&1; then
    echo "Error: uv is required. See the README for installation instructions."
    exit 1
fi

#Checking internal links in markdown files only
echo "Checking internal links in markdown files..."

set +e
#Using custom python script for internal link checking:
uv run --project "$PROJECT_ROOT" python "$PROJECT_ROOT/check-internal-links.py" "$DOCS_DIR"
RESULT_INTERNAL=$?

set -e

if [ $RESULT_INTERNAL -ne 0 ]; then
    echo "Internal linkcheck failed! Please fix Markdown links before pushing."
    exit 1
fi

echo "Internal linkcheck passed!"

# Remove old temp build if it exists
rm -rf "$TMP_BUILD_DIR"

# Build MkDocs into temporary directory
echo "Building MkDocs locally into $TMP_BUILD_DIR..."
uv run --project "$PROJECT_ROOT" python -m mkdocs build -d "$TMP_BUILD_DIR"

# Images in raw HTML <img> tags are not validated by mkdocs, so check them against the build
echo "Checking images..."
set +e
uv run --project "$PROJECT_ROOT" python "$PROJECT_ROOT/check-images.py" "$TMP_BUILD_DIR"
RESULT_IMAGES=$?
set -e

if [ $RESULT_IMAGES -ne 0 ]; then
    rm -rf "$TMP_BUILD_DIR"
    echo "Image check failed! Please fix the image paths before pushing."
    exit 1
fi

echo "Image check passed!"

# LinkChecker must read the build over HTTP. With file:// paths a link such as "dvl/overview/" is
# a folder, so LinkChecker lists the folder and never opens the page in it. Only the links on the
# front page were then checked.
# The server is started with the Python of the project directly, not through "uv run", so that
# SERVER_PID is the server itself and it can be stopped.
PYTHON="$(uv run --project "$PROJECT_ROOT" python -c 'import sys; print(sys.executable)')"
PORT="$("$PYTHON" -c 'import socket; s = socket.socket(); s.bind(("127.0.0.1", 0)); print(s.getsockname()[1])')"
"$PYTHON" -m http.server "$PORT" --bind 127.0.0.1 --directory "$TMP_BUILD_DIR" >/dev/null 2>&1 &
SERVER_PID=$!
# Stop the server and remove the build when the script ends, also when it fails
LINK_REPORT="$(mktemp)"
trap 'kill "$SERVER_PID" 2>/dev/null || true; rm -rf "$TMP_BUILD_DIR" "$LINK_REPORT"' EXIT

# Wait until the server answers
for _ in $(seq 1 50); do
    if "$PYTHON" -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:$PORT/', timeout=1)" >/dev/null 2>&1; then
        break
    fi
    sleep 0.2
done

echo "Running LinkChecker on external links against local build..."
set +e
# Only report broken links. Redirects are warnings and are not reported.
# Links that are not checked:
#   - docs.waterlinked.com: every page has a canonical link to its published address. A new page
#     is not published yet when it is checked here.
#   - 192.168.x.x and waterlinked-<product>: addresses of a device on the reader's own network.
#   - octopart.com and support.blueye.no: answer 403 to automated requests.
uv run --project "$PROJECT_ROOT" linkchecker "http://127.0.0.1:$PORT/" \
    --no-status \
    --no-warnings \
    --check-extern \
    --timeout=30 \
    --ignore-url='sitemap\.xml\.gz' \
    --ignore-url='https://github.com/.*/edit/' \
    --ignore-url='https://www.youtube.com/' \
    --ignore-url='.*/assets/.*' \
    --ignore-url='.*/images/.*' \
    --ignore-url='.*/pdf/waterlinked-.*\.pdf$' \
    --ignore-url='^https://docs\.waterlinked\.com/' \
    --ignore-url='^https?://192\.168\.' \
    --ignore-url='^https?://waterlinked-[a-z0-9-]+(/|$)' \
    --ignore-url='^https://octopart\.com/' \
    --ignore-url='^https://support\.blueye\.no/' \
    | tee "$LINK_REPORT"
# The PDF manuals are verified by scripts/build_pdf.py

RESULT_EXTERNAL=${PIPESTATUS[0]}
set -e

# On GitHub Actions, show every broken link on the summary page of the run
if [ $RESULT_EXTERNAL -ne 0 ] && [ -n "$GITHUB_ACTIONS" ]; then
    awk '/^URL /      { url = $0; sub(/^URL +/, "", url) }
         /^Parent URL/ { parent = $0; sub(/^Parent URL +/, "", parent); sub(/^http:\/\/127\.0\.0\.1:[0-9]+/, "", parent) }
         /^Result +Error/ { result = $0; sub(/^Result +/, "", result); print "::error title=Broken link::" url " on page " parent " - " result }' "$LINK_REPORT"
fi

if [ $RESULT_EXTERNAL -ne 0 ]; then
    echo "External linkcheck failed! Please fix broken links before pushing."
    exit 1
fi

echo "External linkcheck passed!"
exit 0
