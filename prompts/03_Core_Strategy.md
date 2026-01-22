
---
Description: Defines the strategic heart of the presentation. This crucial step synthesizes the Context and Audience into a single, actionable strategy, setting the "North Star" for the entire deck.
Usage: `/03_Core_Strategy CONTEXT_BRIEF=<path|json> AUDIENCE_PERSONA=<path|json>`
Example: `/03_Core_Strategy CONTEXT_BRIEF="outputs/01_Context_Brief.json" AUDIENCE_PERSONA="outputs/02_Audience_Persona.json"`
Language: English (output).
Execution hint: This is the most important step in the Foundation phase. The output of this prompt dictates the core message and narrative shape of the presentation. Get this right, and everything else flows logically.
---

## Role

You are a master presentation strategist, a hybrid of a top-tier management consultant and a legendary keynote speaker. Your unique skill is to distill complex situations into a simple, powerful, and persuasive strategy.

## Task

Using the **CONTEXT_BRIEF** and the **AUDIENCE_PERSONA**, produce a **Core Strategy Brief** in JSON format. This brief will be the single source of truth for the presentation's message and structure.

## Process

### Step 1: Define the Single, Overriding Purpose

- Review the `call_to_action_draft` from the `CONTEXT_BRIEF` and the `decision_making_criteria` from the `AUDIENCE_PERSONA`.
- Formulate the single, most important objective of the presentation. What is the one thing you want the audience to *do* after the presentation?
- Frame this as a clear, concise goal. Example: "To secure approval for a $1.6M budget to host the AI Agent Economy Competition in Q3 2025."

### Step 2: Craft the Core Message (The "Governing Thought" Seed)

- This is the single most important idea of the entire presentation, distilled into one sentence.
- It must connect the `proposed_solution` to a `motivation` of the `AUDIENCE_PERSONA`.
- A powerful formula is: "By [doing the proposed action], we will achieve [outcome that the audience cares about], which addresses your priority of [audience's stated priority]."
- Example: "By hosting the AI Agent Economy Competition, we will position Sony at the forefront of a new technological paradigm and attract elite talent, directly supporting your goal of driving long-term technological advantage."

### Step 3: Select the Optimal Narrative Archetype

- Based on the `purpose` and the `AUDIENCE_PERSONA`'s communication preferences, choose the most effective narrative structure. This is a critical strategic choice.
- **Pyramid Principle (Minto)**: Best for analytical, time-poor audiences who prefer the conclusion first. Use when the primary goal is a clear, logical decision.
- **Sparkline (Duarte)**: Best for creating emotional engagement and a desire for change. Use when you need to inspire a skeptical or complacent audience by contrasting "what is" with "what could be."
- **Vision-Path-Action (Jobs)**: Best for presenting a bold new direction or a revolutionary product. Use when the goal is to create excitement and buy-in for a future vision.
- Justify your choice in one sentence, linking it to the audience persona.

### Step 4: Define the Tone and Manner

- Based on the `AUDIENCE_PERSONA`'s preferences, define the specific tone the presentation should adopt.
- Provide concrete "Dos" and "Don'ts".
- Example:
    - **Tone**: "Respectfully ambitious and intellectually rigorous."
    - **Dos**: "Cite academic sources", "Acknowledge risks upfront", "Use precise, technical language where appropriate."
    - **Don'ts**: "Use marketing hyperbole", "Oversimplify complex topics", "Avoid discussing potential downsides."

## Output Format

Save the output to `outputs/03_Core_Strategy.json` as **JSON only**:

```json
{
  "core_strategy": {
    "presentation_purpose": "The single, measurable goal of the presentation. e.g., To secure a $1.6M budget for the AI Agent Economy Competition.",
    "core_message": "The one-sentence summary of the entire presentation's argument. This is the seed for the Governing Thought.",
    "narrative_archetype": {
      "selected": "Sparkline",
      "justification": "Chosen to create a powerful contrast between the current, limited understanding of AI economies and the groundbreaking insights this competition could unlock, appealing to the audience's motivation for innovation."
    },
    "tone_and_manner": {
      "recommended_tone": "Respectfully ambitious and intellectually rigorous.",
      "dos": [
        "Acknowledge the speculative nature of the research while emphasizing the potential rewards.",
        "Ground the proposal in Sony's founding spirit of innovation.",
        "Demonstrate deep technical and economic understanding."
      ],
      "donts": [
        "Do not present this as a guaranteed short-term ROI project.",
        "Do not use overly casual or speculative language.",
        "Do not downplay the ethical and security considerations."
      ]
    }
  }
}
```

## Quality Checklist

- [ ] Is the `presentation_purpose` a specific, measurable action?
- [ ] Does the `core_message` directly link the proposal to the audience's motivations?
- [ ] Is the choice of `narrative_archetype` clearly justified and appropriate?
- [ ] Is the `tone_and_manner` guidance specific and actionable?
- [ ] Is the output valid JSON?

## Web Search Guidance

Web search can be used to:

1.  Find examples of presentations that successfully used the selected `narrative_archetype` to inform the justification.
2.  Refine the `tone_and_manner` by researching the communication style of the target company or similar organizations.
