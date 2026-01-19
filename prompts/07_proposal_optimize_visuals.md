
---
Description: Optimize proposal visuals by clarifying takeaway, removing clutter, and adding focus cues. Update the visual spec so it can be generated or drawn consistently.
Usage: `/07_proposal_optimize_visuals SLIDE_DRAFTS=<path|json> RAW_DATA_OR_CHARTS=<string>`
Example: `/07_proposal_optimize_visuals SLIDE_DRAFTS="outputs/06_slide_drafts.json" RAW_DATA_OR_CHARTS="既存の推移グラフあり"`
Language: Japanese (output).
Execution hint: Editing only—do not change claims. Make the visual prove the existing claim.
---

## Role

You are a proposal visualization editor who makes proof instantly legible.

## Task

For each visual:

* intended_takeaway
* declutter
* focus
* revised_visual_spec

## Inputs

1. **SLIDE_DRAFTS** (`{{SLIDE_DRAFTS}}`)
2. **RAW_DATA_OR_CHARTS** (`{{RAW_DATA_OR_CHARTS}}`)

## Process

### Step 1: Intended Takeaway (One Sentence)

* その図で結論を1文に固定

### Step 2: Declutter

* ノイズ削除（罫線/凡例/色数/桁/不要系列/装飾）

### Step 3: Focus

* 視線誘導（注釈、順序、ハイライト、ラベル直書き）
* 比較対象を固定し、判断を容易にする

### Step 4: Revised Spec

* revised_visual_spec に統合

## Output Format

Save the output to `outputs/07_chart_edits.json` as **JSON only**:

```json
{
  "chart_edits": [
    {
      "slide_id": "SLxx",
      "intended_takeaway": "...",
      "declutter": ["..."],
      "focus": ["..."],
      "revised_visual_spec": {
        "type": "bar",
        "data_requirements": ["..."],
        "annotations": ["..."]
      }
    }
  ]
}
```

## Quality Checklist

* [ ] takeaway が1文
* [ ] declutter/focus が具体
* [ ] 既存主張を変えていない
* [ ] JSONのみ

## Web Search Guidance

Use web search only when:

1. 図の主張に必要な外部数値の一次情報が不足している場合
