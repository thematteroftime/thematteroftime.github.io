# Jiedong Zhang · Personal website

Live: https://thematteroftime.github.io/

- English: `index.html`
- Chinese: `zh.html`
- Editable text: `content/en.json`, `content/zh.json`
- Shared page and interaction logic: `src/page.html`
- Existing design runtime: embedded in `src/bundle.html`

After editing content or the template, run:

```sh
python3 scripts/build.py
```

Commit the generated HTML with the source changes. GitHub Pages publishes the root of `main`.

The language switch retains the current project route and reading position. Both pages share the same image assets and saved theme. Resume downloads match each page’s language: `assets/Resume-Chinese.pdf` and `assets/Resume-English.pdf`.

## Image provenance

- `portrait-piano.jpg`: supplied photograph at the piano.
- `rokid-award.webp`: supplied Agentcraft trophy and certificate photograph.
- `hackathon-building.webp`, `hackathon-team.webp`: supplied photographs from AI Hackathon Tour at Shanghai Jiao Tong University.
- `plasma-simulation.webp`: `docs/images/fig5_best_case_E2_showcase.png` from the author's public [agentic-md-for-dummies repository](https://github.com/thematteroftime/agentic-md-for-dummies), illustrating a PRX 2015 reproduction. It is not presented as an experimental hardware result.

Images are resized WebP copies with metadata removed. Original application documents, identity documents and account screenshots are not part of this repository.

## Additional public material (2026-11-16)

- `lazy-paper-garden.webp`: resized from `docs/assets/v119-garden-live.png` in the author’s public [lazy-paper repository](https://github.com/thematteroftime/lazy-paper). Interface example only; library counts are not current research metrics.
- `rokid-ambassador.webp`: supplied Rokid campus ambassador appointment photograph, September 2025–July 2026, from `c5f8e97ed8eedd6cfdb8b55895a43270.jpg`.
- The lazy-paper project description follows its public README; it does not claim a publication or measured research outcome.

## Research context refresh (2026-11-16)

Active-vision, SVSDF and OPENARM summaries were cross-checked against current project discussion records. Descriptions cover research questions, personal contributions and engineering work in progress. Internal infrastructure details, unpublished manuscript figures, model weights, experimental videos and unverified performance claims are excluded. CV files are unchanged by this content-only refresh.

## Project image selection (2026-11-16)

- `active-vision-dual-view.webp`: resized `demo2_2.jpg` from the project roadshow review. Its adjacent `metadata.json` identifies this frame as a sample of `投币任务双视角回放.mp4` (21.267 s, 1280×360). This is data-collection footage, not a policy-success demonstration.
- `svsdf-test-scenes.webp`: resized `models/se3_racing_suite/renders/suite_overview.jpg` from the user’s planning project. Scene geometry preview only; not an algorithm trajectory or dynamics result.
- `openarm-platform-reference.webp`: resized from [Enactic/OpenArm’s official README image](https://github.com/enactic/openarm/blob/main/website/static/img/hardware/openarm_and_cell.png). Official platform reference, not a photograph of this author’s deployment. Original source: https://raw.githubusercontent.com/enactic/openarm/main/website/static/img/hardware/openarm_and_cell.png .

All three pictures are shared by the Chinese and English pages, retain their aspect ratios, and have metadata removed. Original project assets are unchanged.

## Keeping CV downloads current

Replace `assets/Resume-English.pdf` and `assets/Resume-Chinese.pdf` with the latest approved exports, then run `python3 scripts/build.py` and publish both generated HTML files. The build derives a download URL version from each PDF’s content hash and includes both hashes in the bilingual page release. Updated PDF content therefore refreshes download links automatically. The version labels are derived from the actual files, not manually entered dates.

The complete supplied piano photograph is also shown in the gallery, alongside the two existing hackathon photographs. The certificate photograph is described as a next-round certificate rather than a competition award.
