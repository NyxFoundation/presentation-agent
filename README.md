# Presentation Agent

A Claude-driven pipeline that turns a single Markdown brief into a
production-quality [Slidev](https://sli.dev/) deck — combining the
logical rigor of consulting firms (McKinsey, BCG) with the narrative
craft of presenters like Steve Jobs and Nancy Duarte.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Overview

You write a target audience, constraints, and raw content in
`inputs/introduction.md`. The pipeline runs nine prompts through the
`claude` CLI to build a persona, design the argument structure, draft
each slide, and emit Slidev-ready Markdown — with intermediate JSON at
every step so you can inspect (and override) any stage.

## Design Philosophy

This pipeline is built on three core principles:

1. **Strategy-First:** Before creating content, thoroughly define "why you're speaking," "who you're speaking to," and "what you want to convey."
2. **Logic & Emotion:** Clearly separate logical structures based on the Pyramid Principle from narrative structures like Sparkline, then intentionally combine them.
3. **Iterative Refinement:** Progressively move from abstract ideas to concrete deliverables, improving quality at each stage.

## Quick Start

### 1. Prepare the Input File

Write the YAML frontmatter and presentation content in `inputs/introduction.md`.

```markdown
---
target_audience: "Tech Conference 2026 Attendees (Software Engineers)"
audience_type: group
constraints:
  max_slides: 15
  max_duration_minutes: 15
output_language: English
event:
  name: "Tech Conference Tokyo"
---

# Presentation Title

Write your content here...
```

### 2. Run the Pipeline

```bash
make all
```

### 3. View the Output

```bash
# Preview with Slidev
bun i
bun dev
# Access http://localhost:3030
```

## Input Format

All settings are defined in the YAML frontmatter of `inputs/introduction.md`.

### Required Fields

| Field | Description | Example |
|-------|-------------|---------|
| `target_audience` | Target audience | `"John Doe (Example Corp)"` or `"Conference Attendees"` |
| `audience_type` | Type of audience | `individual` / `group` / `mixed` |
| `constraints.max_slides` | Maximum number of slides | `15` |
| `constraints.max_duration_minutes` | Maximum presentation duration (minutes) | `15` |
| `output_language` | Output language | `Japanese` / `English` |

### Optional Fields

| Field | Description | Example |
|-------|-------------|---------|
| `event.name` | Event name | `"Tech Conference Tokyo"` |
| `event.parent_event` | Parent event | `"Tech Summit 2026"` |
| `event.date` | Date | `"2026-01-XX"` |
| `event.location` | Location | `"Tokyo"` |

### audience_type Usage

| Type | Use Case | Example |
|------|----------|---------|
| `individual` | Pitch to a specific individual | Proposal to an executive |
| `group` | Group with shared characteristics | Conference presentation |
| `mixed` | Multiple specific individuals | Committee presentation |

### Input Examples

#### Individual (Executive Pitch)

```yaml
---
target_audience: "John Doe (Example Inc. Chairman, Example Global Education)"
audience_type: individual
constraints:
  max_slides: 10
  max_duration_minutes: 20
output_language: English
---
```

#### Group (Conference Talk)

```yaml
---
target_audience: "Tech Conference 2026 Attendees (Software Engineers)"
audience_type: group
constraints:
  max_slides: 15
  max_duration_minutes: 15
output_language: English
event:
  name: "Tech Conference Tokyo"
  parent_event: "Tech Summit 2026"
---
```

#### Mixed (Committee Presentation)

```yaml
---
target_audience: "Jane Smith (University A), Bob Johnson (University B), Alice Brown (University C)"
audience_type: mixed
constraints:
  max_slides: 20
  max_duration_minutes: 30
output_language: English
---
```

## Pipeline Architecture

The pipeline consists of 4 phases and 9 steps.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          PHASE 1: FOUNDATION                                │
│                      (Strategy & Understanding)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────┐    ┌───────────────┐    ┌───────────────┐              │
│  │ 01. Context   │───▶│ 02. Audience  │───▶│ 03. Core      │              │
│  │    Analysis   │    │    Persona    │    │    Strategy   │              │
│  └───────────────┘    └───────────────┘    └───────────────┘              │
│   YAML frontmatter      Build Persona        Define Strategy               │
│   + Content Analysis    (from Context Brief)                               │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PHASE 2: ARCHITECTURE                               │
│                      (Structure & Argumentation)                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────┐    ┌───────────────────────┐                    │
│  │ 04. Governing         │───▶│ 05. Narrative         │                    │
│  │     Argument          │    │     Blueprint         │                    │
│  │ (Pyramid Principle)   │    │ (Action Titles)       │                    │
│  └───────────────────────┘    └───────────────────────┘                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHASE 3: CONTENT                                  │
│                      (Content & Visuals)                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────┐    ┌───────────────────────┐                    │
│  │ 06. Slide             │───▶│ 07. Visual            │                    │
│  │     Drafting          │    │     Design            │                    │
│  │ (Bullets & Notes)     │    │ (Charts & Diagrams)   │                    │
│  └───────────────────────┘    └───────────────────────┘                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PHASE 4: POLISH & EXPORT                             │
│                      (Review & Export)                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────┐    ┌───────────────────────┐                    │
│  │ 08. Executive         │───▶│ 09. Final             │                    │
│  │     Review            │    │     Export            │                    │
│  │ (Murder Board)        │    │ (Slidev Markdown)     │                    │
│  └───────────────────────┘    └───────────────────────┘                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Step Details

| Step | Name | Description | Key Output |
|------|------|-------------|------------|
| 01 | Context Analysis | Extract metadata from YAML frontmatter and structure content | `01_Context_Brief.json` |
| 02 | Audience Persona | Read target from Context Brief and build persona | `02_Audience_Persona.json` |
| 03 | Core Strategy | Define presentation purpose, core message, and narrative structure | `03_Core_Strategy.json` |
| 04 | Governing Argument | Build logical structure based on the Pyramid Principle | `04_Governing_Argument.json` |
| 05 | Narrative Blueprint | Design Action Titles for each slide | `05_Narrative_Blueprint.json` |
| 06 | Slide Drafting | Create bullet points and speaker notes for each slide | `06_Slide_Drafts.json` |
| 07 | Visual Design | Design visuals (charts, diagrams) for each slide | `07_Visual_Designs.json` |
| 08 | Executive Review | Conduct final review from decision-maker's perspective | `08_Executive_Review.json` |
| 09 | Final Export | Apply review feedback and export in Slidev format | `09_Final_Export.json` |

## Thinking Frameworks

Each prompt is designed as a "thinking framework" rather than mere rules.

### Jobs Mindset (02_Audience_Persona)
> "What keeps them up at night?"
>
> Understand the audience's deep psychology (fears, desires, biases), not just surface attributes.

### Bezos Mindset (01_Context_Analysis, 06_Slide_Drafting)
> "Speaker Notes First"
>
> Write speaker notes in complete sentences before writing slide bullet points.

### McKinsey Mindset (04_Governing_Argument, 05_Narrative_Blueprint)
> "So What?" / "Why So?" Test
>
> Verify that every claim can answer "So what?" and "Why is that true?"

## Quality Assurance Features

### Consistency Check (01_Context_Analysis)

Automatically validates alignment between content and target audience.

```json
{
  "consistency_check": {
    "content_matches_declared_audience": true,
    "inferred_audience_from_content": "Conference Attendees",
    "notes": "Content and declared audience are aligned."
  }
}
```

When inconsistency is detected:

```json
{
  "consistency_check": {
    "content_matches_declared_audience": false,
    "inferred_audience_from_content": "Research Community",
    "notes": "WARNING: Content appears to target researchers, but declared target is corporate executive."
  }
}
```

### Source Fidelity Check (08_Executive_Review)

Verifies that important elements from the original input (founder stories, anecdotes) are preserved in the final output.

### Evidence Quality Hierarchy (06_Slide_Drafting)

Prioritizes evidence quality in a clear hierarchy:

1. **Hard Data**: Numbers, statistics, verifiable facts
2. **Expert Opinion**: Views from authoritative experts
3. **Analogies**: Inferences from similar cases
4. **Anecdotes**: Individual stories and examples

## Directory Structure

```
.
├── Makefile                    # Pipeline orchestrator
├── README.md                   # This file
├── prompts/                    # Prompt files
│   ├── 01_Context_Analysis.md
│   ├── 02_Audience_Persona.md
│   ├── 03_Core_Strategy.md
│   ├── 04_Governing_Argument.md
│   ├── 05_Narrative_Blueprint.md
│   ├── 06_Slide_Drafting.md
│   ├── 07_Visual_Design.md
│   ├── 08_Executive_Review.md
│   └── 09_Final_Export.md
├── inputs/                     # User input (single file)
│   └── introduction.md         # YAML frontmatter + content
├── outputs/                    # Generated intermediate files
│   ├── 01_Context_Brief.json
│   ├── ...
│   └── logs/                   # Claude CLI logs
└── slides/                     # Final Slidev files
```

## Make Commands

```bash
# Run all steps
make all

# Validate input file only
make validate

# Run individual steps
make context_analysis
make audience_persona
make core_strategy
make governing_argument
make narrative_blueprint
make slide_drafting
make visual_design
make executive_review
make final_export

# Clear outputs
make clean

# Show help
make help
```

## Running Slidev

```bash
# Install dependencies
bun i

# Start development server
bun dev
```

Access http://localhost:3030

## Contributing

PRs and issues are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the
local development workflow, branch conventions, and PR expectations.

## Maintainer Setup

One-time configuration the repository owner must perform on Cloudflare and
GitHub for the branch model described in [Contributing](#contributing) to
actually be enforced. Without these, the conventions are documentation only.

### 1. Cloudflare — branch deployment scope

Deployment is via Cloudflare Workers Builds (Git integration). The
dashboard offers a binary toggle for non-production branch builds, which
combined with the GitHub ruleset in §2 is sufficient:

- **Production branch:** `main`
- **Non-production branch builds:** keep ON. Once §2 is active and any
  stale branches have been cleaned up, the only non-prod branches that
  can exist in upstream are `presentation/*`, so this deploys exactly
  the right set.

Note: fork PRs do not push to upstream branches (they live in
`refs/pull/N/head`), so they cannot trigger Cloudflare auto-deploys.

### 2. GitHub — restrict branch creation in upstream

**Settings → Rules → Rulesets → New branch ruleset.**

- **Target:** `~ALL` (all branches)
- **Enforcement:** Active
- **Rules:** **"Restrict creations"**, **"Restrict updates"**,
  **"Restrict deletions"**
- **Bypass list:** `OrganizationAdmin` (maintainers do all branch creation
  manually, including pushing `presentation/*` decks they want to publish)

Result: only maintainers can create, update, or delete branches in upstream.
Fork PRs from contributors don't create upstream branches at all (they live
in `refs/pull/N/head`), so the deployment namespace stays clean by design.

### 3. Sanity check before going public

- [ ] Cloudflare branch deployment scope verified — only `main` and any
      existing `presentation/*` branches are deploying
- [ ] Branch ruleset is **Active**, with `OrganizationAdmin` in bypass
- [ ] `outputs/` and `slides/` are not tracked on `main`
      (`git ls-files outputs/ slides/` returns empty)
- [ ] Stale non-`presentation/*` branches in upstream have been triaged
      (deleted or renamed under `presentation/`)

## References

The prompt design draws on the following thinkers and frameworks:

- **McKinsey / BCG**: Pyramid Principle, Action Titles, So What? / Why So? Test
- **Barbara Minto**: "The Pyramid Principle"
- **Nancy Duarte**: Sparkline, "What Is vs. What Could Be"
- **Steve Jobs**: Simplicity, Visual Priority, Storytelling
- **Jeff Bezos**: 6-Page Memo, Narrative Structure, Speaker Notes First
- **Gene Zelazny**: Data Visualization Principles, 1 Chart 1 Message

## Acknowledgements

- [Slidev](https://sli.dev/) for the slide rendering engine.
- [Claude Code](https://claude.com/claude-code) and the `claude` CLI for
  executing the prompts.
- All the contributors who file issues and PRs against this project.

## License

Released under the [MIT License](LICENSE).
