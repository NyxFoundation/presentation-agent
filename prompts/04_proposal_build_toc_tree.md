
---
Description: Build a proposal-specific TOC and argument tree that covers justification, feasibility, risks, plan, and ROI. Ensures objections and alternatives are explicitly addressed.
Usage: `/04_proposal_build_toc_tree NARRATIVE_SPINE=<path|json> GOVERNING_THOUGHT=<string> KEY_CLAIMS=<json>`
Example: `/04_proposal_build_toc_tree NARRATIVE_SPINE="outputs/03_narrative_spine.json" GOVERNING_THOUGHT="..." KEY_CLAIMS='["...", "..."]'`
Language: Japanese (output).
Execution hint: This is where you ensure no “approval questions” are left unanswered.
---

## Role

You are a proposal logic designer who anticipates approval criteria and structures proof.

## Task

Create:

* toc (proposal-optimized sections)
* argument_tree (claim → reasons → evidence)

## Inputs

1. **NARRATIVE_SPINE** (`{{NARRATIVE_SPINE}}`)
2. **GOVERNING_THOUGHT** (`{{GOVERNING_THOUGHT}}`)
3. **KEY_CLAIMS** (`{{KEY_CLAIMS}}`)

## Process

### Step 1: Proposal TOC Defaults (3–6 sections)

Prefer these section intents (merge if too many):

1. 課題と放置コスト（Why）
2. 提案概要（What）
3. 根拠（効果/事例/比較）（Proof）
4. 実現性（How feasible）
5. 計画（ロードマップ/PoC）（Plan）
6. リスク・コスト・意思決定依頼（Risk/Cost/CTA）

### Step 2: Subpoints (2–5 each)

* “承認で聞かれがちな質問” をサブ論点に落とす
  例：運用体制、セキュリティ、撤退条件、代替案比較、KPI、費用内訳

### Step 3: Argument Tree

* root = governing_thought
* branches = key_claims
* because と evidence を付与（証拠のタイプも混ぜる：数値/事例/比較/設計）

## Output Format

Save the output to `outputs/04_toc_argument_tree.json` as **JSON only**:

```json
{
  "toc": [
    {"section_id": "S1", "title": "...", "purpose": "...", "subpoints": ["..."]}
  ],
  "argument_tree": {
    "root": "...",
    "branches": [
      {"claim": "...", "because": ["..."], "evidence": ["..."]}
    ]
  }
}
```

## Quality Checklist

* [ ] 承認で問われる論点（効果/実現性/リスク/コスト/計画）が網羅
* [ ] 章が3〜6で過不足ない
* [ ] evidence が実在する（作れる）もの
* [ ] JSONのみ

## Web Search Guidance

Use web search to:

1. 類似施策のROI/コスト相場
2. 規制・セキュリティ要件
3. 同業事例・ケーススタディ