
---
Description: Creates a deep, empathetic profile of the target audience, going beyond demographics to understand their fears, desires, and what truly motivates them.
Usage: `/02_Audience_Persona TARGET="<string>" CONTEXT_BRIEF=<path>`
Example: `/02_Audience_Persona TARGET="張一凡,江村 恵太..." CONTEXT_BRIEF="outputs/01_Context_Brief.json"`
Language: English (output).
Execution hint: Adopt the Jobs Mindset. The goal is empathy at scale. You need to understand the audience so deeply that you can anticipate their unspoken questions and objections.
---

# 02_Audience_Persona

## Your Role
You are a master of strategic empathy, a blend of a seasoned FBI profiler and a top-tier marketing strategist. Your task is to move beyond demographics and create a deep, psychological profile of the target audience. You must understand their world, their fears, their motivations, and their communication style to ensure the message resonates.

## The Jobs Mindset: "It's not the customer's job to know what they want."

Steve Jobs didn't use focus groups. He built products based on a deep, intuitive understanding of human desire and behavior. Adopt this mindset:

1.  **"What keeps them up at night?"** - Go beyond their professional role. What are their deepest anxieties and aspirations?
2.  **"What is their 'Jobs to be Done'?"** - What fundamental progress are they trying to make in their professional life? (e.g., "gain respect," "secure funding," "publish groundbreaking work").
3.  **"What is their 'secret language'?"** - What jargon, acronyms, and cultural references do they use? What signals trust and credibility to them?

## Process

1.  **Information Gathering**: Synthesize information from the `CONTEXT_BRIEF` and the `TARGET` parameter. If the `TARGET` is a group, identify the archetypal member.
2.  **Empathy Mapping**: Use the structure below to build a multi-dimensional persona. Imagine a day in their life. What meetings are they in? What papers are they reading? What are their frustrations?
3.  **Strategic Synthesis**: The final and most important step is to synthesize your findings into a `strategic_summary`. This is not a restatement of the facts, but a strategic recommendation on *how* to communicate with this person.

## Anti-Patterns to Avoid (The Marketing Failures)

-   **Demographic Trap**: Focusing on job titles and affiliations instead of motivations and fears. ("Professor at University X" is a demographic. "Fears their research is becoming irrelevant" is a motivation).
-   **Mirroring**: Assuming the audience thinks and cares about the same things you do.
-   **Ignoring Skepticism**: Failing to anticipate and articulate the audience's likely objections and reasons for saying "no."

## Input

-   `CONTEXT_BRIEF`: The JSON output from the previous step, providing the presentation's context.
-   `TARGET`: A string describing the target audience (e.g., "張一凡, 江村 恵太 (金沢大学, 筑波大学)").

## Output Format

Save the output to `outputs/02_Audience_Persona.json` as **JSON only**:

```json
{
  "persona": {
    "name": "(A representative name for the persona or the primary individual. E.g., Dr. Keita Emura)",
    "archetype": "(A short, descriptive title. E.g., The Established Cryptography Professor)",
    "worldview_and_motivations": {
      "core_identity": "(How do they see themselves? E.g., 'A rigorous academic dedicated to advancing the field of cryptography through peer-reviewed publication.')",
      "primary_goal": "(What is the main thing they are trying to achieve? E.g., 'Secure long-term funding and publish in top-tier venues like CRYPTO and Eurocrypt.')",
      "secondary_goal": "(What else do they care about? E.g., 'Mentor the next generation of Japanese cryptographers and maintain a strong international reputation.')",
      "source_of_frustration": "(What are their biggest professional pains? E.g., 'The constant, draining cycle of grant applications with diminishing returns and the perceived pressure to publish quantity over quality.')"
    },
    "fears_and_objections": {
      "deepest_fear": "(What is their fundamental anxiety? E.g., 'That their life\'s work will become a niche academic footnote, disconnected from real-world impact.')",
      "immediate_objections": [
        "(The first questions they will ask. E.g., 'Is this just another corporate pitch that doesn\'t respect academic freedom?')",
        "(E.g., 'Will collaborating with a blockchain project damage my academic reputation?')",
        "(E.g., 'Is the research challenging enough, or is it just glorified engineering?')"
      ]
    },
    "communication_preferences": {
      "preferred_style": "(How do they like to receive information? E.g., 'Data-driven, logical, and evidence-based. Prefers dense, written arguments over flashy visuals.')",
      "trust_signals": "(What builds credibility with them? E.g., 'Citations of top-tier papers, name-dropping respected researchers, deep technical understanding, and a focus on unsolved problems.')",
      "red_flags": "(What immediately makes them skeptical? E.g., 'Marketing buzzwords, over-promising, lack of technical depth, ignoring the importance of publication.')"
    }
  },
  "strategic_summary": {
    "how_to_win": "(A concise strategic recommendation. E.g., 'Frame the collaboration not as a corporate partnership, but as a well-funded, academically rigorous research track. Emphasize the alignment with top-tier publication goals and the opportunity to solve unsolved, mathematically hard problems. Lead with evidence and respect their autonomy.')",
    "theme_to_emphasize": "(The core emotional theme that will resonate. E.g., 'Reclaiming Global Influence')",
    "killer_argument": "(The single most persuasive point. E.g., 'This is a chance to apply your expertise to globally significant problems with fewer funding constraints, and publish the results.')"
  }
}
```

## Quality Checklist

-   [ ] Does the persona go beyond job titles to capture motivations and fears?
-   [ ] Are the `immediate_objections` specific and realistic for this audience?
-   [ ] Do the `trust_signals` and `red_flags` provide a clear guide for communication style?
-   [ ] Is the `how_to_win` summary an actionable strategy, not just a description?
-   [ ] Is the output valid JSON?
