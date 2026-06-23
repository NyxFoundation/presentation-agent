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
- **2 段（2×2 grid）は使わない** ── 視線の起点が定まらない。1 軸の線形フロー（top→bottom / left→right）を基本に、焦点は 1 つ
- 比較は横並び 3–4 カード（同一軸で A vs 実際の代替 B）
- 集合関係（A ⊂ B）は**入れ子の図形**で描く。並列ボックスは禁止（重複・誤読の元）
- **同じ要素を 2 箇所に重複して書かない**
- 画像は `max-h-[300–460px]` 目安でキャンバス安全域に収める

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
- **`$`（通貨記号）はエスケープしない** ── `\$292M` ではなく `$292M` と書く（`grep -rI '\\\$' slides/` で残存ゼロ）

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

## 投影スライドの中身（入れる / 入れない）

デザインシステム非依存の普遍原則。投影スライドは聴衆が見て追える要素だけに絞る。

**入れない**：詳細タイムテーブル・時刻ごとの内訳／時間表記（`(35分)`, `120分→180分` 等）／認知レベル分類（Bloom's taxonomy 等）／ルーブリック詳細・自己評価リスト／講師の心構え・台本。

**入れる**：図解／比較表（3–7 行）／用語定義／具体例／Open Question／出典。

## 出典（Sources）表示

論文・記事・OSS・事件レポートを参照しているスライドには出典を明記する。ロゴ（右下）と衝突しない位置に：

```html
<div class="absolute bottom-3 left-6 text-[10px] text-gray-400 leading-tight max-w-3xl">
Sources: AUTHORS "TITLE" VENUE YEAR ｜ ...
</div>
```

区切りは全角 ` ｜ `。数値・事件名・固有の主張は出典なしで提示しない。未来事象の数値は「仮想/最新シナリオ」明示か出典脚注を付す。

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

### Firefox フォールバック（chromium がどうしても動かない時）

`dist/` を SPA fallback サーバで配信し、headless Firefox で各ページを撮影する。初回ペイントのタイミングがぶれるので、数回試行して最大サイズの PNG を採用する：

```bash
firefox --headless --window-size=1920,1080 \
  --screenshot=/tmp/slide_NN.png "http://localhost:PORT/N?print"
# blank（極端に小サイズ）になったら並列リトライして最大を採用
```

## 留意点

- `mdc: true` のとき、**HTML ブロック内の空行は CommonMark がブロックを終端する** → SL01–15 はすべて空行除去済み。新規スライド作成時も同様にする
- 各スライドの `<style>` はスコープ独立。グローバルに置きたいプリミティブは `style.css` の `.nx-*` クラスへ
- `Nyx Foundation` ワードマークは `--font-wordmark` (`BIZ UDPMincho`) で `!important` 指定（グローバル sans 上書き対策）

## トンマナ追補（実戦からの学び）

### タイトル・キッカー
- **h1（nx-display）は 1 行に収める**。2 行に折り返すなら短く言い換える。説明的に盛らず、具体的な一言＋**体言止め可**。
- 接続に `──／───`（em dash）を多用しない。句読点・全角空白で素直に。
- **断定調・煽り語・軍事メタファーを使わない**：「青天井」「希少」「巨大市場」「革命的」「本丸」「既成事実」等。キッカーは素直な区分語（`背景／現状／課題／答え`、`コンペ／カンファレンス` 等）にする。これは NHE「言うな、想起させろ」と一致。

### 用語
- 同じ概念は**デッキ全体で 1 語に固定**する。例：Trust は **「信頼」で統一**（「信用」＝金融的 credit と混同しない。trustless＝「信頼が要らない」）。`grep` でゆれを確認する。

### フォント（厳守・再掲）
- `BIZ UDPMincho` は**ワードマーク専用**。見出し・番号・ボタン等に使わない。見出し＝`nx-display`（Cormorant+Shippori）、カード見出し・本文＝`Shippori`、ラベル・番号＝`Mono`。

### 図（凡例・矢印・面・アニメ）
- **凡例は最小化**。種別・戦略は**位置・矢印・エッジラベル**で読ませる（色＋別表に頼らない）。例：ノードが Uniswap↔Aave に矢印＝「裁定」、外から Aave に矢印＝「攻撃」。
- **矢印は塗りつぶし三角**（`<path d="M0,0 L7,3.5 L0,7 Z" fill="…"/>`）。開いた線＋round 端の“手書き風”矢じりは不可。
- **ノード／チップは不透明**に。`accent-soft` 等の半透明は背後の線が透ける → 不透明な淡色（例 `#e7ecf1`）を使う。
- **常時アニメ（パルス・点滅）で“アプリ UI”化しない**。CTA ボタンの脈動・ハイライト行の点滅は不可。落ち着いたトーンを保つ。

### 視線誘導・レイアウト
- 情報の羅列（facts 行＋チップ＋グリッド）を積み重ねない。**焦点（hero）を 1 つ**決め、補助は周辺に置く。
- 2 カラムは「**明確な階層がある場合のみ**」（左＝文脈カード／右＝本体タイムライン等、“人が読めるイベントページ”）。対等な 2×2 は不可。

### 解像度
- 抽象語より**具体の単位**で示す（「サービス＝GDP の 8 割」より産業別の実額）。数字は出典付き。

### 実ロゴの取得（運用）
ブランドロゴは Web から取得して `public/logos/` に置き、`<image href="/logos/…">` で配置する：

```bash
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
# 暗号資産系の SVG
curl -sL -A "$UA" -o public/logos/uniswap.svg https://cryptologos.cc/logos/uniswap-uni-logo.svg
# 取れない場合は公式ファビコン（PNG 128px）
curl -sL -o public/logos/polymarket.png "https://www.google.com/s2/favicons?domain=polymarket.com&sz=128"
```

色付きブランドロゴはライト地（`--bg`）でそのまま視認できる。名目的使用（プラットフォーム参照）の範囲で使う。

## 完了前チェックリスト

すべて通過するまで完了報告しない。

```bash
# 1. $ エスケープ残存ゼロ
grep -rI '\\\$' slides/ public/images/

# 2. 旧ブランド名残存ゼロ（廃止名は全削除し grep で確認）
grep -rI 'zktokyo\|zk tokyo\|zk-tokyo' slides/ public/images/ *.vue style.css

# 3. ビルド成功
bun run build

# 4. 全スライドを PNG 化して目視（オーバーフロー / 視線フロー / 出典 / コントラスト）
```

目視では：下端切れ等のオーバーフロー検出、視線フローが 1 軸か（2×2 になっていないか・焦点が 1 つか）、文字が読めるサイズ・コントラストか、出典の有無、を確認する。あわせて、**タイトルが 1 行か・煽り語/軍事メタファーが無いか／凡例に頼らず位置と矢印で読めるか／ノードが不透明か・矢印が塗り三角か／フォントがワードマーク専用 BIZ を見出しに流用していないか／用語がデッキ全体で一貫しているか**も確認する。

## ピットフォール（繰り返し禁止）

- 原稿・ソース（Notion 等）の全文貼り付け → 枚数膨張・運営情報混入。投影原則で絞る
- canvasWidth デフォルトのまま日本語密度過多
- 2×2 grid で視線迷子
- 集合関係を並列ボックスで描き重複発生（→ 入れ子図形）
- 数値・事件名を出典なしで提示
- 「休憩」等の運営スライドを単独 1 枚で作る
- 黒太枠の多用（→ `--line` 1px のハイラインのみ）
- 読めない極小・低コントラスト文字でムリに情報を詰める
- `BIZ UDPMincho` を見出し・番号に流用（→ ワードマーク専用）
- 凡例過多／色＋別表に依存（→ 位置・矢印・エッジラベルで読ませる）
- 半透明ノードで背後の線が透ける（→ 不透明な淡色）／開いた線の“手書き風”矢じり（→ 塗り三角）
- パルス・点滅の常時アニメで“アプリ UI”化
- 2 行に折り返す長いタイトル／煽り語・軍事メタファー（青天井・本丸・既成事実）／用語ゆれ（信用と信頼の混在）
