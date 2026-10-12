# Academic website — Claudia Neuendorf

A simple static academic homepage intended for **https://claudiandf.github.io/**, using GitHub Pages. No installation, build system, paid hosting, or ChatGPT/GitHub connection required.

## IMPORTANT: Preserve the existing conference poster *before* replacing the homepage

The **existing poster's source files were not available** when this ZIP was made. This archive does **not** contain the old poster or its images. Do not delete the existing repository files.

1. In your GitHub repository, locate the existing `index.html` and all files and folders used by that poster (images, PDF, stylesheets, scripts). If you cannot identify all dependencies, download a complete backup of the repository first (**Code → Download ZIP**).
2. On your computer, make a copy of the old site under a new `poster/` folder. Retain the **relative folder structure** of all its files and links. Make sure `poster/index.html` exists and its images, links and downloads work. Do not merely move the HTML without its assets. If your old site uses absolute links beginning with `/`, those may need to be updated to relative links.
3. Commit this archived copy **before** replacing the root `index.html`. Until you have successfully completed this archiving step, **do not upload the new root index.html**.
4. Once the poster works under `https://claudiandf.github.io/poster/`, upload the contents of this ZIP to the repository root, replacing only any matching files. Keep the `poster/` directory and any other existing files.

If the original site is not in the root directory or uses a framework/build process, adapt these instructions rather than overwriting blindly.

## Publishing (no GitHub plugin necessary)

1. Go to your existing GitHub Pages repository, usually named `claudiandf.github.io` (verify the actual name before proceeding).
2. Optionally use a new branch for review. For the simplest path, use **Add file → Upload files** to upload `index.html`, other HTML pages, `site.css`, `site.js`, `data/` and `scripts/` to the repository root. GitHub's browser upload interface might not reliably include hidden `.github` directories; upload the workflow separately using **Add file → Create new file** with the full path `.github/workflows/update-publications.yml`, or use git locally.
3. Under **Settings → Pages**, verify that Pages is configured to deploy from the intended branch and **/(root)** folder. This site needs no build tool and does not require changing to GitHub Actions as the Pages source.
4. Open https://claudiandf.github.io/ and check Home, Research, Publications, Projects, About, and `/poster/`.
5. If you used a review branch, merge only after testing. Branch previews are not automatically available at your normal Pages URL.

## Automatic ORCID publications (optional extra setup)

The site **works immediately** using `data/publications.json`, which has an initial curated selection derived from the 2026 CV. The updater requires an ORCID public API client and token; it will not automatically sync until the credentials are configured.

1. Register for ORCID public API credentials according to https://info.orcid.org/documentation/integration-and-api-faq/ . These are separate from GitHub authentication.
2. In your GitHub repository, open **Settings → Secrets and variables → Actions**, and create two repository **secrets**, named `ORCID_CLIENT_ID` and `ORCID_CLIENT_SECRET`.
3. Commit `.github/workflows/update-publications.yml` to the default branch. Under **Actions → Update ORCID publications**, use **Run workflow** to check the first sync.
4. The workflow is scheduled every Monday. GitHub may disable scheduled workflows in inactive repositories; if so, re-enable it in the Actions interface.
5. Review the first generated entries. Newly discovered public works are added; curated entries are kept, and no existing entries are removed. This avoids unexpected deletions but means retracted or corrected metadata must be reviewed manually.

### Data quality limitations

- The CV entries are **a selection**, not the entire eight-page bibliography. The publication page shows exactly what is in `data/publications.json`.
- The CV describes some manuscripts as *under review*. The initial list labels only documents with public preprint links as `Preprint`; **submission and acceptance are not asserted** unless verified.
- The ORCID works API's publication types and dates vary in quality; automated classification is provisional. Not all public ORCID works expose a URL or year, and such records will be skipped.
- Deduplication uses DOI and normalized title. Different titles for preprint and journal versions may still need manual reconciliation.
- Only published/public ORCID works are accessible; private items will not be displayed.
- The homepage shows the five most recent publications/preprints and optional news, sorted by year. Entries with the same year are sorted alphabetically, **not by exact publication date**, unless an optional `date` in `YYYY-MM-DD` format is provided.
- The script will not wipe existing records after a network/API error. If API secrets are missing, the workflow skips updating publications.

## Manual news: only when you actually have news

Edit `data/news.json` and add entries such as:

```json
[
  {
    "type": "News",
    "date": "2026-10-12",
    "title": "A new workshop resource is available",
    "url": "https://example.com/"
  }
]
```

Keep it as `[]` to omit news entirely. The homepage latest-updates list combines news with publication records. There is no blog or database.

## Editing the core content

- Homepage: `index.html`
- Research topics: `research.html`
- Project directory: `projects.html`
- Short bio: `about.html`
- Style and mobile layout: `site.css`
- Publication list: `data/publications.json`
- News: `data/news.json`

All pages are regular HTML. The site can be previewed locally with `python -m http.server 8000` from the extracted ZIP folder. Open http://localhost:8000/ — double-clicking index.html without a local server may prevent browsers from loading JSON files.

## Source information

Draft biography, positions, projects and seed publication records came from the user-uploaded `CV_2026_english.docx`. Before publishing, review for personal accuracy and preferred wording. No email, phone number, or photo has been included.
