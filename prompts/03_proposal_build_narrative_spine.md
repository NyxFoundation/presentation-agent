
---
Description: Build the proposal deck narrative using Sparkline by default (What is ↔ What could be), culminating in a clear call-to-action. Ensures the first two slides establish urgency and the decision request.
Usage: `/03_proposal_build_narrative_spine DECISION_BRIEF=<path|json> GOVERNING_THOUGHT=<string> KEY_CLAIMS=<json>`
Example: `/03_proposal_build_narrative_spine DECISION_BRIEF="outputs/01_decision_brief.json" GOVERNING_THOUGHT="..." KEY_CLAIMS='["...", "..."]'`
Language: Japanese (output).
Execution hint: Proposal decks should default to Sparkline unless the deck is purely informational.
---

## Role

You are a proposal storyteller who drives urgency, credibility, and commitment.

## Task

Select narrative_model (default SPARKLINE) and output a beat spine suitable for slide mapping.

## Inputs

1. **DECISION_BRIEF** (`{{DECISION_BRIEF}}`)
2. **GOVERNING_THOUGHT** (`{{GOVERNING_THOUGHT}}`)
3. **KEY_CLAIMS** (`{{KEY_CLAIMS}}`)

## Process

### Step 1: Default to Sparkline

Use SPARKLINE beats (adjust count but keep order):

1. WHAT_IS（現状）
2. PAIN/IMPACT（放置コスト・機会損失）
3. WHAT_COULD_BE（理想）
4. PROPOSAL（提案の全体像）
5. WHY_NOW（なぜ今）
6. PROOF（根拠サマリ：効果/事例）
7. FEASIBILITY（実現性：体制/技術）
8. PLAN（ロードマップ/PoC設計）
9. RISK_MITIGATION（リスク・セキュリティ）
10. COST_ROI（コストと投資回収）
11. CALL_TO_ACTION（意思決定依頼）

### Step 2: Make Each Beat Slide-Ready

* 6〜12拍に収め、各拍が “1スライド=1役割” になる粒度にする

### Step 3: Opening Two Slides Goal

* スライド1〜2で「何の問題で、放置コストがあり、何を決めてほしいか」まで到達

## Output Format

Save the output to `outputs/03_narrative_spine.json` as **JSON only**:

```json
{
  "narrative_model": "SPARKLINE",
  "spine": [
    {"beat": "WHAT_IS", "intent": "...", "notes": "..."}
  ],
  "opening_two_slides_goal": ["...", "..."]
}
```

## Quality Checklist

* [ ] 提案資料として緊急性→提案→根拠→依頼の流れ
* [ ] 各beatが1スライドに落ちる
* [ ] 冒頭2枚で意思決定依頼が見える
* [ ] JSONのみ

## Web Search Guidance

Use web search to:

1. 冒頭で刺さる統計（業界課題）
2. 類似導入事例（一次情報）
3. 競合や代替案の最新動向