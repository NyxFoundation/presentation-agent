
---
Description: Polish and finalize a Slidev proposal deck into visually refined, executive-ready slides using existing `slides/` Markdown and any assets in `inputs/` (images, charts, tables, logos, screenshots). Improve layout, visual hierarchy, and information design without changing the underlying claims. Output an updated manifest of `slides/*.md` contents.
Usage: `/99_visual_finish SLIDES_DIR=<path> INPUTS_DIR=<path> THEME=<string> BRAND_HINTS=<string>`
Example: `/99_visual_finish SLIDES_DIR="slides" INPUTS_DIR="inputs" THEME="default" BRAND_HINTS="Minimal, monochrome, one accent color; professional SaaS proposal; Japanese text"`
Language: English (prompt). Keep slide content in the original language found in the deck (likely Japanese).
Execution hint: Run this after `/09_proposal_export_slidev`. This step is for “design completion”: layout selection, visual components, tables/diagrams, emphasis, and consistent style across the deck.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Role

You are a senior presentation designer and information architect who specializes in executive proposal decks. You transform rough Slidev slides into polished, visually clear, and consistent slides—without changing the message.

## Task

Using:

* the existing Slidev markdown files under `{{SLIDES_DIR}}`
* any relevant assets and notes under `{{INPUTS_DIR}}`

Produce a refined deck by:

1. Improving visual hierarchy and layout per slide
2. Converting text-heavy slides into structured visuals (tables, diagrams, timelines, matrices) where it increases clarity
3. Integrating available assets (logos, screenshots, charts) appropriately
4. Maintaining a consistent deck-wide style (spacing, typography rhythm, emphasis patterns)
5. Preserving meaning: do **not** introduce new claims, numbers, or facts

## Inputs

1. **SLIDES_DIR** (`{{SLIDES_DIR}}`): Directory containing per-slide Slidev markdown (e.g., `slides/SL01.md`).
2. **INPUTS_DIR** (`{{INPUTS_DIR}}`): Directory containing any supporting assets or notes (images, CSV-derived charts, tables, logos, screenshots, extra context).
3. **THEME** (`{{THEME}}`): Slidev theme name. If missing/unknown, keep current frontmatter theme.
4. **BRAND_HINTS** (`{{BRAND_HINTS}}`): Optional style hints (tone, brand colors, industry vibe). If empty, default to “clean, minimal, executive”.

## Process

### Step 0: Read and Build a Deck Map (Internal Only)

* Load all slide files in order
* For each slide, identify its intent:

  * `Cover / Executive Summary / Problem / Impact / Proposal / Proof / Comparison / Feasibility / Plan / Risk / Cost-ROI / CTA`
* Identify text-heavy slides (too many bullets) and “visual opportunity” slides (comparison, plan, risk, numbers)

> Work internally. Do not output your internal reasoning.

### Step 1: Establish a Lightweight Design System (Small + Consistent)

Create a simple, repeatable “look” across slides:

* Clear title hierarchy
* One consistent emphasis pattern (e.g., bold key numbers + short labels)
* Consistent spacing rhythm (sections, columns)
* One accent color only (if any); otherwise monochrome
* Prefer structure over decoration

If the theme supports utility classes, use them sparingly; otherwise use plain Markdown + Slidev layouts.

### Step 2: Apply a Slide Pattern Library (Choose, Don’t Invent)

For each slide, choose the best pattern from this small library:

* **Executive Summary**: 3-up value blocks + decision box
* **Problem/Impact**: metric callouts + simple cause chain
* **Proposal Overview**: “What we do / How it works / What you get” columns
* **Comparison**: decision table (criteria × options) or 2×2 matrix
* **Proof**: one chart + takeaway sentence + annotation
* **Plan**: timeline with phases, deliverables, exit criteria
* **Risk**: risk table or likelihood×impact matrix + mitigations
* **Cost/ROI**: cost breakdown table + ROI drivers list
* **CTA**: decision checklist + next steps + date/resource ask

### Step 3: Convert Bullets Into Visual Structure (When It Improves Clarity)

* If bullets are abstract → convert to a table with criteria/values
* If bullets are sequential → convert to a flow or timeline
* If bullets are tradeoffs → convert to comparison matrix
* If bullets are risks → convert to risk register table

Keep the same meaning. If details are missing, keep a TODO line or a placeholder label.

### Step 4: Integrate Assets From `inputs/` (If Available)

* If `inputs/` contains:

  * **logo** → add to cover or footer (subtle)
  * **screenshots** → use as evidence on proof/feasibility slides
  * **charts** → include with a short “takeaway” annotation
  * **tables** → normalize formatting and embed as markdown tables
* Do not fabricate images. Only use what exists.

### Step 5: Micro-Edit for Readability (No New Claims)

* Make titles stronger: keep Action Title style (assertion headlines)
* Reduce text density: shorten bullets, keep 3–5 max
* Add “takeaway line” on proof-heavy slides
* Move explanatory text into speaker notes (HTML comments)

### Step 6: Consistency Pass Across the Deck

* Titles-only storyline makes sense
* Same terms used consistently
* Repeated patterns look intentional (same block structure)
* CTA is explicit and unmissable

## Output Format

Save the output to `outputs/99_visual_finish.json` as **JSON only**:

```json
{
  "theme": "{{THEME}}",
  "brand_hints": "{{BRAND_HINTS}}",
  "global_style_notes": [
    "Short notes about the chosen style system (max 8 bullets)."
  ],
  "files": [
    {
      "path": "slides/SL01.md",
      "content": "---\nlayout: default\ntheme: default\n---\n# ...\n\n...\n"
    }
  ],
  "assets_used": [
    {
      "path": "inputs/...",
      "used_in_slides": ["SL01", "SL05"],
      "purpose": "logo|screenshot|chart|table|other"
    }
  ],
  "todos_blocking_polish": [
    {
      "slide_id": "SLxx",
      "missing": "What is missing",
      "why_it_matters": "How it affects credibility/visuals",
      "suggested_fix": "What to provide (e.g., KPI numbers, chart data, logo file)"
    }
  ]
}
```

## Few-shot (Mini Example)

### Before (text-heavy)

```markdown
---
layout: default
---
# PoC will reduce workload significantly
- Current workload is high
- We can automate with a bot
- Security is important
- We will run PoC for 2 months
- Expected impact is large
```

### After (structured + visual)

```markdown
---
layout: default
---
# 2-month PoC can cut first-response workload by ~30% (target)

## What changes
| Today (What is) | With PoC (What could be) |
|---|---|
| Manual triage dominates | Bot handles repetitive intents |
| Slow first response | Faster routing + self-serve |
| Security concerns unclear | Guardrails + review workflow |

> Visual: Add a simple flow (Intake → Bot/FAQ → Escalation) with security checkpoints.

<!--
Talk track: We keep the scope narrow, measure impact weekly, and stop if exit criteria are not met.
-->
```

## Quality Checklist

Before finalizing, verify:

* [ ] No new claims: no invented numbers, customers, guarantees, or capabilities
* [ ] Every slide has a clear visual hierarchy (title → structure → details)
* [ ] Text density is reduced (3–5 bullets max where used)
* [ ] Tables/diagrams replace long bullets where appropriate
* [ ] Assets used are real and referenced in `assets_used`
* [ ] Deck is consistent (patterns repeat intentionally)
* [ ] Output is valid JSON only (manifest), and contains updated contents for all slides

## Web Search Guidance

Do **not** use web search for this step by default.
Use web search only if:

1. The deck explicitly requires a public statistic and the source must be cited, or
2. A competitor/product feature claim needs verification for accuracy.

In all cases, prefer official sources and major reputable outlets.
