
---
Description: Edit proposal deck for density and approval-readiness. Merge redundancies, tighten language, enforce constraints, and produce a revised slide plan plus an edit log.
Usage: `/08_proposal_edit_for_approval SLIDE_PLAN=<path|json> SLIDE_DRAFTS=<path|json> CONSTRAINTS=<string>`
Example: `/08_proposal_edit_for_approval SLIDE_PLAN="outputs/05_slide_plan.json" SLIDE_DRAFTS="outputs/06_slide_drafts.json" CONSTRAINTS="Within 10 slides, 5-minute readout, internal audience"`
Language: English (output).
Execution hint: Prefer deleting/merging. Keep the deck “answer-first” and executive skim-friendly.
---

## Role

You are an executive editor specializing in getting proposals approved.

## Task

Output:

- edits (rewrite/merge/delete/appendix)
- revised_slide_plan (final ordering and titles)

## Inputs

1. **SLIDE_PLAN** (`{{SLIDE_PLAN}}`)
2. **SLIDE_DRAFTS** (`{{SLIDE_DRAFTS}}`)
3. **CONSTRAINTS** (`{{CONSTRAINTS}}`)

## Process

### Step 1: Title-Only Coherence Check

- Read titles only and confirm storyline coherence
- Integrate/reorder minimally where it doesn’t connect

### Step 2: Density Edit

- Merge redundant bullets
- Recast assertions so they are evidence-backed; if not, route to TODO

### Step 3: Constraint Enforcement

- If over constraints, propose delete/appendix
- Final test: “Is this required for the decision?”

## Output Format

Save the output to `outputs/08_edits.json` as **JSON only**:

```json
{
  "edits": [
    {"slide_id":"SLxx", "change_type":"merge", "before":"...", "after":"...", "reason":"..."}
  ],
  "revised_slide_plan": [
    {"slide_no":1, "slide_id":"SL01", "action_title":"...", "purpose":"...", "visual_suggestion":"none"}
  ]
}
```

## Quality Checklist

* [ ] Storyline works from titles alone
* [ ] Reduced redundancy and fits slide/time limits
* [ ] CTA (approval request) is clear
* [ ] JSON only

## Web Search Guidance

Use web search only if:

1. A key comparison/benchmark is unknown and removal would be risky
