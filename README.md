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

The language switch retains the current project route and reading position. Both pages share the same image assets and saved theme. The Chinese resume is available at `assets/Resume-Chinese.pdf`.

## Image provenance

- `portrait.webp`: supplied personal portrait.
- `rokid-award.webp`: supplied Agentcraft trophy and certificate photograph.
- `hackathon-building.webp`, `hackathon-team.webp`: supplied photographs from AI Hackathon Tour at Shanghai Jiao Tong University.
- `plasma-simulation.webp`: `docs/images/fig5_best_case_E2_showcase.png` from the author's public [agentic-md-for-dummies repository](https://github.com/thematteroftime/agentic-md-for-dummies), illustrating a PRX 2015 reproduction. It is not presented as an experimental hardware result.

Images are resized WebP copies with metadata removed. Original application documents, identity documents and account screenshots are not part of this repository.
