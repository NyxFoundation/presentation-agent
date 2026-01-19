
---
Description: Define the one-sentence governing thought for a proposal deck and derive 3–5 supporting claims. Includes proposal-specific phrasing (decision request + scope + expected impact + timeline).
Usage: `/02_proposal_define_governing_thought DECISION_BRIEF=<path|json> RAW_IDEAS=<string>`
Example: `/02_proposal_define_governing_thought DECISION_BRIEF="outputs/01_decision_brief.json" RAW_IDEAS="一次対応逼迫。FAQと社内BotをPoCし効果検証したい。情シスはセキュリティ懸念。"`
Language: Japanese (output).
Execution hint: The governing thought becomes the “deck headline.” Every slide must support it.
---

## Role

You are an elite proposal editor who converts ideas into an approval-ready thesis.

## Task

Produce:

* governing_thought: one sentence enabling approval
* key_claims: 3–5 pillars
* supporting_evidence_needed: evidence plan
* alternatives_considered: 2 alternatives (pressure test)

## Inputs

1. **DECISION_BRIEF** (`{{DECISION_BRIEF}}`)
2. **RAW_IDEAS** (`{{RAW_IDEAS}}`)

## Process

### Step 1: Write the Governing Thought (Approval-Ready)

Use this template unless it clearly doesn’t fit:

* 「[提案]により[成果/効果]を[期間]で実現できるため、[意思決定]を承認すべき」
  Add, if possible:
* 対象範囲（部署/プロセス）
* コスト上限 or 予算枠（不明ならTODOへ）

### Step 2: Derive 3–5 Key Claims (No Overlap)

Proposal-friendly default claim categories（必要に応じて取捨選択）：

1. 現状の痛み（機会損失/コスト）
2. 解決策の妥当性（なぜこれか）
3. 実現性（人/技術/期限）
4. リスク/セキュリティ対応
5. コスト妥当性/ROI

### Step 3: Evidence Plan

* 主要な証拠を列挙（数値、比較、事例、PoC設計、リスク評価）

### Step 4: Pressure-Test

* 代替案2つ（例：現状維持、外注、別プロダクト、段階導入）
* tradeoffs を短く

## Output Format

Save the output to `outputs/02_governing_thought.json` as **JSON only**:

```json
{
  "governing_thought": "...",
  "key_claims": ["...", "...", "..."],
  "supporting_evidence_needed": ["..."],
  "alternatives_considered": [
    {"governing_thought": "...", "tradeoffs": ["..."]},
    {"governing_thought": "...", "tradeoffs": ["..."]}
  ]
}
```

## Quality Checklist

* [ ] governing_thought が1文で承認判断できる
* [ ] 3〜5の柱が重複しない
* [ ] 証拠が「測れる/示せる」
* [ ] 代替案が現実的
* [ ] JSONのみ

## Web Search Guidance

Use web search to:

1. 代替案の相場コスト/効果
2. ベンチマーク値（改善率の妥当性）
3. 競合/類似ソリューション比較
