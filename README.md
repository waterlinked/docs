# W-DN-17002 User Manuals

[![Deploy Water Linked Docs](https://github.com/waterlinked/waterlinked.github.io/actions/workflows/build.yml/badge.svg)](https://github.com/waterlinked/waterlinked.github.io/actions/workflows/build.yml)

We are using mkdocs to manage our documentation.

# Contributing

We're really happy if you want to contribute to make the documentation better!
This is done by creating a pull request.

1. Download, install dependencies

Make sure you have Python3 installed.

```
git clone https://github.com/waterlinked/docs.git
cd docs

python -m venv venv
source venv/bin/activate (Linux)
venv\Scripts\activate.bat (Windows)
pip install -r requirements.txt

./install-hooks.sh  # (Optional) To automatically check links on git push
```

2. Make changes using your favorite editor

3. Test them

```
mkdocs serve  # Allow you to view the changes on your browser
```
* Fire up your browser and go to localhost:8000

Verify links are valid:

```
./check-links.sh
```

## Deploy changes to server
After the changes have been tested and they work, push the changes to a branch, and make a merge request. The documentation site will built automatically and links will be verified.

Once the pull request is merged the documentation will be automatically built and published to https://docs.waterlinked.com.
