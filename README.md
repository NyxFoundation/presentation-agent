# Presentation Agent

## 概要

本パイプラインは、世界最高峰のコンサルティングファーム（McKinsey, BCG）の論理的厳密性と、伝説的なプレゼンター（Steve Jobs, Nancy Duarte）の感情的影響力を融合させた、理想的なプレゼンテーション資料作成エージェントです。

## 設計思想

本パイプラインは、以下の3つの原則を核としています。

1.  **戦略主導 (Strategy-First):** コンテンツ作成に着手する前に、「なぜ話すのか」「誰に話すのか」「何を伝えたいのか」を徹底的に定義します。
2.  **論理と感情の融合 (Logic & Emotion):** ピラミッド原則に基づく論理構造と、Sparklineのような物語構造を明確に分離し、意図的に組み合わせます。
3.  **反復的な具体化 (Iterative Refinement):** 抽象的なアイデアから具体的な成果物へと段階的に具体化し、品質を段階的に向上させます。

## クイックスタート

### 1. 入力ファイルの準備

`inputs/introduction.md` にYAML frontmatterとプレゼンテーションの内容を記述します。

```markdown
---
target_audience: "テックカンファレンス2026参加者（ソフトウェアエンジニア）"
audience_type: group
constraints:
  max_slides: 15
  max_duration_minutes: 15
output_language: Japanese
event:
  name: "Tech Conference Tokyo"
---

# プレゼンテーションタイトル

本文をここに記述...
```

### 2. パイプラインの実行

```bash
make all
```

### 3. 出力の確認

```bash
# Slidevで確認
bun dev
# http://localhost:3030 へアクセス
```

## 入力フォーマット

すべての設定は `inputs/introduction.md` のYAML frontmatterで定義します。

### 必須フィールド

| フィールド | 説明 | 例 |
|-----------|------|-----|
| `target_audience` | ターゲットオーディエンス | `"山田太郎 (Example Corp)"` または `"カンファレンス参加者"` |
| `audience_type` | オーディエンスの種類 | `individual` / `group` / `mixed` |
| `constraints.max_slides` | 最大スライド数 | `15` |
| `constraints.max_duration_minutes` | 最大プレゼン時間（分） | `15` |
| `output_language` | 出力言語 | `Japanese` / `English` |

### オプションフィールド

| フィールド | 説明 | 例 |
|-----------|------|-----|
| `event.name` | イベント名 | `"DEPCON Hakodate"` |
| `event.parent_event` | 親イベント | `"Tech Summit 2026"` |
| `event.date` | 日付 | `"2026-01-XX"` |
| `event.location` | 場所 | `"東京"` |

### audience_type の使い分け

| タイプ | 用途 | 例 |
|--------|------|-----|
| `individual` | 特定の個人向けピッチ | 経営幹部への提案 |
| `group` | 共通の特性を持つグループ | カンファレンス発表 |
| `mixed` | 複数の特定個人 | 委員会プレゼン |

### 入力例

#### 個人向け（Executive Pitch）

```yaml
---
target_audience: "山田太郎 (Example株式会社 Chairman, Example Global Education)"
audience_type: individual
constraints:
  max_slides: 10
  max_duration_minutes: 20
output_language: Japanese
---
```

#### グループ向け（Conference Talk）

```yaml
---
target_audience: "テックカンファレンス2026参加者（ソフトウェアエンジニア）"
audience_type: group
constraints:
  max_slides: 15
  max_duration_minutes: 15
output_language: Japanese
event:
  name: "Tech Conference Tokyo"
  parent_event: "Tech Summit 2026"
---
```

#### 複数人向け（Committee Presentation）

```yaml
---
target_audience: "田中花子 (A大学), 鈴木一郎 (B大学), 佐藤次郎 (C大学)"
audience_type: mixed
constraints:
  max_slides: 20
  max_duration_minutes: 30
output_language: Japanese
---
```

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
│   YAML frontmatter        ペルソナ構築          戦略定義                     │
│   + 内容解析              (Context Briefから)                               │
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
└─────────────────────────────────────────────────────────────────────────────┘
```

## 各ステップの詳細

| Step | Name | Description | Key Output |
|---|---|---|---|
| 01 | Context Analysis | YAML frontmatterからメタデータを抽出し、内容を構造化 | `01_Context_Brief.json` |
| 02 | Audience Persona | Context Briefからターゲットを読み取り、ペルソナを構築 | `02_Audience_Persona.json` |
| 03 | Core Strategy | プレゼンの目的、コアメッセージ、ナラティブ構造を決定 | `03_Core_Strategy.json` |
| 04 | Governing Argument | ピラミッド原則に基づく論理構造を構築 | `04_Governing_Argument.json` |
| 05 | Narrative Blueprint | スライドごとのAction Titleを設計 | `05_Narrative_Blueprint.json` |
| 06 | Slide Drafting | 各スライドの箇条書きとスピーカーノートを作成 | `06_Slide_Drafts.json` |
| 07 | Visual Design | 各スライドのビジュアル（チャート、図）を設計 | `07_Visual_Designs.json` |
| 08 | Executive Review | 決裁者の視点から最終レビューを実施 | `08_Executive_Review.json` |
| 09 | Final Export | レビュー結果を反映し、Slidev形式でエクスポート | `09_Final_Export.json` |

## 思考フレームワーク

各プロンプトは、単なるルールではなく「思考フレームワーク」として設計されています。

### Jobs Mindset（02_Audience_Persona）
> "What keeps them up at night?"
> 
> 聴衆の表面的な属性ではなく、深層心理（恐れ、欲求、バイアス）を理解する。

### Bezos Mindset（01_Context_Analysis, 06_Slide_Drafting）
> "Speaker Notes First"
> 
> スライドの箇条書きを書く前に、完全な文章でスピーカーノートを書く。

### McKinsey Mindset（04_Governing_Argument, 05_Narrative_Blueprint）
> "So What?" / "Why So?" テスト
> 
> すべての主張が「だから何？」「なぜそう言える？」に答えられるか検証する。

## 品質保証機能

### 整合性チェック（01_Context_Analysis）

内容とターゲットオーディエンスの整合性を自動検証します。

```json
{
  "consistency_check": {
    "content_matches_declared_audience": true,
    "inferred_audience_from_content": "カンファレンス参加者",
    "notes": "Content and declared audience are aligned."
  }
}
```

不整合が検出された場合：

```json
{
  "consistency_check": {
    "content_matches_declared_audience": false,
    "inferred_audience_from_content": "研究者コミュニティ",
    "notes": "WARNING: Content appears to target researchers, but declared target is corporate executive."
  }
}
```

### Source Fidelity Check（08_Executive_Review）

元の入力に含まれていた重要な要素（創業者ストーリー、アネクドート）が最終出力に保持されているか検証します。

### Evidence Quality Hierarchy（06_Slide_Drafting）

証拠の品質を階層化し、優先順位を明示します。

1. **Hard Data**: 数値、統計、検証可能な事実
2. **Expert Opinion**: 権威ある専門家の見解
3. **Analogies**: 類似事例からの推論
4. **Anecdotes**: 個別の事例やストーリー

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
├── inputs/                     # ユーザー入力（単一ファイル）
│   └── introduction.md         # YAML frontmatter + 内容
├── outputs/                    # 生成された中間ファイル
│   ├── 01_Context_Brief.json
│   ├── ...
│   └── logs/                   # Claude CLI のログ
└── slides/                     # 最終的なSlidevファイル
```

## Makeコマンド

```bash
# 全ステップを実行
make all

# 入力ファイルの検証のみ
make validate

# 個別のステップを実行
make context_analysis
make audience_persona
make core_strategy
make governing_argument
make narrative_blueprint
make slide_drafting
make visual_design
make executive_review
make final_export

# 出力をクリア
make clean

# ヘルプを表示
make help
```

## Slidevの実行

```bash
bun i
bun dev
```

http://localhost:3030 へアクセス

## GitHub Actionsでの実行

GitHub Actionsを使用してパイプラインを自動実行できます。

### 前提条件

- **Self-hosted runner**: `claude` CLIがインストールされ、ログイン済みのself-hosted runnerが必要です
- **リポジトリ権限**: `contents: write` と `pull-requests: write` 権限が必要です

### 実行方法

1. `inputs/introduction.md` にYAML frontmatterと内容を記述してコミット
2. GitHubリポジトリの **Actions** タブを開く
3. **Presentation Pipeline** ワークフローを選択
4. **Run workflow** ボタンをクリック

### 動作の流れ

1. `inputs/introduction.md` からメタデータを抽出
2. `make all` で全パイプラインを実行
3. 生成されたファイルを新しいブランチにコミット
4. Pull Requestを自動作成

### 生成されるPull Request

ワークフロー完了後、以下の内容を含むPRが自動作成されます：

- **ブランチ名**: `presentation/generated-{run_id}-{timestamp}`
- **含まれるファイル**:
  - `outputs/` - パイプラインの中間出力（JSON）
  - `slides/` - 最終的なSlidevマークダウン

### 環境変数

ワークフローで使用される環境変数：

| 変数 | 説明 |
|------|------|
| `CLAUDE_CODE_PERMISSIONS` | `bypassPermissions` に設定（自動実行用） |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | 最大出力トークン数（デフォルト: 100000） |

### Artifactの確認

実行ログは **pipeline-logs** という名前のArtifactとして7日間保存されます。

## 参考にした手法

- **McKinsey / BCG**: ピラミッド原則、Action Titles、So What? / Why So? テスト
- **Barbara Minto**: 「考える技術・書く技術」
- **Nancy Duarte**: Sparkline、「What Is vs. What Could Be」
- **Steve Jobs**: シンプルさ、ビジュアル優先、ストーリーテリング
- **Jeff Bezos**: 6ページメモ、ナラティブ構造、Speaker Notes First
- **Gene Zelazny**: データビジュアライゼーションの原則、1 Chart 1 Message
