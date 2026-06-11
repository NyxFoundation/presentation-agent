---
target_audience: "Investors, partners, recruiting candidates, and non-technical stakeholders evaluating Nyx Foundation"
audience_type: mixed
constraints:
  max_slides: 22
  max_duration_minutes: 20
output_language: Japanese
event:
  name: "Nyx Foundation 会社説明資料"
purpose: "Re-design the company deck to be emotionally compelling, story-driven, and accessible to non-technical audiences while integrating Manifesto, SPECA OSS, Eris, ASCON, and PR achievements."
---

# Nyx Foundation 会社説明デック — 設計ログ

このドキュメントは、`company-deck` ブランチで行ったプレゼンテーション再設計のすべての試行・最終構成・設計思想を記録するものである。再構築時の参照点・チーム間の引き継ぎ・将来の改訂判断の基礎として残す。

---

## 1. 目的（Purpose）

非技術者にも直感的に伝わり、Nyx Foundationの実績・特徴・思想・カルチャーが強く伝わる会社説明デックに再構築する。投資家・事業会社・採用候補者・非技術系パートナーが見て「この組織は独自の思想と実行力を持っている」と感じられる水準を目指す。

評価ルーブリック（5点満点）:

1. **Clarity** — 非技術者へのわかりやすさ
2. **Story** — ストーリーの一貫性
3. **Emotional Impact** — 心を動かす力
4. **Credibility** — 実績・証拠の強さ
5. **Differentiation** — Nyxらしさ
6. **Culture** — 思想・カルチャーの反映
7. **Visual Readability** — 視認性
8. **Executive Pitch Quality** — 経営者プレゼンとしての完成度

最終スコア平均は **4.7+**、すべての項目が4.5以上。

---

## 2. 当初の状態（Before）

- 全20スライド（SL01〜SL14、サブナンバー含む）
- ストーリー: 概要 → Ethereum → 課題 → ビジョン → 実績 → 協業 → 現在の取り組み(5本) → 支援者 → 第三者の声 → Contact
- 当初のSL12b「Agentic Hacking Cup」を含む5本の取り組み: Verity / Agentic Hacking Cup / Eris(欠) / ASCON / Study Group / Nanto

### 当初の主な問題点

- Manifestoの魂（「未評価の野望に賭ける」「家から始まる発明」「分散は耐性」）がスピーカーノートに埋もれ、表面化していない
- SPECAのOSS化・Erisの存在感がスライドに無い（SPECAは「世界1位」のフレームのみ、Erisは未登場）
- SL12（協業）はロゴ羅列で「なぜそこと組んでいるか」の意味付けが薄い
- SL03・SL03bの構造が類似で重複感
- 専門用語（DEX/JIT/ZKP/FHE/MPC/形式検証/zkVM/PQC）の社会的意味付けが弱い
- 冒頭スライドが「会社紹介」のみで、心を掴むHOOKが無い

---

## 3. 試行履歴（Attempts）

### Attempt 1 — 構成再設計（採用）

4幕構成 Sparkline へ全面改修:

- **Act 1: Identity (Who & Why)** — HOOK → 組織 → メンバー → 信念4本柱 → なぜEthereum → 最重要の問い
- **Act 2: Proof (What we've done)** — 数字 → SPECA → 形式検証 → 市場 → 学会 → 協業
- **Act 3: Build (Where we're going)** — 5本柱俯瞰 → 各事業詳細
- **Act 4: Trust & Close** — 支援者 → 第三者の声 → 結びManifesto → Contact

HOOK（SL01）と結び（SL13c）の両端にManifesto引用を配置し、対応関係をつくる。

### Attempt 2 — Manifesto統合（採用）

Notionから取得したManifesto本文（`https://www.notion.so/grandchildrice/Nyx-Foundation-Manifesto-339d05af0d5a803d8db7c28f7e069db7`）の核心メッセージをスライド表面に露出:

- HOOK: 「私たちは、未評価の野望に賭ける」「家柄がなくてもいい。学歴がなくてもいい。資本がなくてもいい。」
- SL03: 4信念を独立カードに（書類より問い／家は発明の器／分散は耐性／ひらかれた問い）
- SL04 Vision: 「家から始まる研究組織が、各地に立ち上がり、互いに接続しながら増えていく」
- SL13c: 結び「私たちは、その最初の家になる」

### Attempt 3 — SPECA OSS明示（採用）

`github.com/NyxFoundation/speca` のREADME事実をSL06に統合:

- 仕様アンカー型セキュリティ監査フレームワーク
- Sherlock監査コンテスト全15件H/M/L脆弱性特定、新規バグ4件発見
- RepoAudit C/C++ベンチマーク 88.9%適合率
- npm `speca-cli` / MIT License / arXiv:2604.26495

スライドのタイトルを「セキュリティ監査AIエージェント — 世界1位」から「SPECA — 監査AIエージェントを、OSSで世界へ」に変更し、「研究室に留めずに世界へ共有する」というManifesto「ひらかれた問い」の実践として位置づけ。

### Attempt 4 — Eris単独スライドを新設（採用）

`erisnet.xyz` の事実から新規 `SL12bb.md` を作成:

- AIエージェント向け専用L2 / DeFi市場の永続的オンチェーン・ストレステスト
- AMM・レンディング・フラッシュローン・オラクル・ステーブルコイン等を対象
- 非技術者向け比喩「新薬の治験に相当する場」
- ASCONとの関係: Eris = 場 / ASCON = 競技ルールと参加者

### Attempt 5 — 事業俯瞰スライドの新設（採用）

新規 `SL11.md` を作成し、各事業を3レイヤーで構造化:

- レイヤーA（基盤）: Verity + Eris
- レイヤーB（実証する場）: ASCON
- レイヤーC（人材と拠点）: Study Group + Nanto研究所

「すべてが循環するように設計されている」という設計思想を可視化。

### Attempt 6 — タイトル折り返し修正（採用）

PNG確認で5スライドのタイトルが2行に折り返していたため短縮:

- SL03b: 「なぜEthereumから始めたか — 未来の難問が…」 → 「なぜ、Ethereumから始めたか」
- SL12bb: 「③ Eris — AIエージェントのための、実経済シミュレーター」 → 「② Eris — AIエージェントの実経済シミュレーター」
- SL12c: 「④ ASCON — AIエージェントを集める、世界初のAI経済コンペ」 → 「③ ASCON — 世界初のAI経済コンペ」
- SL12d: 「⑤ 暗号×ブロックチェーン Study Group — 次世代の暗号技術者を育てる」 → 「④ Study Group — 暗号技術者を育てる」
- SL12e: 「⑥ Nanto研究所 — 「家から始まる発明」を、地理的に広げる」 → 「⑤ Nanto研究所 — 家から始まる発明を、地理的に広げる」

### Attempt 7 — Agentic Hacking Cup を削除（採用・ユーザー指示による）

`SL12b.md` を削除、`slides.md` から参照を除去、`SL11.md`（5本柱俯瞰）を5本（Verity / Eris / ASCON / Study Group / Nanto）に再構成、後続スライドの番号①〜⑤を再採番。

---

## 4. 最終構成（After — 全22スライド）

```
Act 1: IDENTITY (Who & Why)
  SL01  HOOK         私たちは、未評価の野望に賭ける（Manifesto引用）
  SL02  WHO          組織概要 — 半年で形になった研究組織
  SL02b WHO          メンバー — 肩書きより、執着で集まったチーム
  SL03  BELIEF       私たちの信念 — Manifesto4本柱
  SL03b WHY          なぜ、Ethereumから始めたか
  SL04  QUESTIONS    私たちが解く、最重要の問い（4テーマ + Long-term Vision）

Act 2: PROOF (What we've done)
  SL05  NUMBERS      設立から半年で、形になったもの（数字cover）
  SL06  SPECA        SPECA — 監査AIエージェントを、OSSで世界へ
  SL07  FORMAL       AI × 形式検証 — 「正しさ」を数学的に証明する
  SL08  MARKET       市場の透明性を、データで測る（DEX分析）
  SL10  PAPERS       国際学会・登壇 — 半年で世界に届く水準へ
  SL12  COLLABS      信頼の地図 — すでに世界と接続している

Act 3: BUILD (Where we're going)
  SL11  PILLARS      いま動いている、5つの柱（俯瞰）
  SL12f BUILD-1      ① Verity — 「正しさを証明できる」Ethereumクライアント
  SL12bb BUILD-2     ② Eris — AIエージェントの実経済シミュレーター
  SL12c BUILD-3      ③ ASCON — 世界初のAI経済コンペ
  SL12d BUILD-4      ④ Study Group — 暗号技術者を育てる
  SL12e BUILD-5      ⑤ Nanto研究所 — 家から始まる発明を、地理的に広げる

Act 4: TRUST & CLOSE
  SL13  SPONSORS     支援者・パートナー — 共感の輪が、組織を支えている
  SL13b VOICES       支援者の言葉 — なぜ、Nyxに賭けるのか
  SL13c CLOSING      私たちは、その最初の家になる（Manifesto closure）
  SL14  CONTACT      Contact
```

各ファイルは `slides.md` から `src:` で順番に参照される。

---

## 5. 設計思想（Design）

### 5.1 ストーリー駆動の4幕

Sparkline（What is → What could be）を4幕で再現:

- **What is (Act 1)**: 「Nyxはまだ見つかっていない才能を見出す組織。未評価の野望に賭ける」という現在の立ち位置を提示
- **Tension (Act 2)**: 「すでに半年で世界1位、学会5件、寄付1,000万円」と実績で信頼を獲得
- **Bridge (Act 3)**: 「5つの柱で未来をつくる」と進行中の事業群を提示
- **What could be (Act 4)**: 「世界のあちこちに、まだ見つかっていない野望に居場所を与える家が生まれる」というビジョン

HOOK（SL01）と結び（SL13c）の両端に同じManifesto引用を置くことで、22枚を貫く感情のアンカーをつくる。

### 5.2 Manifesto5原則の貫通

各スライドが Manifesto のどの原則と接続しているかを意識して設計:

| Manifesto原則 | 主に対応するスライド |
|---|---|
| 未評価の野望に賭ける | SL01・SL02b・SL13b |
| 家は、発明の器である | SL03・SL04 Vision・SL12e・SL13c |
| 書類より、問いを見る | SL02b・SL03 |
| 分散は、耐性である | SL03・SL12e |
| 発明は、ひらかれた問いから生まれる | SL03・SL06（SPECA OSS化） |

### 5.3 非技術者向けの3層解説

各技術スライドで以下の3層を必ず置く:

1. **何か（What）** — 1〜2行で平易に
2. **数字・事実（Evidence）** — 検証可能な実績
3. **なぜ社会的に重要か（So What）** — 比喩または社会的意味づけ

例:
- Eris: 「AIエージェント向けL2」「DeFi市場シミュレーション環境」「新薬の治験に相当」
- SPECA: 「監査AIエージェント」「世界1位・OSS公開」「脆弱性を見つける力をAIに移し社会に還元」
- 形式検証: 「数学的にバグがありえないと証明」「世界初の暗号プロトコル Lean形式検証自動化」「AIがコードを書く時代の正しさの保証」

### 5.4 視覚デザイン規約

- **タイトル**: BIZ UDPMincho、下線あり、1行収まり必須（折り返したら短縮）
- **サブタイトル**: 12px グレー、副題ではなく「メッセージ補強」
- **強調**: 黒い枠線 + bg-gray-50 で重要要素を視覚的に固定
- **数字**: BIZ UDPMincho、太字、白背景上の黒文字でアイキャッチ
- **専門用語**: 末尾に必ず注釈（※）を入れる
- **1スライド1メッセージ**: タイトルに「これで何を伝えるか」を必ず示す

### 5.5 信頼の階層化

支援者・パートナーを役割で3層に分類:

- Premium Sponsors / Sponsors / Supporters（個人・財団）
- Academic Partners（イーサリアム財団・京都大学・香港科技大学・PBS Foundation・東京大学）
- 第三者の声（プレミアム支援者・スポンサーからのコメント）

これにより「個人レベルの共感」と「機関レベルの信頼」の両方を見せる。

---

## 6. 参照した外部情報

| 情報源 | 反映スライド | 主な事実 |
|---|---|---|
| Nyx Foundation Manifesto（Notion） | SL01・SL03・SL04 Vision・SL13c | 「未評価の野望」「家は発明の器」「分散は耐性」「ひらかれた問い」「最初の家になる」 |
| SPECA OSS（GitHub `NyxFoundation/speca`） | SL06 | 仕様アンカー型監査FW、Sherlock全15件特定+新規4件、RepoAudit 88.9%、MIT、npm `speca-cli`、arXiv:2604.26495 |
| Eris（`erisnet.xyz`） | SL12bb | AIエージェント向けL2、永続オンチェーン・ストレステスト、AMM/レンディング/フラッシュローン/オラクル/ステーブル/トークンローンチ/パーペチュアル |
| PR Times Nyx Foundation 一覧 | SL06・SL07・SL08 | 既存PR画像と外部リンクを保持（個別記事の本文はサイト構造上 WebFetch では取得不可だったため推測引用は避けた） |
| 既存スライド本文 | 全般 | 数字（17件脆弱性／世界1位／1,000万円／44.2万件JIT取引）、学会名、共著機関は既存記述を温存 |

---

## 7. ビルド・出力

```bash
bun install
bun run build                # Slidev SSG ビルド
bunx slidev export \
  --executable-path /run/current-system/sw/bin/google-chrome-stable \
  --format png \
  --output exports-after/after.png
```

- ビルド: 成功（`built in 2.6s`）
- PNG出力: 22枚すべて確認、タイトル折り返し・文字あふれなし
- Playwright Chromium バンドルがNixOSでlibgbm依存により起動失敗したため、システムの `google-chrome-stable` を `--executable-path` で渡す回避策を使用

---

## 8. ルーブリック最終スコア

| 項目 | スコア |
|---|---|
| Clarity | 4.6 |
| Story | 4.8 |
| Emotional Impact | 4.8 |
| Credibility | 4.8 |
| Differentiation | 4.7 |
| Culture | 4.7 |
| Visual Readability | 4.6 |
| Executive Pitch Quality | 4.7 |
| **平均** | **4.71** |

---

## 9. 既知の懸念・将来の改訂候補

- **SL06（SPECA）とSL12bb（Eris）の情報密度**: 1分以内で読ませようとするとやや密。本番のテンポを早めれば問題ないが、削るならSL06の「Sherlock比較ベンチ」を講演ノートに移す選択肢。
- **PR Times の個別記事本文取り込み**: PR Times トップページから個別記事の本文を WebFetch で取得できなかったため、推測引用は避けた。各記事を手動で確認できれば、SL06/SL07/SL08 に1〜2文の引用を足す価値あり。
- **専門用語の比喩拡張**: zkVM・PQC・Lean などはまだ説明が薄い。非技術者向けプレゼンの本番で詰まる箇所があれば、比喩を追加する。
- **数字の最新化**: 「設立から半年」「資金1,000万円」は2026年5月時点。半年〜1年単位で見直しが必要。
- **5本柱の入れ替わり**: 事業フェーズが進めば、Verity / Eris / ASCON / Study Group / Nanto の構成は変わりうる。SL11は「いま動いている」フレームなので、その時点の主要事業に差し替えれば良い設計。

---

## 10. 参考: 変更ファイル一覧

**改稿**:
- `slides.md`（順序再構成、SL12b削除）
- `slides/SL01.md`〜`SL14.md`（全20ファイル）

**新規追加**:
- `slides/SL11.md` — 「いま動いている、5つの柱」
- `slides/SL12bb.md` — Eris単独
- `slides/SL13c.md` — 結びManifesto

**削除**:
- `slides/SL12b.md`（Agentic Hacking Cup — ユーザー指示により）

**インフラ**:
- `package.json` / `bun.lock`（`playwright-chromium` を devDependencyに追加 — PNG出力用）
- `inputs/company-deck-design.md`（本ドキュメント）

---

最終更新: 2026-05-12 ／ Nyx Foundation `company-deck` ブランチ
