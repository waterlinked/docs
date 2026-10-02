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

> **Note:** `mkdocs serve` and `mkdocs build` do *not* generate the PDF manuals, because that
> takes a few minutes and needs Chromium. The "Download PDF" buttons therefore point to files
> that do not exist until you have built them once. To build and serve the complete site,
> website plus PDFs, run:
>
> ```sh
> scripts/build_site.sh --serve
> ```
>
> See [PDF manuals](#pdf-manuals) for the details and for reviewing the PDFs of a pull request.

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

### Building the complete site locally

The normal `mkdocs serve` / `mkdocs build` only builds the website. The PDFs are a separate,
slower step, so that editing pages stays fast and contributors who only fix text do not need
Chromium. To build everything in one go (website, PDFs, website again so it serves the PDFs
under `/pdf/`):

```sh
scripts/build_site.sh            # full build into site/ and docs/pdf/
scripts/build_site.sh --serve    # same, then serves it on http://localhost:8000
```

The first run downloads Chromium for Playwright (about 115 MB, once). The PDFs are written to
`docs/pdf/`, which is ignored by git, and every later `mkdocs serve` or `mkdocs build` includes
them until you delete that folder.

To run the PDF step on its own:

```sh
uv run playwright install chromium   # once
uv run python scripts/build_pdf.py
uv run python scripts/build_pdf.py --only "Underwater GPS"   # just one product
```

### Reviewing the PDFs of a pull request

The PDFs are part of the review. Two ways to get them:

* **Without building anything:** after a push, GitHub Actions builds the PDFs for every branch.
  Open the workflow run of the branch (Actions tab), download the `pdf-manuals` artifact and
  open the PDFs.
* **Locally:** check out the branch and run `scripts/build_site.sh --serve`, then use the
  "Download PDF" buttons or open `docs/pdf/` directly.

Things to look at: the cover (logo, product name, date), the table of contents against the `nav`,
page breaks around tables and images, and that every page of the section is present. The build
itself fails if a nav page is missing from a PDF, an internal link is broken or an image is
missing. On `master` the PDFs are published with the website under `/pdf/`.

Styling of the PDFs is in `scripts/pdf/pdf.css`, the button is in
`overrides/partials/pdf-download.html`.


## Deploy changes to server
After the changes have been tested and they work, push the changes to a branch, and make a merge request. The documentation site will built automatically and links will be verified.

Once the pull request is merged the documentation will be automatically built and published to https://docs.waterlinked.com.
