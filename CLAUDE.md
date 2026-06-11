# presentation-agent

Slidev ベースの会社紹介スライドデッキ。HP (`../nyx-web`) と視覚言語を完全に揃え、Narrative Heat Engineering に沿って構成する。

## 構成

```
slides.md           # エントリ（各 SL を順に src include）
slides/SL*.md       # 1枚 1ファイル。<style> はスライド内スコープ
style.css           # グローバルトークン + プリミティブ（.nx-*）
global-bottom.vue   # 右下の Nyx ロゴ + ページ番号
```

## デザインシステム（p2/p3/p4 で確立）

### カラートークン（HP `tokens.css` 準拠・固定）

| トークン | 値 | 役割 |
|---|---|---|
| `--bg` | `#faf9f5` | 暖色オフホワイト・キャンバス |
| `--bg-2` | `#f3f1ea` | カード／インセット面・ハイライト枠の下地 |
| `--ink` | `#18181a` | ニア黒（暖色）・主タイトル／本文 |
| `--ink-dim` | `#55524c` | 本文セカンダリ |
| `--ink-faint` | `#9a958c` | キャプション・取り消し線 |
| `--accent` | `#1f3a52` | ディープ青 ──「検証」「証明」「✓」 |
| `--severe` | `#a25434` | くすんだ赤茶 ──「退行」「リスク」 |
| `--line` | `rgba(24,24,26,.10)` | 細いライン（黒太枠は禁止） |

**色の意味は固定**：accent 青 = Verifiable / 肯定、severe 赤茶 = Regression / 否定。
スライド間で色が連続して「退行（赤茶）→ 前進（青）」の物語を形成する。

### タイポグラフィ

| フォント | 役割 |
|---|---|
| `Cormorant Garamond` (italic) | 装飾的 em、数式記号（π, ∀） |
| `Shippori Mincho` | 日本語本文・タイトル下地 |
| `JetBrains Mono` | キッカー・軸ラベル・コード風（`VERIFY( π )`, `01 ／ 問題`） |
| `BIZ UDPMincho` | ワードマーク（`Nyx Foundation`、`AI` シンボル）。`!important` で `--font-sans` グローバルを上書き |

### サイズ階層（プレゼン最小可読サイズ・厳守）

| 役割 | サイズ | 用途 |
|---|---|---|
| `nx-display` | **36px** | スライド主タイトル（h1） |
| Hero 特大 | 46–56px | 中心命題スライドの宣言文 |
| `nx-lead` | **16px** | リード本文 |
| サブタイトル / `.ja` | **15px** | h1 直下のサブ説明 |
| `nx-kicker` | **12px** | セクションキッカー |
| カード本文 | **14px** 以上 | dom-body / proj-body 等 |
| ラベル・キャプション | **12–13px** 以上 | mono タグ・ファイルラベル |
| SVG 内テキスト | **13–16px** 以上 | グラフ軸・凡例 |
| SVG 内ヘッドライン | 22–44px | 強調語（「肩書きへの逆行」など） |

**禁則**：本文 12px 未満・ラベル 11px 未満は採用しない（プレゼンで読めない）。SVG 内も `class` 経由でこれを守る。

### 見出し構造（全スライド共通）

```
[nx-kicker] 罫線 + Mono UPPER + 0.18em letter-spacing
01 ／ 問題

[nx-display] Cormorant + Shippori、30px、italic em で「核」を反転
誰が言うかより、<em>何が確かめられたか</em>。
```

`<em>` は強調ではなく「**この一文の核**」を指す意味タグ。必ず italic Cormorant + accent 青で描く。

### レイアウト共通ブロック

```
kicker
display title（italic em で核）
(任意) verse-line-lead   ── 左 2px 縦罫 + bg-2 背景の 1 行リード
MAIN VISUAL（1スライド1枚、大型 SVG）
```

- **1スライド1ビジュアル**。本文は verse 1 行まで、残りは図に語らせる
- 余白は HP 基準：`.sec` の padding は `~1rem 2.6rem`
- スライド canvas は 980×551 (16:9)、SVG `max-width` で外側スケール調整

### メインビジュアル（SVG）原則

1. **inline SVG**。フォント／サイズ／色は SVG 属性ではなく **CSS class 経由**で当てる（属性指定は Slidev のグローバル CSS と衝突する）
2. viewBox を決め打ちし、外側 `max-width` でだけ拡縮する
3. 図形はミニマル：円・矩形・線分の合成。線端は `round`
4. **核となる枠だけハイライト**：bg-2 背景 + accent 2px border で「ここを見て」、それ以外は line 1px の軽量フレーム
5. 数式記号（π, ∀, ＋, ✓）は**重要箇所の代名詞**として大型に使う。`+` は円囲みで演算子化
6. 機械可読感は mono + 括弧表記（`VERIFY( π )`, `01 ／ 問題`）

### テキストルール

- **英訳サブテキスト（.ja）は使わない**（日本語版スライド時）
- 小さい説明文は思い切って削る ── 読めない文字は無意味
- 取り消し線は **mono + ink-faint** で「否定の語彙」を示す（過去・廃止）
- キッカーは `数字 ／ 日本語` 形式（`01 — The Problem` は不可）
- リード本文の `<b>` は強調ではなく語彙のキー化（accent 青ではなく ink 黒で締める）

### スライド種別と視覚パターン

| 種別 | パターン |
|---|---|
| Hero / 中心命題 | 左寄せ宣言 + grid 背景（`.nx-grid-bg`）+ ステータス pulse |
| Problem / 脅威 | 大型 SVG チャート、severe 赤茶で退行方向、italic 大型数字 |
| Thesis / 答え | 3 段フロー（STAGE 01／02／03）、中央 02 を accent 枠でハイライト |
| 列挙（領域・関わり方） | カード grid。bg-2 背景、line 枠、Mono タグ + 和文見出し |
| 単一固有装置（家・組織） | 写真 + italic Cormorant 大見出し + Mono 位置ラベル |

### Narrative Heat Engineering との対応

| スライド帯 | NHE フェーズ | 視覚言語 |
|---|---|---|
| Hero (SL02) | 中心命題の早期提示 | 余白多めの宣言 + grid |
| Problem (SL03) | 古い答えの肯定→限界 | severe 赤茶の大型グラフ |
| Thesis (SL04) | 新しい答え（具体例） | accent 青の 3 段フロー |
| Proof / Dashboard | 伏線回収（最大ピーク①） | architectural italic 数字 / ブラウザバー風 |
| Domains / Projects | 中間資産・固有装置 | カード grid |
| Future / Closing | 青天井感・見ておくべき場所閉じ | 9セクター grid / 静かなカバー |

詳細な NHE プロトコルは Notion `Narrative Heat Engineering：期待熱量を設計するための実践方法論`。

## 運用コマンド

```bash
bun run dev          # 開発サーバ (http://localhost:3030)
bun run build        # 静的ビルド → dist/
```

### PNG エクスポート（NixOS 環境）

playwright 同梱の chromium は NixOS で libglib 不足のため動かない。`nix-shell` でシステム chromium を取得し、`--executable-path` で渡す：

```bash
CHROMIUM=$(nix-shell -p chromium --run "command -v chromium")
nix-shell -p chromium --run \
  "bunx slidev export --format png --output dist-png --executable-path $CHROMIUM --per-slide"
# 特定ページのみ: --range 3 や --range 3,4
```

出力は `dist-png/NN.png`（slide 1-indexed）。Read ツールで直接画像確認できる。

## 留意点

- `mdc: true` のとき、**HTML ブロック内の空行は CommonMark がブロックを終端する** → SL01–15 はすべて空行除去済み。新規スライド作成時も同様にする
- 各スライドの `<style>` はスコープ独立。グローバルに置きたいプリミティブは `style.css` の `.nx-*` クラスへ
- `Nyx Foundation` ワードマークは `--font-wordmark` (`BIZ UDPMincho`) で `!important` 指定（グローバル sans 上書き対策）
