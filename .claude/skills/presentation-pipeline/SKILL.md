---
name: presentation-pipeline
description: Turn a single Markdown brief into a production-quality Slidev deck via a 9-step strategy→architecture→content→export pipeline (McKinsey/BCG logic + Jobs/Bezos/Duarte narrative). Use when the user wants to generate, draft, or architect a presentation/slide deck from raw notes, or asks to "run the presentation pipeline". Originated from the acp26/week1 branch.
---

# presentation-pipeline

Build a Slidev deck from one brief by running nine sequential stages. Each stage
reads the previous stage's JSON, applies a specific mental model, and writes its
own JSON to `outputs/`. The final stage writes the actual `slides/SL*.md` files.

The full specification for each stage lives in `prompts/0N_*.md` (bundled with
this skill). **Treat each prompt file as the authoritative instruction for that
stage** — open it, follow its Role / Process / Output Format / Quality Checklist
exactly, and emit the JSON it specifies.

## Inputs

The single source of truth is a brief with YAML frontmatter + Markdown body:

```markdown
---
target_audience: "..."          # required
audience_type: group            # individual | group | mixed
constraints:
  max_slides: 15
  max_duration_minutes: 15
output_language: Japanese        # or English
event:                           # optional
  name: "..."
---

# Title
...raw content...
```

A template is at `inputs/introduction.example.md`. If the user has not pointed to
a brief, ask for the path (default `inputs/introduction.md`) before starting.

`inputs/rules.md` captures slide-design rules established on earlier decks — read
it before stage 06/07 and respect it.

## The 9 stages

| # | Stage | Reads | Writes | Lens |
|---|-------|-------|--------|------|
| 1 | Context Analysis | the brief | `outputs/01_Context_Brief.json` | Bezos — find the SCR narrative |
| 2 | Audience Persona | 01 | `outputs/02_Audience_Persona.json` | Jobs — "what keeps them up at night?" |
| 3 | Core Strategy | 01, 02 | `outputs/03_Core_Strategy.json` | Jobs+Bezos — villain/hero, core message |
| 4 | Governing Argument | 03 (+02) | `outputs/04_Governing_Argument.json` | McKinsey — Pyramid Principle, MECE |
| 5 | Narrative Blueprint | 04, 03, 01 | `outputs/05_Narrative_Blueprint.json` | Jobs — Action Titles, Skim Test |
| 6 | Slide Drafting | 05, 04, 01 | `outputs/06_Slide_Content.json` | Bezos — notes first, evidence hierarchy |
| 7 | Visual Design | 06 | `outputs/07_Visual_Design.json` | Jobs+BCG — show don't tell, 1 chart 1 message |
| 8 | Executive Review | 07, 03, 01 | `outputs/08_Executive_Review.json` | gatekeeper — "not good enough", source fidelity |
| 9 | Final Export | 08, 07, 06 | `slides/SL*.md` (+ `outputs/09_Final_Export.json`) | assembler — apply revisions, WRITE FILES |

Stage 9's real deliverable is the `slides/SL*.md` files on disk, not JSON.

## How to run (in-conversation, default)

Run the stages yourself, one at a time, in order:

1. Ensure `outputs/` exists. Confirm (or ask for) the brief path.
2. For each stage 1→9: read `prompts/0N_*.md`, read the listed input JSON(s),
   produce the output per that file's **Output Format**, and Write it to the
   specified path. Show the user a 1–2 line summary per stage, not the whole JSON.
3. Between stages, honor that stage's Quality Checklist before moving on. If a
   checklist item fails (e.g. Skim Test, MECE, 3-Second Test), iterate that
   stage before continuing — a weak early stage poisons everything downstream.
4. After stage 9, list the slide files created and offer `bun run dev` to preview.

Pause for user confirmation after stage 3 (strategy) and stage 5 (blueprint) when
the deck is high-stakes — these are the cheapest points to course-correct.

## How to run (headless CLI, optional)

A `Makefile` is bundled that drives the same pipeline by shelling out to the
`claude` CLI per stage (`make all`, or a single stage like `make core_strategy`).
Use this only when the user explicitly wants the non-interactive batch mode; it
expects `prompts/`, `inputs/introduction.md`, and writes to `outputs/`/`slides/`
relative to wherever it's invoked. The in-conversation flow above is the default.

## Adapting to this repo's design system

The bundled stage 07 prompt assumes a generic dark theme (`#0f0f0f` bg, mermaid,
stock Slidev layouts). **This repo (presentation-agent) overrides that** — it has
its own light-theme design system documented in `CLAUDE.md` (the `nx-*` tokens,
Shippori Mincho / Cormorant typography, one-visual-per-slide SVG discipline,
`severe` 赤茶 vs `accent` 青 semantics). When generating slides for THIS repo,
follow `CLAUDE.md`'s design system, not stage 07's generic color/layout table —
use the pipeline for the strategy/argument/narrative spine and let the repo's
visual language govern the final SVG/Markdown.

## Notes

- Output language follows `output_language` in the brief; stage JSON is English
  internally, but slide-facing copy uses the requested language. Per `CLAUDE.md`,
  Japanese decks omit English `.ja` subtext.
- Keep stage outputs as valid JSON — downstream stages parse them.
- Don't skip stages; each guards a failure mode the next one assumes is handled.
