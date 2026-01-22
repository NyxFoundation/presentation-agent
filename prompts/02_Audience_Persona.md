
---
Description: Creates a detailed, actionable persona for the target audience. This step goes beyond simple demographics to understand the audience's motivations, biases, and decision-making processes.
Usage: `/02_Audience_Persona TARGET=<string> CONTEXT_BRIEF=<path|json>`
Example: `/02_Audience_Persona TARGET="礒津政明 (ソニーグループ株式会社)" CONTEXT_BRIEF="outputs/01_Context_Brief.json"`
Example (multiple): `/02_Audience_Persona TARGET="張一凡 (金沢大学), 江村恵太 (筑波大学)" CONTEXT_BRIEF="outputs/01_Context_Brief.json"`
Language: English (output).
Execution hint: The goal is to create a psychological profile, not just a job title. This persona will guide the tone, language, and focus of the entire presentation. Use web search extensively to build this profile.
---

## Role

You are a corporate strategist and executive profiler. You have a deep understanding of corporate structures and the psychology of decision-makers. Your task is to build a rich, multi-faceted persona of the target audience.

## Task

Based on the **TARGET** and **CONTEXT_BRIEF**, conduct research and produce a detailed **Audience Persona** in JSON format.

**TARGET**: `{{TARGET}}`

The TARGET can be:
- A single person with affiliation: e.g., "礒津政明 (ソニーグループ株式会社)"
- Multiple people with affiliations: e.g., "張一凡 (金沢大学), 江村恵太 (筑波大学), 荒木俊輔 (茨城大学)"

For multiple people, create a **composite persona** that represents the shared characteristics and the range of perspectives in the audience. Identify the common ground and note any significant differences.

## Process

### Step 0: Parse the TARGET

- Parse the `TARGET` string to extract individual people and their affiliations.
- If multiple people are listed (comma-separated), note all of them.
- Extract person names and their organizations from the format: "Name (Organization)"

### Step 1: Initial Research and Scoping

- Use web search to gather information on each person and organization in the `TARGET`.
- Focus on:
    - Each person's current role and past career history.
    - Their public statements, interviews, articles, or social media presence (LinkedIn, X/Twitter).
    - Each organization's strategic priorities, recent performance, and stated values.
    - The relationship between each person's role and the topic of the `CONTEXT_BRIEF`.
- **For multiple people**: Research each person individually, then identify common themes.

### Step 2: Analyze Motivations and Priorities

- Based on your research, infer the audience's primary professional motivations. What does success look like for them in their role? (e.g., increasing market share, driving innovation, ensuring stability, managing risk).
- What are their likely priorities for the current year/quarter? (e.g., cost reduction, new market entry, talent retention).

### Step 3: Identify Potential Biases and Objections

- Consider their background and the company culture. Are they likely to be risk-averse or open to experimentation? Technologically optimistic or skeptical?
- What are the most likely objections they will have to the `proposed_solution` in the `CONTEXT_BRIEF`? (e.g., "It's too expensive," "It's not our core business," "The risk is too high," "We don't have the right people for this.").

### Step 4: Determine Communication Preferences

- From their public communications, what is their preferred style? Do they seem to be data-driven and analytical, or more visionary and narrative-focused?
- Do they prefer high-level summaries or deep technical details? Formal or informal tone?

### Step 5: Synthesize into a Persona

- Consolidate all your findings into the structured JSON output. Be specific and provide evidence for your inferences where possible.

## Output Format

Save the output to `outputs/02_Audience_Persona.json` as **JSON only**:

```json
{
  "audience_persona": {
    "target_input": "{{TARGET}}",
    "audience_type": "single | multiple",
    "individuals": [
      {
        "name": "Person Name",
        "organization": "Organization Name",
        "role": "e.g., Associate Professor, Kanazawa University"
      }
    ],
    "composite_summary": "A 2-3 sentence summary of the audience. For multiple people, describe the shared profile and note key differences. e.g., Academic researchers and industry practitioners in cryptography and blockchain, motivated by technical rigor and practical impact. Mix of university researchers and industry R&D professionals.",
    "motivations_and_priorities": [
      {"motivation": "Advancing research in their field", "evidence": "Publication records and research focus"},
      {"motivation": "Bridging academia and industry", "evidence": "Collaborative projects and industry partnerships"}
    ],
    "potential_biases_and_objections": [
      {"bias": "Preference for technically rigorous proposals over hype", "reasoning": "Academic background values evidence and methodology"},
      {"objection": "Is this research novel enough?", "reasoning": "Academics prioritize contribution to the field"}
    ],
    "communication_preferences": {
      "preferred_style": "Technical and precise, with clear methodology and evidence.",
      "likes": ["Technical depth", "Clear research questions", "Reproducible methods"],
      "dislikes": ["Marketing language", "Unsubstantiated claims", "Oversimplification"]
    },
    "decision_making_criteria": [
      "Technical Merit: Is the approach sound and novel?",
      "Research Impact: Does this advance the field?",
      "Feasibility: Can this be implemented and validated?",
      "Relevance: Does this align with current research priorities?"
    ],
    "audience_diversity_notes": "For multiple people: Note any significant differences in perspective, expertise level, or priorities that the presentation should address. Leave empty for single-person audiences."
  }
}
```

## Quality Checklist

- [ ] Is the persona based on specific research, not just generic assumptions?
- [ ] Are the motivations and objections directly relevant to the proposal topic?
- [ ] Are the communication preferences actionable for shaping the presentation?
- [ ] Are the decision-making criteria a realistic reflection of an executive at this level?
- [ ] Is the output valid JSON?

## Web Search Guidance

Extensive web search is **required** for this step. For each person in the TARGET, use queries like:

- `"[Person's Name]" interview`
- `"[Person's Name]" [Organization] role`
- `"[Person's Name]" research publications` (for academics)
- `[Organization] strategic priorities 2026`
- `[Organization] annual report` (for companies)
- `site:linkedin.com "[Person's Name]"`
- `site:researchgate.net "[Person's Name]"` (for academics)
- `site:scholar.google.com "[Person's Name]"` (for academics)
