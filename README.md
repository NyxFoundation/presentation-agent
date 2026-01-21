# Presentation Agent

## 概要

本パイプラインは、世界最高峰のコンサルティングファーム（McKinsey, BCG）の論理的厳密性と、伝説的なプレゼンター（Steve Jobs, Nancy Duarte）の感情的影響力を融合させた、理想的なプレゼンテーション資料作成エージェントです。

## 設計思想

本パイプラインは、以下の3つの原則を核としています。

1.  **戦略主導 (Strategy-First):** コンテンツ作成に着手する前に、「なぜ話すのか」「誰に話すのか」「何を伝えたいのか」を徹底的に定義します。
2.  **論理と感情の融合 (Logic & Emotion):** ピラミッド原則に基づく論理構造と、Sparklineのような物語構造を明確に分離し、意図的に組み合わせます。
3.  **反復的な具体化 (Iterative Refinement):** 抽象的なアイデアから具体的な成果物へと段階的に具体化し、品質を段階的に向上させます。

## パイプライン構成

パイプラインは4つのフェーズ、9つのステップで構成されます。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          PHASE 1: FOUNDATION                                │
│                        (戦略・理解フェーズ)                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────┐    ┌───────────────┐    ┌───────────────┐              │
│  │ 01. Context   │───▶│ 02. Audience  │───▶│ 03. Core      │              │
│  │    Analysis   │    │    Persona    │    │    Strategy   │              │
│  └───────────────┘    └───────────────┘    └───────────────┘              │
│       ↓ RAW_INPUT          ↓ PERSON_NAME        ↓ PURPOSE                  │
│                            ↓ COMPANY            ↓ CORE_MESSAGE             │
│                                                 ↓ NARRATIVE_ARCHETYPE      │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PHASE 2: ARCHITECTURE                               │
│                        (構造・論証フェーズ)                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────┐    ┌───────────────────────┐                    │
│  │ 04. Governing         │───▶│ 05. Narrative         │                    │
│  │     Argument          │    │     Blueprint         │                    │
│  │ (Pyramid Principle)   │    │ (Action Titles)       │                    │
│  └───────────────────────┘    └───────────────────────┘                    │
│       ↓ GOVERNING_THOUGHT          ↓ SLIDE-BY-SLIDE OUTLINE                │
│       ↓ KEY_CLAIMS                                                         │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHASE 3: CONTENT                                  │
│                     (コンテンツ・ビジュアルフェーズ)                           │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────┐    ┌───────────────────────┐                    │
│  │ 06. Slide             │───▶│ 07. Visual            │                    │
│  │     Drafting          │    │     Design            │                    │
│  │ (Bullets & Notes)     │    │ (Charts & Diagrams)   │                    │
│  └───────────────────────┘    └───────────────────────┘                    │
│       ↓ KEY_POINTS                 ↓ VISUAL_SPEC                           │
│       ↓ SPEAKER_NOTES              ↓ TAKEAWAY                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PHASE 4: POLISH & EXPORT                             │
│                       (レビュー・エクスポートフェーズ)                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────┐    ┌───────────────────────┐                    │
│  │ 08. Executive         │───▶│ 09. Final             │                    │
│  │     Review            │    │     Export            │                    │
│  │ (Murder Board)        │    │ (Slidev Markdown)     │                    │
│  └───────────────────────┘    └───────────────────────┘                    │
│       ↓ VERDICT                    ↓ SLIDEV FILES                          │
│       ↓ REMEDIATION_PLAN                                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 各ステップの詳細

| Step | Name | Description | Key Output |
|---|---|---|---|
| 01 | Context Analysis | ユーザーの断片的な入力を構造化された情報に整理 | `Context_Brief.json` |
| 02 | Audience Persona | ターゲットオーディエンスの詳細なペルソナを構築 | `Audience_Persona.json` |
| 03 | Core Strategy | プレゼンの目的、コアメッセージ、ナラティブ構造を決定 | `Core_Strategy.json` |
| 04 | Governing Argument | ピラミッド原則に基づく論理構造を構築 | `Governing_Argument.json` |
| 05 | Narrative Blueprint | スライドごとのAction Titleを設計 | `Narrative_Blueprint.json` |
| 06 | Slide Drafting | 各スライドの箇条書きとスピーカーノートを作成 | `Slide_Drafts.json` |
| 07 | Visual Design | 各スライドのビジュアル（チャート、図）を設計 | `Visual_Designs.json` |
| 08 | Executive Review | 決裁者の視点から最終レビューを実施 | `Executive_Review.json` |
| 09 | Final Export | レビュー結果を反映し、Slidev形式でエクスポート | `Final_Export.json` |

## 使い方

### 1. セットアップ

```bash
# リポジトリをクローン
git clone <repository_url>
cd presentation-agent
```

### 2. 入力ファイルの準備

`inputs/introduction.md` にプレゼンテーションの元ネタを記述します。

```bash
# テンプレートを編集
vim inputs/introduction.md
```

### 3. Makefile の設定

`Makefile` の先頭にある変数を編集します。

```makefile
# --- User Inputs (Edit these for your presentation) ---
PERSON_NAME ?= 礒津政明
COMPANY ?= ソニーグループ株式会社
RAW_INPUT ?= inputs/introduction.md
CONSTRAINTS ?= 15 slides max, 15-minute presentation
```

### 4. パイプラインの実行

```bash
# 全ステップを実行
make all

# または、個別のステップを実行
make context_analysis
make audience_persona
# ...
```

### 5. 出力の確認

- 各ステップの出力は `outputs/` ディレクトリに保存されます。
- 最終的なSlidevファイルのマニフェストは `outputs/09_Final_Export.json` に出力されます。

### 6. Slidevの実行

```bash
bun i
bun dev
```

http://localhost:3030 へ

## ディレクトリ構成

```
.
├── Makefile                    # パイプラインオーケストレーター
├── README.md                   # 本ファイル
├── prompts/                    # プロンプトファイル
│   ├── 01_Context_Analysis.md
│   ├── 02_Audience_Persona.md
│   ├── 03_Core_Strategy.md
│   ├── 04_Governing_Argument.md
│   ├── 05_Narrative_Blueprint.md
│   ├── 06_Slide_Drafting.md
│   ├── 07_Visual_Design.md
│   ├── 08_Executive_Review.md
│   └── 09_Final_Export.md
├── inputs/                     # ユーザー入力
│   └── introduction.md
├── outputs/                    # 生成された中間ファイル
│   ├── 01_Context_Brief.json
│   ├── ...
│   └── logs/                   # Claude CLI のログ
└── slides/                     # 最終的なSlidevファイル
```

## 参考にした手法

- **McKinsey / BCG**: ピラミッド原則、Action Titles
- **Barbara Minto**: 「考える技術・書く技術」
- **Nancy Duarte**: Sparkline、「What Is vs. What Could Be」
- **Steve Jobs**: シンプルさ、ビジュアル優先、ストーリーテリング
- **Jeff Bezos**: 6ページメモ、ナラティブ構造
- **Gene Zelazny**: データビジュアライゼーションの原則
