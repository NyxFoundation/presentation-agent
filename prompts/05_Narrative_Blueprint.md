
---
Description: Creates the narrative and structural blueprint of the presentation. This step maps the logical Key Claims onto the chosen Narrative Archetype, creating a slide-by-slide outline with powerful, assertion-driven Action Titles.
Usage: `/05_Narrative_Blueprint GOVERNING_ARGUMENT=<path|json> CORE_STRATEGY=<path|json> CONSTRAINTS=<string>`
Example: `/05_Narrative_Blueprint GOVERNING_ARGUMENT="outputs/04_Governing_Argument.json" CORE_STRATEGY="outputs/03_Core_Strategy.json" CONSTRAINTS="15 slides max"`
Language: English (output).
Execution hint: This is where logic meets story. The output is the architectural plan for the deck. The sequence of Action Titles must tell a compelling story on its own, even without the slide content.
---

## HARD CONSTRAINTS (MUST FOLLOW)

The presentation MUST adhere to the following constraints: **{{CONSTRAINTS}}**.

This is a non-negotiable requirement. The `estimated_slide_count` in your output MUST NOT exceed the maximum slide count specified. Structure your narrative to fit within this limit. If the content is too extensive, prioritize the most impactful claims and combine related points into single slides.

## Role

You are a master presentation architect and storyteller. You excel at weaving a logical argument into a captivating narrative, and you understand that a presentation's structure is the key to its persuasiveness. You are a disciple of both Barbara Minto and Nancy Duarte.

## Task

Using the **GOVERNING_ARGUMENT** and **CORE_STRATEGY**, produce a **Narrative Blueprint** in JSON format. This blueprint will serve as the definitive plan for the slide deck.

## Process

### Step 1: Lay Out the Narrative Arc

- Based on the `selected` narrative archetype from the `CORE_STRATEGY`, lay out the key beats of the story.
- **Example for 'Sparkline' Archetype:**
    1.  **The Hook & The Status Quo**: What is the current, accepted reality?
    2.  **The Problem / The Tension**: What is the pain or inefficiency in that reality?
    3.  **The Vision / The Promised Land**: What could a better future look like?
    4.  **The Bridge / The Solution**: How does our proposal get us from the problem to the vision?
    5.  **The Proof / The Plan**: Why should you believe we can do this? What's the plan?
    6.  **The Call to Action**: What is the one thing we need you to do to make the vision a reality?

### Step 2: Map Key Claims to Narrative Beats

- Allocate the `key_claims` from the `GOVERNING_ARGUMENT` to the most appropriate beats in the narrative arc. A single beat may contain multiple claims, or a single claim may span multiple slides within a beat.
- This step ensures the logical argument is presented within a compelling story structure.

### Step 3: Decompose Beats into Slides with Action Titles

- Break down each narrative beat into one or more slides.
- For each slide, write a powerful **Action Title**. This is the most important part of this step.
- An Action Title is a full, declarative sentence that makes a clear point. It is the headline of the slide.
- **Bad Title (Topic)**: "Our Team"
- **Good Title (Action)**: "We have assembled a world-class team with proven expertise in both AI and blockchain."
- The sequence of Action Titles, when read alone, must form a complete, logical, and persuasive story.

### Step 4: Define Each Slide's Purpose and Evidence Requirement

- For each slide, write a single sentence defining its specific job. (e.g., "Purpose: To establish the financial cost of the current problem.")
- List the specific pieces of evidence (data, facts, quotes) that will be required to prove the Action Title. This is derived from the `evidence_strategy` in the `GOVERNING_ARGUMENT`.

## Output Format

Save the output to `outputs/05_Narrative_Blueprint.json` as **JSON only**:

```json
{
  "narrative_blueprint": {
    "narrative_archetype_used": "Sparkline",
    "estimated_slide_count": 12,
    "slides": [
      {
        "slide_number": 1,
        "slide_id": "SL01",
        "narrative_beat": "The Hook & The Status Quo",
        "action_title": "The world is on the cusp of a new economy driven entirely by AI agents.",
        "purpose": "To establish the context and introduce a major technological shift, creating a sense of importance and scale.",
        "evidence_needed": ["Gartner/Forrester quote on AI autonomy", "Analyst projection on AI-driven transaction volume"]
      },
      {
        "slide_number": 2,
        "slide_id": "SL02",
        "narrative_beat": "The Problem / The Tension",
        "action_title": "However, the rules and institutions that will govern this new economy are completely unknown, creating massive uncertainty and risk.",
        "purpose": "To introduce the core problem and create a sense of intellectual tension and urgency.",
        "evidence_needed": ["List of unanswered questions about AI economic governance", "Example of potential negative emergent behavior"]
      },
      {
        "slide_number": 3,
        "slide_id": "SL03",
        "narrative_beat": "The Vision / The Promised Land",
        "action_title": "We have the opportunity to be the architects of this new world, shaping its foundations for decades to come.",
        "purpose": "To present a bold, inspiring vision that positions the audience as pioneers.",
        "evidence_needed": ["Visionary quote about shaping the future", "Image representing a complex, thriving digital economy"]
      }
    ]
  }
}
```

## Quality Checklist

- [ ] Does the sequence of `action_titles` tell a complete and persuasive story from start to finish?
- [ ] Is every `action_title` a full, assertive sentence?
- [ ] Is each slide's `purpose` clear and aligned with the overall narrative?
- [ ] Is the `evidence_needed` for each slide specific and directly supportive of its Action Title?
- [ ] **Does the `estimated_slide_count` strictly adhere to the `CONSTRAINTS` specified at the top of this prompt? This is a HARD requirement.**
- [ ] Is the output valid JSON?

## Web Search Guidance

Use web search to:

1.  Find powerful, attention-grabbing statistics or quotes for the opening "Hook" slide.
2.  Research examples of strong Action Titles from top consulting firms or keynote presentations to refine your own.
3.  Verify that the evidence you are planning to use is credible and find potential sources for it.
