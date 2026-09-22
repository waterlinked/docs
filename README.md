# W-DN-17002 User Manuals

[![Deploy Water Linked Docs](https://github.com/waterlinked/waterlinked.github.io/actions/workflows/build.yml/badge.svg)](https://github.com/waterlinked/waterlinked.github.io/actions/workflows/build.yml)

We are using mkdocs to manage our documentation.

# Contributing

We're really happy if you want to contribute to make the documentation better!
This is done by creating a pull request.

1. Download and install dependencies

Install [uv](https://docs.astral.sh/uv/getting-started/installation/). It will
install the required Python version and manage the virtual environment.

```sh
git clone https://github.com/waterlinked/docs.git
cd docs

uv sync --locked

./install-hooks.sh  # (Optional) To automatically check links on git push
```

2. Make changes using your favorite editor

3. Test them

```sh
uv run mkdocs serve  # Allow you to view the changes in your browser
```
* Fire up your browser and go to localhost:8000

Verify links are valid:

```sh
./check-links.sh
```
This also checks that all images resolve. Images written as raw HTML (`<img src="...">`) are not
checked by mkdocs, so they are verified against the built site by `check-images.py`. Note that such
paths are relative to the *page URL*, not to the markdown file: a page `docs/dvl/foo.md` is served
as `/dvl/foo/`, so an image in `docs/img/` is reached with `../../img/`. To run the check alone:

```sh
uv run mkdocs build -d /tmp/site && uv run python check-images.py /tmp/site
```

## PDF manuals

Every product (each top-level section in the `nav` of `mkdocs.yml`) is also published as a PDF
manual. Each page on the website has a "Download PDF" button for its product, and the home page
lists all manuals.

The PDFs are generated from the built website by `scripts/build_pdf.py`, so they always contain
the same pages and content. Page order and grouping follow the `nav`: when you add, remove or
move a page in the `nav`, the PDF changes with it. Nothing has to be updated by hand.

The build fails if a page from the `nav` is missing in its PDF, if an internal link is broken,
or if an image is missing.

To build the PDFs locally (written to `docs/pdf/`, which is ignored by git):

```sh
uv run playwright install chromium   # once
uv run python scripts/build_pdf.py
uv run python scripts/build_pdf.py --only "Underwater GPS"   # just one product
```

After a push, GitHub Actions builds the PDFs for every branch. They can be downloaded from the
workflow run ("pdf-manuals" artifact) to review them before merging. On `master` they are
published with the website under `/pdf/`.

Styling of the PDFs is in `scripts/pdf/pdf.css`, the button is in
`overrides/partials/pdf-download.html`.


## Deploy changes to server
After the changes have been tested and they work, push the changes to a branch, and make a merge request. The documentation site will built automatically and links will be verified.

Once the pull request is merged the documentation will be automatically built and published to https://docs.waterlinked.com.
