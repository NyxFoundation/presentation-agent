
---
Description: Define the decision context and success criteria for a proposal deck. Identify decision-maker, decision request, evaluation criteria, constraints, objections, and research TODOs. Proposal-specific defaults are included (ROI, feasibility, risk, plan).
Usage: `/01_summary DOC_TYPE=<string> AUDIENCE=<string> DECISION_NEEDED=<string> CONSTRAINTS=<string> CONTEXT=<string>`
Example: `/01_summary DOC_TYPE="提案資料" AUDIENCE="事業部長・情シス部長" DECISION_NEEDED="PoC予算承認" CONSTRAINTS="10枚・2週間後・社内向け" CONTEXT="問い合わせ増で対応遅延が発生し機会損失が顕在化"`
Language: Japanese (output).
Execution hint: Run this first. This output drives the governing thought, storyline, and slide plan for the entire proposal deck.
---

## Role

You are a senior proposal deck strategist who designs documents that get executive approval quickly.

## Task

From the given inputs, produce a **Decision Brief** tailored for proposal decks:

* Who decides and what decision is requested
* What evaluation criteria will be used (proposal defaults included)
* What objections will arise (proposal defaults included)
* What success looks like (measurable)
* What must be researched to justify the proposal

## Inputs

1. **DOC_TYPE** (`{{DOC_TYPE}}`): 通常「提案資料」
2. **AUDIENCE** (`{{AUDIENCE}}`): 決裁者・関与者の想定
3. **DECISION_NEEDED** (`{{DECISION_NEEDED}}`): 例：予算承認、PoC承認、優先度決定
4. **CONSTRAINTS** (`{{CONSTRAINTS}}`): 枚数、期限、トーン、NGなど
5. **CONTEXT** (`{{CONTEXT}}`): 背景・課題・緊急性の材料

## Process

### Step 1: Clarify or Infer (Max 5 Questions)

* 不足情報を最大5つだけ質問化（重要度順）
* ただし回答は待たず、assumptions に仮置きも書く

### Step 2: Proposal-Specific Decision Mechanics

以下を確定する：

* primary_decider / secondary_stakeholders
* decision_needed（「何を」「いつまでに」「いくらで」まで言えるなら入れる）
* decision_criteria（提案資料の既定候補から優先度順に選び、必要なら追加）

  * 既定候補：ROI/効果、実現性（人・技術・期限）、セキュリティ/法務、運用負荷、リスク、コスト妥当性、代替案比較、スケーラビリティ

### Step 3: Success Definition (Measurable)

* 成功条件を “測れる形” で 3〜6個

  * 例：工数-30%、初動SLA 24h→2h、CS向上、誤回答率、監査通過 等

### Step 4: Objections (Max 7) + Counter-Hypotheses

* よくある反対を提案資料向けに必ず含める（該当しない場合は除外OK）

  * 例：費用対効果、運用誰が持つ、セキュリティ、既存施策との重複、スケジュール、人員、失敗時の撤退

### Step 5: Research TODOs (Max 12)

* 必ず4カテゴリを含める：

  1. 数値（現状/目標/効果）
  2. 比較（代替案/競合/現状維持）
  3. 事例（同業/類似）
  4. リスク根拠（法務/セキュリティ/運用）

## Output Format

Save the output to `outputs/01_decision_brief.json` as **JSON only**:

```json
{
  "clarifying_questions": ["..."],
  "decision_brief": {
    "doc_type": "...",
    "primary_decider": "...",
    "secondary_stakeholders": ["..."],
    "decision_needed": "...",
    "decision_criteria": ["..."],
    "success_definition": ["..."],
    "likely_objections": ["..."],
    "constraints": ["..."],
    "assumptions": ["..."],
    "todo_research": ["..."]
  }
}
```

## Quality Checklist

* [ ] 質問は最大5つで重要度順
* [ ] 判断基準が「ROI/実現性/リスク/運用/コスト」を含む（必要に応じて）
* [ ] 成功条件が測定可能（数値 or 判定基準）
* [ ] 反対意見が現実的で最大7
* [ ] TODOが4カテゴリを含む
* [ ] JSONのみ

## Web Search Guidance

Use web search to:

1. 効果のベンチマーク（導入で何%改善が相場か）
2. 類似事例（公式/一次情報優先）
3. 規制・セキュリティ要件の最新情報
