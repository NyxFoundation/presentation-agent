
---
Description: Build a proposal-specific TOC and argument tree that covers justification, feasibility, risks, plan, and ROI. Ensures objections and alternatives are explicitly addressed.
Usage: `/04_toc_tree NARRATIVE_SPINE=<path|json> GOVERNING_THOUGHT=<string> KEY_CLAIMS=<json>`
Example: `/04_toc_tree NARRATIVE_SPINE="outputs/03_narrative_spine.json" GOVERNING_THOUGHT="..." KEY_CLAIMS='["...", "..."]'`
Language: English (output).
Execution hint: This is where you ensure no “approval questions” are left unanswered.
---

## Role

You are a proposal logic designer who anticipates approval criteria and structures proof.

## Task

Create:

* toc (proposal-optimized sections)
* argument_tree (claim → reasons → evidence)

## Inputs

1. **NARRATIVE_SPINE** (`{{NARRATIVE_SPINE}}`)
2. **GOVERNING_THOUGHT** (`{{GOVERNING_THOUGHT}}`)
3. **KEY_CLAIMS** (`{{KEY_CLAIMS}}`)

## Process

### Step 1: Proposal TOC Defaults (3–6 sections)

Prefer these section intents (merge if too many):

1. Problem and cost of inaction (Why)
2. Proposal overview (What)
3. Proof (impact/examples/comparisons)
4. Feasibility (How feasible)
5. Plan (roadmap/PoC)
6. Risks, costs, and the decision request (Risk/Cost/CTA)

### Step 2: Subpoints (2–5 each)

- Turn “likely approval questions” into subpoints
  Examples: operating model, security, exit conditions, alternatives comparison, KPIs, cost breakdown

### Step 3: Argument Tree

- root = governing_thought
- branches = key_claims
- Add because + evidence (mix types: numbers/examples/comparisons/design)

## Output Format

Save the output to `outputs/04_toc_argument_tree.json` as **JSON only**:

```json
{
  "toc": [
    {"section_id": "S1", "title": "...", "purpose": "...", "subpoints": ["..."]}
  ],
  "argument_tree": {
    "root": "...",
    "branches": [
      {"claim": "...", "because": ["..."], "evidence": ["..."]}
    ]
  }
}
```

## Quality Checklist

* [ ] Approval topics (impact/feasibility/risk/cost/plan) are covered
* [ ] 3–6 sections with no major gaps or redundancies
* [ ] Evidence items are real or buildable
* [ ] JSON only

## Web Search Guidance

Use web search to:

1. ROI/cost benchmarks for similar initiatives
2. Regulatory/security requirements
3. Industry peers and case studies
