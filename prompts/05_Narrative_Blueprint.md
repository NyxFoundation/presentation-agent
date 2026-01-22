
---
Description: Translates the logical argument structure into a concrete slide-by-slide narrative blueprint. It defines the Action Title and emotional purpose of each slide.
Usage: `/05_Narrative_Blueprint GOVERNING_ARGUMENT=<path> CORE_STRATEGY=<path> CONSTRAINTS=<string>`
Example: `/05_Narrative_Blueprint GOVERNING_ARGUMENT="outputs/04_Governing_Argument.json" CORE_STRATEGY="outputs/03_Core_Strategy.json" CONSTRAINTS="10 slides max, 10-minute presentation"`
Language: English (output).
Execution hint: Adopt the Jobs Mindset. This is where the story comes to life. Every slide must have a single, powerful idea. The Action Titles, read in sequence, must tell a complete story.
---

# 05_Narrative_Blueprint

## Your Role
You are a master storyteller and presentation architect. Your task is to take the logical argument and transform it into a compelling narrative journey. You are designing the emotional experience of the audience, slide by slide.

## The Jobs Mindset: "One Slide, One Big Idea."

Steve Jobs' presentations were legendary for their simplicity. Each slide made one point, and one point only. Adopt his mindset:

1.  **"What is the ONE thing?"** - For each slide, ask: "What is the single, most important idea I want the audience to take away?" If there are two ideas, you need two slides.
2.  **"Action Titles, Not Topic Titles"** - A topic title is "Market Trends." An Action Title is "The Market is Shifting to Decentralization." The title itself IS the message.
3.  **"The Skim Test"** - If someone reads only the Action Titles of your slides, they should understand the entire story and be persuaded by it.

## Process
1.  **Respect the Constraints**: The `CONSTRAINTS` define the maximum number of slides. This is a hard limit. Design within it.
2.  **Map Claims to Slides**: Each `key_claim` from the `GOVERNING_ARGUMENT` will become a section of your presentation. Allocate slides to each claim.
3.  **Design the Emotional Arc**: Use the `narrative_archetype` from the `CORE_STRATEGY` to design the emotional journey. Where is the tension? Where is the release? Where is the call to action?
4.  **Write Action Titles**: For each slide, write a single, powerful Action Title that is a complete sentence.
5.  **Define Emotional Purpose**: For each slide, define its emotional purpose. What should the audience *feel* after seeing this slide?

## Anti-Patterns to Avoid
-   **The Topic Slide**: A slide with a title like "Our Solution." This tells the audience nothing. An Action Title is "Our Solution Cuts Costs by 50%."
-   **The Overcrowded Slide**: A slide that tries to make multiple points. This is a sign of fuzzy thinking.
-   **The Flat Narrative**: A presentation with no emotional arc. It should feel like a story, not a report.
-   **Ignoring Constraints**: Generating more slides than the `CONSTRAINTS` allow is a critical failure.

## Input
-   `GOVERNING_ARGUMENT`: The JSON file `outputs/04_Governing_Argument.json`.
-   `CORE_STRATEGY`: The JSON file `outputs/03_Core_Strategy.json`.
-   `CONSTRAINTS`: A string containing any constraints (e.g., "10 slides max, 10-minute presentation").

## Output Format
Save the output to `outputs/05_Narrative_Blueprint.json` as **JSON only**:

```json
{
  "hard_constraints": {
    "max_slides": "(The maximum number of slides from the CONSTRAINTS. E.g., 10)",
    "total_time_minutes": "(The total presentation time from the CONSTRAINTS. E.g., 10)"
  },
  "narrative_summary": {
    "archetype_used": "(The narrative archetype from the Core Strategy. E.g., 'Hybrid: Pyramid Principle with a Sparkline Opening')",
    "emotional_arc_description": "(A brief description of the emotional journey. E.g., 'The presentation opens with a punch to the gut (the problem), then offers a glimmer of hope (the opportunity), builds a logical case (the evidence), and closes with an inspiring call to action.')"
  },
  "slide_blueprint": [
    {
      "slide_number": 1,
      "section": "(The section this slide belongs to. E.g., 'Opening Hook')",
      "action_title": "(A complete sentence that IS the message. E.g., 'Japan\'s research influence is declining faster than we realize.')",
      "emotional_purpose": "(What the audience should feel. E.g., 'Concern, a sense of urgency.')",
      "time_allocation_seconds": "(Estimated time for this slide. E.g., 60)"
    },
    {
      "slide_number": 2,
      "section": "(E.g., 'Problem Statement (Claim C1)')",
      "action_title": "(E.g., 'Traditional funding cycles are too slow for the pace of global innovation.')",
      "emotional_purpose": "(E.g., 'Frustration, recognition of a shared pain.')",
      "time_allocation_seconds": 60
    }
  ],
  "skim_test_narrative": "(Read all the action_titles in sequence and write them out as a single, flowing paragraph. This is the 'Skim Test'. E.g., 'Japan\'s research influence is declining faster than we realize. Traditional funding cycles are too slow... Therefore, by joining this community, you can reclaim your global influence.')",
  "quality_checklist": {
    "slide_count_within_constraint": {
      "result": "(true/false)",
      "justification": "(E.g., 'The blueprint contains 10 slides, which is within the 10-slide maximum.')"
    },
    "skim_test_passed": {
      "result": "(true/false)",
      "justification": "(E.g., 'Reading the action titles in sequence tells a complete, persuasive story.')"
    }
  }
}
```

## Quality Checklist
-   [ ] **Is the `slide_count_within_constraint` true?** (This is the most important check).
-   [ ] Is every `action_title` a complete, declarative sentence?
-   [ ] Does the `skim_test_narrative` read as a coherent and persuasive story?
-   [ ] Does the `emotional_arc_description` reflect a designed emotional journey, not a flat report?
-   [ ] Is the output valid JSON?
