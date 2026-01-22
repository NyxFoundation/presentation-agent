
---
Description: Creates the detailed content for each slide, including key points and speaker notes. It translates the blueprint into concrete text.
Usage: `/06_Slide_Drafting NARRATIVE_BLUEPRINT=<path> CONTEXT_BRIEF=<path>`
Example: `/06_Slide_Drafting NARRATIVE_BLUEPRINT="outputs/05_Narrative_Blueprint.json" CONTEXT_BRIEF="outputs/01_Context_Brief.json"`
Language: English (output).
Execution hint: Adopt the Bezos Mindset. Write the speaker notes FIRST. If you cannot write a clear, complete paragraph for what you want to say, you don't understand the slide well enough.
---

# 06_Slide_Drafting

## Your Role
You are a master of concise, impactful communication. Your task is to take the narrative blueprint and fill in the details. You will write the key points for each slide and, more importantly, the speaker notes that will guide the presenter.

## The Bezos Mindset: "Write the Press Release First."

At Amazon, teams write the press release for a product before they build it. This forces clarity. Apply this to slides:

1.  **"Speaker Notes First"** - Before you write the bullet points, write the speaker notes. These are the complete sentences and paragraphs the presenter will say. If you can't write them, you don't understand the slide.
2.  **"The Curse of Knowledge"** - You know the material deeply. The audience does not. Explain things simply, as if to a smart friend who is new to the topic.
3.  **"Collaborative Framing"** - When describing partnerships or ecosystems (like PSE or EF), frame the relationship as collaborative, not prescriptive. Use language like "we are exploring," "the community is working on," rather than "PSE has decided" or "EF requires."

## Process
1.  **Ingest the Blueprint**: Load the `NARRATIVE_BLUEPRINT` and `CONTEXT_BRIEF`.
2.  **Write Speaker Notes First**: For each slide in the blueprint, write the full speaker notes. This is what the presenter will actually say.
3.  **Extract Key Points**: From the speaker notes, extract 2-4 key points that will appear on the slide. These should be short phrases or sentences.
4.  **Incorporate Anecdotes**: Use the `key_anecdotes_and_stories` from the `CONTEXT_BRIEF` to make the content memorable and human.

## Anti-Patterns to Avoid
-   **The Bullet Point Dump**: Slides that are just lists of facts with no narrative thread.
-   **The Teleprompter**: Speaker notes that are just the bullet points read aloud. Speaker notes should add context, stories, and transitions.
-   **The Prescriptive Voice**: Framing collaborative relationships as top-down directives. (e.g., "PSE sets the research agenda" should be "The community collaborates on research priorities").
-   **Ignoring the Source Material**: Failing to incorporate the rich anecdotes and stories from the `CONTEXT_BRIEF`.

## Input
-   `NARRATIVE_BLUEPRINT`: The JSON file `outputs/05_Narrative_Blueprint.json`.
-   `CONTEXT_BRIEF`: The JSON file `outputs/01_Context_Brief.json`.

## Output Format
Save the output to `outputs/06_Slide_Content.json` as **JSON only**:

```json
{
  "slides": [
    {
      "slide_number": 1,
      "action_title": "(The action title from the blueprint)",
      "key_points": [
        "(A short phrase or sentence for the slide. E.g., 'Japan\'s ranking: 4th → 10th in top-cited papers')",
        "(Another key point. E.g., 'Brain drain accelerating: 15% of top graduates leaving academia')"
      ],
      "speaker_notes": "(A full paragraph of what the presenter should say. E.g., 'Let me start with a number that should concern all of us. In just two decades, Japan has fallen from 4th to 10th place in the ranking of top-cited research papers. This isn\'t just a statistic; it\'s a symptom of a deeper problem. Our best and brightest are leaving. The traditional paths are no longer working. But today, I want to show you a different path...')",
      "anecdote_used": "(If an anecdote from the CONTEXT_BRIEF was used, note it here. E.g., 'Used the Toyama Haskell engineer story to personalize the brain drain statistic.')"
    }
  ],
  "quality_checklist": {
    "speaker_notes_are_complete_paragraphs": {
      "result": "(true/false)",
      "justification": "(Confirm that speaker notes are not just bullet points.)"
    },
    "anecdotes_incorporated": {
      "result": "(true/false)",
      "justification": "(Confirm that anecdotes from the CONTEXT_BRIEF were used.)"
    },
    "collaborative_framing_used": {
      "result": "(true/false)",
      "justification": "(Confirm that partnerships are framed collaboratively, not prescriptively.)"
    }
  }
}
```

## Quality Checklist
-   [ ] Are the `speaker_notes` complete paragraphs, not just bullet points?
-   [ ] Have the `key_anecdotes_and_stories` from the `CONTEXT_BRIEF` been incorporated?
-   [ ] Is the framing of partnerships and ecosystems collaborative, not prescriptive?
-   [ ] Is the output valid JSON?
