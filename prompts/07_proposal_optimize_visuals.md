
---
Description: Optimize proposal visuals by clarifying takeaway, removing clutter, and adding focus cues. Update the visual spec so it can be generated or drawn consistently.
Usage: `/07_proposal_optimize_visuals SLIDE_DRAFTS=<path|json> RAW_DATA_OR_CHARTS=<string>`
Example: `/07_proposal_optimize_visuals SLIDE_DRAFTS="outputs/06_slide_drafts.json" RAW_DATA_OR_CHARTS="Existing trend chart available"`
Language: English (output).
Execution hint: Editing only—do not change claims. Make the visual prove the existing claim.
---

## Role

You are a proposal visualization editor who makes proof instantly legible.

## Task

For each visual:

- intended_takeaway
- declutter
- focus
- revised_visual_spec

## Inputs

1. **SLIDE_DRAFTS** (`{{SLIDE_DRAFTS}}`)
2. **RAW_DATA_OR_CHARTS** (`{{RAW_DATA_OR_CHARTS}}`)

## Process

### Step 1: Intended Takeaway (One Sentence)

- Fix the conclusion of the visual in one sentence

### Step 2: Declutter

- Remove noise (gridlines, legends, color count, digits, unnecessary series, decoration)

### Step 3: Focus

- Direct attention (annotations, ordering, highlights, direct labels)
- Fix the comparison target to make judgment easy

### Step 4: Revised Spec

- Consolidate into revised_visual_spec

## Output Format

Save the output to `outputs/07_chart_edits.json` as **JSON only**:

```json
{
  "chart_edits": [
    {
      "slide_id": "SLxx",
      "intended_takeaway": "...",
      "declutter": ["..."],
      "focus": ["..."],
      "revised_visual_spec": {
        "type": "bar",
        "data_requirements": ["..."],
        "annotations": ["..."]
      }
    }
  ]
}
```

## Quality Checklist

* [ ] Takeaway is one sentence
* [ ] Declutter/focus steps are specific
* [ ] Claims remain unchanged
* [ ] JSON only

## Web Search Guidance

Use web search only when:

1. You lack primary external numbers needed for the chart’s claim
