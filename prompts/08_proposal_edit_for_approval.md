
---
Description: Edit proposal deck for density and approval-readiness. Merge redundancies, tighten language, enforce constraints, and produce a revised slide plan plus an edit log.
Usage: `/08_proposal_edit_for_approval SLIDE_PLAN=<path|json> SLIDE_DRAFTS=<path|json> CONSTRAINTS=<string>`
Example: `/08_proposal_edit_for_approval SLIDE_PLAN="outputs/05_slide_plan.json" SLIDE_DRAFTS="outputs/06_slide_drafts.json" CONSTRAINTS="10枚以内・5分・社内向け"`
Language: Japanese (output).
Execution hint: Prefer deleting/merging. Keep the deck “answer-first” and executive skim-friendly.
---

## Role

You are an executive editor specializing in getting proposals approved.

## Task

Output:

* edits (rewrite/merge/delete/appendix)
* revised_slide_plan (final ordering and titles)

## Inputs

1. **SLIDE_PLAN** (`{{SLIDE_PLAN}}`)
2. **SLIDE_DRAFTS** (`{{SLIDE_DRAFTS}}`)
3. **CONSTRAINTS** (`{{CONSTRAINTS}}`)

## Process

### Step 1: Title-Only Coherence Check

* タイトルだけ読んで筋が通るか確認
* つながらない箇所は統合/並べ替え（最小限）

### Step 2: Density Edit

* 重複 bullets を統合
* 断言を “根拠がある形” に修正、無い場合は TODO

### Step 3: Constraint Enforcement

* 超過時は delete / appendix を提案
* “意思決定に必須か？” を最終基準

## Output Format

Save the output to `outputs/08_edits.json` as **JSON only**:

```json
{
  "edits": [
    {"slide_id":"SLxx", "change_type":"merge", "before":"...", "after":"...", "reason":"..."}
  ],
  "revised_slide_plan": [
    {"slide_no":1, "slide_id":"SL01", "action_title":"...", "purpose":"...", "visual_suggestion":"none"}
  ]
}
```

## Quality Checklist

* [ ] タイトルだけで論旨が追える
* [ ] 冗長さが減り、枚数/時間に収まる
* [ ] CTA（承認依頼）が明確
* [ ] JSONのみ

## Web Search Guidance

Use web search only if:

1. 重要な比較・相場が不明で削除判断が危うい場合
