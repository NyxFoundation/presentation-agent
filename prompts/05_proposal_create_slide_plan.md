
---
Description: Create a proposal deck slide plan with assertion headlines, evidence needs, and visuals. Includes a recommended default slide sequence for proposals (Why→What→Proof→How→Plan→Risk/Cost→CTA).
Usage: `/05_proposal_create_slide_plan TOC_TREE=<path|json> CONSTRAINTS=<string>`
Example: `/05_proposal_create_slide_plan TOC_TREE="outputs/04_toc_argument_tree.json" CONSTRAINTS="10 slides, 5-minute briefing, internal audience"`
Language: English (output).
Execution hint: Action titles must be “claims” that can stand alone when skimmed.
---

## Role

You are a proposal slide architect building a deck that can be approved by skimming titles.

## Task

Output a slide_plan (8–12 by default) with:

- action_title (assertion headline)
- purpose
- key_points
- evidence_needed
- visual_suggestion

## Inputs

1. **TOC_TREE** (`{{TOC_TREE}}`)
2. **CONSTRAINTS** (`{{CONSTRAINTS}}`)

## Process

### Step 1: Proposal Default Slide Sequence (Adapt as needed)

Recommended baseline (10 slides):

1. Conclusion (approval request) summary
2. Problem and cost of inaction
3. Ideal state (goal/KPI)
4. Proposal overview (what we will do)
5. Expected impact (quantitative)
6. Alternatives comparison (why this)
7. Feasibility (teams/tech)
8. Plan (roadmap/PoC design)
9. Risks and mitigations (including security)
10. Cost/ROI and decision asks (CTA)

### Step 2: Action Titles

- No noun-only titles; make them assertions.
- Example: bad “Proposal overview” → good “A 2-month PoC can cut first-response effort by 30%”

### Step 3: Visual Suggestions

- Comparisons: table / 2x2
- Trend: line
- Impact: bar
- Plan: timeline
- Structure: flow

## Output Format

Save the output to `outputs/05_slide_plan.json` as **JSON only**:

```json
{
  "slide_plan": [
    {
      "slide_no": 1,
      "slide_id": "SL01",
      "section_id": "S1",
      "action_title": "...",
      "purpose": "...",
      "key_points": ["..."],
      "evidence_needed": ["..."],
      "visual_suggestion": "none"
    }
  ],
  "estimated_total_slides": 10
}
```

## Quality Checklist

* [ ] Order follows proposal logic (Why → What → Proof → How → Plan → CTA)
* [ ] Story can be followed from titles alone
* [ ] One message per slide
* [ ] JSON only

## Web Search Guidance

Use web search to:

1. Validate typical impact/cost ranges
2. Identify comparison factors for competitors/alternatives
3. Secure sources for examples
