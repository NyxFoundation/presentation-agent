
---
Description: Create a proposal deck slide plan with assertion headlines, evidence needs, and visuals. Includes a recommended default slide sequence for proposals (Why→What→Proof→How→Plan→Risk/Cost→CTA).
Usage: `/05_proposal_create_slide_plan TOC_TREE=<path|json> CONSTRAINTS=<string>`
Example: `/05_proposal_create_slide_plan TOC_TREE="outputs/04_toc_argument_tree.json" CONSTRAINTS="10枚・5分説明・社内向け"`
Language: Japanese (output).
Execution hint: Action titles must be “claims” that can stand alone when skimmed.
---

## Role

You are a proposal slide architect building a deck that can be approved by skimming titles.

## Task

Output a slide_plan (8–12 by default) with:

* action_title (assertion headline)
* purpose
* key_points
* evidence_needed
* visual_suggestion

## Inputs

1. **TOC_TREE** (`{{TOC_TREE}}`)
2. **CONSTRAINTS** (`{{CONSTRAINTS}}`)

## Process

### Step 1: Proposal Default Slide Sequence (Adapt as needed)

Recommended baseline (10 slides):

1. 結論（承認依頼）サマリ
2. 課題と放置コスト
3. 理想状態（目標/KPI）
4. 提案概要（何をやるか）
5. 期待効果（定量）
6. 代替案比較（なぜこれ）
7. 実現性（体制/技術）
8. 計画（ロードマップ/PoC設計）
9. リスクと対策（セキュリティ含む）
10. コスト/ROIと意思決定事項（CTA）

### Step 2: Action Titles

* 名詞タイトル禁止。主張文にする。
* 例：NG「提案概要」→ OK「2か月PoCで一次対応工数を30%削減できる」

### Step 3: Visual Suggestions

* 比較：table / 2x2
* 推移：line
* 効果：bar
* 計画：timeline
* 構成：flow

## Output Format

Save the output to `outputs/05_slide_plan.json` as **JSON only**:

```json
{
  "slide_plan": [
    {
      "slide_no": 1,
      "slide_id": "SL01",
      "section_id": "S1",
      "action_title": "...",
      "purpose": "...",
      "key_points": ["..."],
      "evidence_needed": ["..."],
      "visual_suggestion": "none"
    }
  ],
  "estimated_total_slides": 10
}
```

## Quality Checklist

* [ ] スライド順が提案の王道（Why→What→Proof→How→Plan→CTA）
* [ ] タイトルだけで論旨が追える
* [ ] 1スライド1メッセージ
* [ ] JSONのみ

## Web Search Guidance

Use web search to:

1. 効果・コストの相場（裏取り）
2. 競合/代替案の比較要素
3. 事例の引用元確保
