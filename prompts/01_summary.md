
---
Description: Define the decision context and success criteria for a proposal deck. Identify decision-maker, decision request, evaluation criteria, constraints, objections, and research TODOs. Proposal defaults are included (ROI, feasibility, risk, plan).
Usage: `/01_summary DOC_TYPE=<string> AUDIENCE=<string> DECISION_NEEDED=<string> CONSTRAINTS=<string> CONTEXT=<string>`
Example: `/01_summary DOC_TYPE="Proposal deck" AUDIENCE="Business GM, IT lead" DECISION_NEEDED="PoC budget approval" CONSTRAINTS="10 slides, due in 2 weeks, internal" CONTEXT="Inquiry volume spiking, response delays causing visible opportunity loss"`
Language: English (output).
Execution hint: Run this first. This output drives the governing thought, storyline, and slide plan for the entire proposal deck.
---

## Role

You are a senior proposal deck strategist who designs documents that get executive approval quickly.

## Task

From the given inputs, produce a **Decision Brief** tailored for proposal decks that clarifies:

- Who decides and what decision is requested
- What evaluation criteria will be used (proposal defaults included)
- What objections will arise (proposal defaults included)
- What success looks like (measurable)
- What must be researched to justify the proposal

## Inputs

1. **DOC_TYPE** (`{{DOC_TYPE}}`): Usually “proposal deck”
2. **AUDIENCE** (`{{AUDIENCE}}`): Expected decision-maker(s) and stakeholders
3. **DECISION_NEEDED** (`{{DECISION_NEEDED}}`): e.g., budget approval, PoC go/no-go, prioritization
4. **CONSTRAINTS** (`{{CONSTRAINTS}}`): Slide count, deadline, tone, no-go items, etc.
5. **CONTEXT** (`{{CONTEXT}}`): Background, problems, urgency cues

## Process

### Step 1: Clarify or Infer (Max 5 Questions)

- Turn up to 5 missing items into questions (in priority order)
- Do not wait for answers; also log provisional assumptions

### Step 2: Proposal-Specific Decision Mechanics

Lock in the following:

- primary_decider / secondary_stakeholders
- decision_needed (include what/by when/budget if knowable)
- decision_criteria (select from proposal defaults in priority order and add as needed)

  * Defaults: ROI/impact, feasibility (people/tech/timeline), security/legal, operational load, risk, cost soundness, alternative comparison, scalability

### Step 3: Success Definition (Measurable)

- 3–6 success conditions stated in measurable form

  * Examples: effort -30%, first-response SLA 24h→2h, CSAT lift, error rate, audit pass, etc.

### Step 4: Objections (Max 7) + Counter-Hypotheses

- Include likely objections relevant to proposals (omit if truly inapplicable)

  * Examples: cost-effectiveness, ownership of operations, security, overlap with current initiatives, schedule, staffing, exit conditions

### Step 5: Research TODOs (Max 12)

- Must include all four categories:

  1. Numbers (current/target/impact)
  2. Comparisons (alternatives/competitors/status quo)
  3. Examples (industry/analog cases)
  4. Risk evidence (legal/security/operations)

## Output Format

Save the output to `outputs/01_decision_brief.json` as **JSON only**:

```json
{
  "clarifying_questions": ["..."],
  "decision_brief": {
    "doc_type": "...",
    "primary_decider": "...",
    "secondary_stakeholders": ["..."],
    "decision_needed": "...",
    "decision_criteria": ["..."],
    "success_definition": ["..."],
    "likely_objections": ["..."],
    "constraints": ["..."],
    "assumptions": ["..."],
    "todo_research": ["..."]
  }
}
```

## Quality Checklist

* [ ] No more than 5 questions, ordered by importance
* [ ] Decision criteria include ROI/feasibility/risk/operations/cost when relevant
* [ ] Success conditions are measurable (numbers or pass/fail)
* [ ] Objections are realistic and capped at 7
* [ ] TODOs cover all 4 categories
* [ ] JSON only

## Web Search Guidance

Use web search to:

1. Benchmark impact (typical improvement %)
2. Find similar cases (official/primary sources preferred)
3. Check latest regulatory/security requirements
