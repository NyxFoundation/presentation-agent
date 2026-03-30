# pretext-flow スキル

スライドに pretext-flow レイアウト（テキスト回り込み + 画像バウンスアニメーション）を適用する。

## いつ使うか

ユーザーが「pretext」「回り込み」「テキストフロー」「バウンス」「キャラ動かす」などと言及した場合。

## レイアウトの仕組み

`layouts/pretext-flow.vue` が以下を提供する：

1. **画像のバウンスアニメーション** — 背景透過 PNG が画面内をジグザグに移動
2. **テキスト回り込み** — `@chenglou/pretext` で画像の輪郭（ピクセルレベル）に沿ってテキストをリアルタイムレイアウト
3. **ドラッグ操作** — 画像をマウスでドラッグ可能（ドラッグ中はアニメーション一時停止）

## 使い方

### スライドの frontmatter

```yaml
---
layout: pretext-flow
charSrc: /images/logo.png
charWidth: 172
charHeight: 116
speedX: 1.5
speedY: 0.8
font: 20px Noto Sans JP
lineHeight: 30
padding: 4
textColor: '#111'
---
```

### 本文

frontmatter の下にプレーンテキストを書く。Markdown 記法ではなく、純粋なテキストとして扱われる（pretext が Canvas API でレイアウトするため）。

```markdown
---
layout: pretext-flow
charSrc: /images/logo.png
charWidth: 172
charHeight: 116
---

ここにスライドの本文テキストを書く。テキストは画像の輪郭に沿って自動的に回り込む。
```

### props 一覧

| prop | 型 | デフォルト | 説明 |
|------|------|-----------|------|
| charSrc | String | /images/logo.png | 画像パス（背景透過 PNG 推奨） |
| charWidth | Number | 172 | 表示幅 px |
| charHeight | Number | 116 | 表示高さ px |
| font | String | 20px Noto Sans JP | テキストのフォント（CSS font shorthand） |
| lineHeight | Number | 30 | 行の高さ px |
| speedX | Number | 1.5 | 水平移動速度 px/frame |
| speedY | Number | 0.8 | 垂直移動速度 px/frame |
| padding | Number | 4 | 画像とテキストの間隔 px |
| textColor | String | #111 | テキスト色 |

## 新しい画像を使う場合

1. 背景透過 PNG を用意する
2. `sips -Z 300 "元画像" --out public/images/name.png` で適切なサイズに縮小
3. `sips -g pixelWidth -g pixelHeight public/images/name.png` で実寸を確認
4. frontmatter の `charSrc`, `charWidth`, `charHeight` を実寸に合わせて設定

## コンポーネント版（PretextFlow.vue）

レイアウトではなくコンポーネントとして使う場合は `components/PretextFlow.vue` を直接使用する：

```markdown
<PretextFlow
  text="テキスト内容"
  charSrc="/images/logo.png"
  :charWidth="172"
  :charHeight="116"
/>
```

コンポーネント版は `text` prop にテキストを渡す。レイアウト版は slot（本文）からテキストを取得する。
