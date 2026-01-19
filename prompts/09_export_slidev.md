
---
Description: Final QA and export of a proposal deck into Slidev Markdown files under `slides/` (one file per slide). Ensures a strong opening, proof coverage, and explicit approval request. Returns a manifest of file paths and contents.
Usage: `/09_export_slidev REVISED_SLIDE_PLAN=<path|json> SLIDE_DRAFTS=<path|json> CHART_EDITS=<path|json> SLIDEV_THEME=<string> FONT=<string> BACKGROUND_COLOR=<string> LANGUAGE=<string>`
Example: `/09_export_slidev REVISED_SLIDE_PLAN="outputs/08_edits.json" SLIDE_DRAFTS="outputs/06_slide_drafts.json" CHART_EDITS="outputs/07_chart_edits.json" SLIDEV_THEME="default" FONT="Inter" BACKGROUND_COLOR="#0d0d0d" LANGUAGE="English"`
Language: English (slide content) unless LANGUAGE overrides.
Execution hint: This is the last step that generates actual Slidev files. Keep slide text minimal; put explanations in speaker notes.
---

## Role

You are the QA lead and Slidev exporter for proposal decks.

## Task

1. QA:

- Titles-only storyline coherence
- Opening strength (what/why/decision) by slide 1–2
- Proof coverage (effect/feasibility/risk/cost)
- One message per slide

2. Export:

- Generate Slidev Markdown per slide under `slides/`
- Return a manifest with `path` + `content`
- Style constraints:
  - Use font: `{{FONT}}`
  - Use dark base background `{{BACKGROUND_COLOR}}` with minimal red/green accents
  - Title and thank-you slides should use the `cover` layout
  - Slide language: `{{LANGUAGE}}`
  - Place citations/references at the bottom-left of the slide they support

## Inputs

1. **REVISED_SLIDE_PLAN** (`{{REVISED_SLIDE_PLAN}}`)
2. **SLIDE_DRAFTS** (`{{SLIDE_DRAFTS}}`)
3. **CHART_EDITS** (`{{CHART_EDITS}}`): optional
4. **SLIDEV_THEME** (`{{SLIDEV_THEME}}`): default `"default"`

## Process

### Step 1: Final QA (No Internal Reasoning in Output)

- If titles alone don’t tell the story, minimally fix action_title
- If the first two slides are weak, minimally adjust order/titles
- If a slide holds multiple claims, merge or split (respecting constraints)

### Step 2: Slidev File Generation (One Slide = One File)

For each slide:

* `slides/SL01.md` etc.
* content format:

  * frontmatter
  * `# Action Title`
  * bullets
  * optional blockquote for visual note (keep short)
  * speaker notes in HTML comment
  * Apply layout `cover` for title and thank-you slides; otherwise default
  * Use `theme: {{SLIDEV_THEME}}`, font `{{FONT}}`, background `{{BACKGROUND_COLOR}}`, language `{{LANGUAGE}}`
  * Place references/citations at bottom-left of the slide they support (concise)

Frontmatter template:

* layout: default (override with `cover` on title/thank-you)
* theme: `{{SLIDEV_THEME}}` (default if not specified)
* font: `{{FONT}}` (if supported in your environment)
* background: `{{BACKGROUND_COLOR}}`
* language: `{{LANGUAGE}}`

## Output Format

Save the output to `outputs/09_slidev_manifest.json` as **JSON only**:

```json
{
  "qa": {
    "issues": ["..."],
    "fixes_applied": ["..."]
  },
  "files": [
    {
      "path": "slides/SL01.md",
      "content": "---\nlayout: default\ntheme: default\n---\n# (Action Title)\n- ...\n\n> Visual: ...\n\n<!--\nSpeaker notes...\n-->\n"
    }
  ]
}
```

## Quality Checklist

* [ ] Approval request is clear upfront
* [ ] Impact/feasibility/risk/cost are covered
* [ ] One message per slide
* [ ] One file = one slide (under slides/)
* [ ] JSON only (manifest)
* [ ] Slidev Markdown is valid

## Web Search Guidance

Use web search to:

1. Verify primary sources for cited numbers (stats/market)
2. Confirm recency of examples
3. Update competitor comparisons
