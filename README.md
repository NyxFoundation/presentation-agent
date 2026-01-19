# Nyx Foundation プレゼンテーション作成AIエージェント

提案資料に特化した資料作成をサポートしてくれます

## エージェントフロー概要

プロンプトと Makefile で提案資料を自動生成します。

```
inputs/introduction.md  -> /00_contents -> 00_contents.json
           ^            -> /00_audience -> 00_audience.json
           |                  |
           |                  v
           +-> make summary -> 01_decision_brief.json
                -> 02_governing_thought.json
                -> 03_narrative_spine.json
                -> 04_toc_argument_tree.json
                -> 05_slide_plan.json
                -> 06_slide_drafts.json
                -> 07_chart_edits.json
                -> 08_edits.json
                -> 09_slidev_manifest.json (slides/ 配下のMDを生成)
```

## スライド資料生成手順

#### 0. このレポジトリをクローンしてください

```bash
git clone git@github.com:NyxFoundation/presentation-agent
cd presentation-agent
git checkout -b <資料タイトル or 顧客名など> # 資料ごとに新たなブランチを切ること
```

#### 1. インプットを準備  

以下ファイルを編集してください。
- `inputs/introduction.md` に提案の生メモを記載。
- `Makefile` 冒頭の変数を編集して、PERSON_NAME/COMPANY、INTRODUCTION、CONSTRAINTS、TONE、LANGUAGE、FONT、BACKGROUND_COLOR、SLIDEV_THEME などを設定。

#### 2. コンテンツの抽出
```bash
make contents
make audience
```

#### 3. 全体生成（推奨）  

```bash
make all
```

make helpから各コマンドを参照し、各プロセスを個別実行することも可能。

#### 4. Slidevを立ち上げ

```bash
bun install
bun dev
```

visit <http://localhost:3030>

## Slidevについて

#### 基本

1. **slides.md** と **slides/** を編集してスライドを作成
2. 保存すると自動でリロードされる

#### 画像の使用

画像は `public/images/` に格納:

```
public/
└── images/
    ├── logo.png
    └── screenshot.jpg
```

スライド内での参照:

```md
![説明](/images/logo.png)
```

#### レイアウト

```yaml
---
layout: cover      # カバーページ
---

---
layout: two-cols   # 2カラム
---

左側のコンテンツ

::right::

右側のコンテンツ
```

#### Mermaid図

````md
```mermaid {scale: 0.6}
flowchart LR
    A[Start] --> B[End]
```
````

#### 数式 (KaTeX)

```md
インライン: $E = mc^2$

ブロック:
$$
\sum_{i=1}^{n} x_i
$$
```

#### スタイリング (UnoCSS)

```html
<div class="grid grid-cols-2 gap-4">
  <div class="bg-blue-50 p-4 rounded">左</div>
  <div class="bg-green-50 p-4 rounded">右</div>
</div>
```

#### PDF出力

```bash
bun run export
```

## Documentation

- [Slidev 公式ドキュメント (日本語)](https://ja.sli.dev/)
- [Slidev Documentation (English)](https://sli.dev/)
