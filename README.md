# Claudia Neuendorf — academic website (revised)

A static GitHub Pages site, based on the supplied CVs. The archived original poster is included under `poster/`. The files do not include a `.git` folder.

## Preview before publishing

Open this folder in VS Code and start a local HTTP server (for example, in VS Code Terminal run `python -m http.server 8000`). Then visit `http://localhost:8000/`. Opening `index.html` directly as a file will prevent the browser loading local JSON.

## Publishing safely

1. Back up your Git repository (you already have an original ZIP).
2. Create a development branch in Gitnuro (for example `website-redesign`).
3. Copy **the contents of this ZIP** into the repository root, not into a nested folder. Do not overwrite your repository's `.git` folder or other Git configuration.
4. Preview and check all links. Then commit, push and merge into the publishing branch when ready. GitHub Pages must publish from the configured branch/root.
5. The archived original poster is at `https://claudiandf.github.io/poster/`. Some original asset links may need checking after moving the old site into a subfolder.

## Adding a conference PDF (once a month is fine)

1. Put a file in `conferences/2027/` (create the year folder), for example `abstract.pdf` and `poster.pdf`.
2. Open `data/conferences.json`. Add a new JSON object, preserving commas and quotation marks. Example:

```json
{
  "title": "Presentation title",
  "conference": "EARLI 2027",
  "location": "City, Country",
  "date": "2027-08-25",
  "authors": "Neuendorf, C., et al.",
  "topics": ["classroom-heterogeneity"],
  "abstract": "conferences/2027/abstract.pdf",
  "poster": "conferences/2027/poster.pdf"
}
```

3. Commit and push. An entry with no PDF file leaves the link out; add files and paths only when ready. Dates for the two existing historical conferences are month placeholders because the CV gives their years but not exact presentation dates; replace those dates when known.

## Updating the CV

Replace `assets/Claudia_Neuendorf_CV_2026.pdf` to update the CV.

## Automatically updating publications from ORCID

- Current list: `data/publications.json` (seeded from the 2026 CV, selected entries).
- Schedule: `.github/workflows/update-publications.yml` (weekly, and manually triggerable).
- Set repository Actions secrets `ORCID_CLIENT_ID` and `ORCID_CLIENT_SECRET` for ORCID Public API access, then run workflow once manually. Without the secrets, the initial CV-based list remains functional.
- The sync script appends newly discovered public records and retains manually curated entries. Newly added publications can be given topic tags in `data/publications.json`, using any of: `classroom-heterogeneity`, `peer-networks`, `high-achievers`, `methodology`, `open-science`. You can tag a publication in more than one area. This is the only topic-specific manual upkeep.
- Crossref enrichment, robust deduplication of substantially retitled preprints, or automated identification of conference materials are **not** implemented; manually check occasionally.
- ORCID may not have every publication. This workflow does not delete manually curated entries.

## Latest updates

The homepage assembles the newest five items from publications, conferences and `data/news.json`. New entries need a real date for accurate ordering. Publications with only a year are sorted at year granularity and may display ahead of or behind dated entries within the same year.

## Original poster archive

The folder `poster/` contains your original conference website files extracted from your uploaded ZIP, without the `.git` directory.
