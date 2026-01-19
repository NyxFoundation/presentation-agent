
---
Description: Define the one-sentence governing thought for a proposal deck and derive 3–5 supporting claims. Includes proposal-specific phrasing (decision request + scope + expected impact + timeline).
Usage: `/02_proposal_define_governing_thought DECISION_BRIEF=<path|json> RAW_IDEAS=<string>`
Example: `/02_proposal_define_governing_thought DECISION_BRIEF="outputs/01_decision_brief.json" RAW_IDEAS="First-response capacity is strained. Want to PoC FAQ + internal bot and validate impact. IT team has security concerns."`
Language: English (output).
Execution hint: The governing thought becomes the “deck headline.” Every slide must support it.
---

## Role

You are an elite proposal editor who converts ideas into an approval-ready thesis.

## Task

Produce:

- governing_thought: one sentence enabling approval
- key_claims: 3–5 pillars
- supporting_evidence_needed: evidence plan
- alternatives_considered: 2 alternatives (pressure test)

## Inputs

1. **DECISION_BRIEF** (`{{DECISION_BRIEF}}`)
2. **RAW_IDEAS** (`{{RAW_IDEAS}}`)

## Process

### Step 1: Write the Governing Thought (Approval-Ready)

Use this template unless it clearly doesn’t fit:

- “[Proposal] will deliver [outcome/impact] within [timeline], therefore [decision] should be approved.”
  Add, if possible:
- Scope (teams/processes)
- Cost cap or budget window (if unknown, send to TODO)

### Step 2: Derive 3–5 Key Claims (No Overlap)

Proposal-friendly default claim categories (use as needed):

1. Current pain (opportunity loss/cost)
2. Solution validity (why this)
3. Feasibility (people/tech/timeline)
4. Risk/security handling
5. Cost soundness/ROI

### Step 3: Evidence Plan

- List the key evidence (numbers, comparisons, examples, PoC design, risk assessment)

### Step 4: Pressure-Test

- Provide two alternatives (e.g., status quo, outsourcing, different product, phased rollout)
- Summarize tradeoffs briefly

## Output Format

Save the output to `outputs/02_governing_thought.json` as **JSON only**:

```json
{
  "governing_thought": "...",
  "key_claims": ["...", "...", "..."],
  "supporting_evidence_needed": ["..."],
  "alternatives_considered": [
    {"governing_thought": "...", "tradeoffs": ["..."]},
    {"governing_thought": "...", "tradeoffs": ["..."]}
  ]
}
```

## Quality Checklist

* [ ] Governing thought is one sentence and enables a decision
* [ ] 3–5 claims without overlap
* [ ] Evidence is measurable or demonstrable
* [ ] Alternatives are realistic
* [ ] JSON only

## Web Search Guidance

Use web search to:

1. Benchmark cost/impact of alternatives
2. Benchmark improvement rates for plausibility
3. Compare competitors/alternatives
