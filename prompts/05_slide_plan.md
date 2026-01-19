
---
Description: Create a proposal deck slide plan with assertion headlines, evidence needs, and visuals. Includes a recommended default slide sequence for proposals (Why→What→Proof→How→Plan→Risk/Cost→CTA).
Usage: `/05_slide_plan TOC_TREE=<path|json> CONSTRAINTS=<string>`
Example: `/05_slide_plan TOC_TREE="outputs/04_toc_argument_tree.json" CONSTRAINTS="10 slides, 5-minute briefing, internal audience"`
Language: English (output).
Execution hint: Action titles must be “claims” that can stand alone when skimmed. Favor charts/tables/diagrams over dense bullets; each slide should have a concrete visual suggestion that can be rendered in Slidev.
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

### Step 0: Audience/Context Guardrails

- If `outputs/00_audience.json` exists, align slide purposes with that audience’s decision criteria, objections, and tone (e.g., learner-centered, governance-heavy for education leaders).
- Lead with mission/education outcomes and governance/guardrails before tech or market sizing when the audience is education- or trust-focused.
- Avoid hype-y market stats unless they directly support the decision; prefer education impact, operational feasibility, and safety/gov proof needs.
- Reserve space for data governance, human-in-the-loop boundaries, and “what is out of scope” if AI/agent/blockchain are involved.

### Step 1: Proposal Default Slide Sequence (Adapt as needed)

Recommended baseline (10 slides):

1. Conclusion (approval request) summary
2. Problem and cost of inaction (tie to target learners/users, not tech hype)
3. Mission/education fit & credibility (who we are, why us for this audience)
4. Proposal overview (what we will do; clarify if “research sandbox” vs “competition”)
5. Expected impact (education/learning/gov metrics first; market only if relevant)
6. Alternatives comparison (status quo, simulations, corporate sandboxes)
7. Feasibility (teams/ops/governance, human roles vs automation)
8. Plan (roadmap/PoC/competition timeline with exit gates)
9. Risks and mitigations (safety, data governance, legal/brand; what is out of scope)
10. Cost/ROI and decision asks (CTA; include low-commit options if relevant)

### Step 2: Action Titles

- No noun-only titles; make them assertions.
- Example: bad “Proposal overview” → good “A 2-month PoC can cut first-response effort by 30%”

### Step 3: Visual Suggestions

- Always propose a primary visual per slide (table, chart, diagram); avoid “none” unless absolutely unavoidable.
- Comparisons: table / 2x2
- Trend: line
- Impact: bar
- Plan: timeline
- Structure/process: flow / swimlane
- Organization profile: badge/summary card

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
* [ ] Story can be followed from titles alone and reflects audience priorities
* [ ] Education/mission impact and governance/guardrails are explicit if AI/agent/data are involved
* [ ] One message per slide
* [ ] JSON only

## Web Search Guidance

Use web search to:

1. Validate typical impact/cost ranges
2. Identify comparison factors for competitors/alternatives
3. Secure sources for examples
