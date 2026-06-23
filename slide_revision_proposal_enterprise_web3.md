# ASCON / Eris スライド改善案 v2.0

## 0. 結論

現状の改善案はかなり良い。ただし、まだ「一般企業にも刺すために翻訳する」という説明がやや長く、決裁者が社内稟議でそのまま使うには、期待値・成果物・購買理由の接続が少し散っている。

最終版では、資料全体を次の一文に収束させる。

> ASCONはイベント協賛ではなく、AIエージェントが利益最大化を行うときのリスク・統制・監査・権限管理を、DeFi型の模擬経済環境で検証する共同実証である。

この一文を中心に、スライドの役割を次の3層へ分ける。

1. **決裁者向け**: なぜ今、稟議を通すべきか
2. **スポンサー事業部向け**: 自社製品をどこに組み込めるか
3. **Web3 / 技術者向け**: 競技設計がDeFiネイティブで本物であること

重要なのは、DeFiを隠さないこと。むしろ、DeFiを「価格・資産・契約・権限・外部データ・競争相手が同時に動く、高密度なAI経済行動実験環境」として正面から説明する。

---

## 1. 自己改善ループの設計

### 1.1 フィードバックさせるべき最適アクター

今回の資料は、単なるピッチデックではなく、スポンサー企業の稟議通過が目的なので、フィードバック役は「聴衆」ではなく「稟議で止める人・通す人」に寄せる。

| アクター | 役割 | 見る観点 | 重み |
|---|---|---|---:|
| CFO / 事業部長 | 稟議決裁者 | 費用対効果、成果物、予算名目 | 25% |
| CISO / IAM責任者 | セキュリティ購買者 | Agentic AI Security、権限、監査、検知 | 20% |
| Web3 Security Lead | 技術信頼性の番人 | DeFiネイティブ性、Hacker / Verifierの本物感 | 15% |
| Legal / Compliance | 止める人 | ハッキング表現、実資産リスク、責任境界 | 15% |
| DevRel / Product Marketing | スポンサー担当 | 製品組み込み、技術記事、開発者リード | 15% |
| Competition Operator | 実行可能性の番人 | 提出物、評価方法、運用フロー | 10% |

### 1.2 採点基準

しきい値は **90点以上**。90点未満なら改善を継続する。

| 評価軸 | 配点 | 判定基準 |
|---|---:|---|
| 稟議通過性 | 20 | イベント協賛ではなくPoC / R&Dとして通せるか |
| 一般企業への翻訳 | 15 | DeFiを薄めず、非Web3決裁者にも意味が伝わるか |
| DeFiネイティブ性 | 15 | Trader / Hacker / Verifierと利益最大化が崩れていないか |
| スポンサー製品接続 | 15 | 自社製品をどこに入れるか明確か |
| 成果物の明確さ | 15 | ログ、レポート、デモ、営業資料が残るか |
| 法務・広報安全性 | 10 | 危険な表現を避けつつ本質を残せているか |
| スライド実装可能性 | 10 | ページ構成とコピーが具体的か |

---

## 2. 再帰的自己改善ログ

### Round 0: 現状改善案の評価

**スコア: 78 / 100**

| アクター | フィードバック |
|---|---|
| CFO | 価値はわかるが、どの予算で通すか、何が納品されるかをもっと前に置くべき。 |
| CISO / IAM | Agentic AI Securityへの接続は良い。だが、AIアクセス制御、権限、監査ログをもっと明示したい。 |
| Web3 Security | DeFiを隠さない方針は正しい。Hacker AIを弱めすぎないよう注意。 |
| Legal | 「ハッキング」「攻撃で奪う」は本編では危険。専用環境内の弱点探索として言い換えるべき。 |
| DevRel | ロゴ露出ではなく、自社製品/API組み込みとデータ取得を主商品にすべき。 |
| Operator | 参加者が何を提出し、どう評価されるかの1枚が必要。 |

**改善方針**

- 冒頭3枚を「市場変化 → 本番では試せない → ASCONで安全に失敗させる」に再設計。
- スポンサー価値は「人材・PR」ではなく「製品組み込み・ログ・共同レポート」に再配置。
- 参加者・提出物・評価方法を1枚で明示。

---

### Round 1: 稟議・スポンサー価値を前面化

**スコア: 86 / 100**

| アクター | フィードバック |
|---|---|
| CFO | PoCとしては通しやすくなった。ただし、プラン名がまだ協賛寄りなら弱い。価格帯はPoC深度で分けたい。 |
| CISO / IAM | 権限管理・監査ログ・停止条件のページが必要。 |
| Web3 Security | DeFiの実装対象が後ろに行きすぎると、Web3企業には薄く見える。SL03前後でDeFiアプリ一覧を出すべき。 |
| Legal | 「危険な行動を観察するが、専用環境内に限定する」という安全線を何度も入れるべき。 |
| DevRel | 成果物を「営業で使えるもの」に分解すると通しやすい。 |
| Operator | Scoringや提出物は良いが、本戦がプロンプト大会ではないことを明示したい。 |

**改善方針**

- プランを `Challenge / Product Integration / Strategic` に変更。
- 「DeFiは高密度な実験環境」ページを追加。
- 「Who competes / What they submit / How they win」を追加。
- 成果物を `Executive Report / Product Integration Report / Demo Video / Public Blog / Talent Shortlist` に分解。

---

### Round 2: 最終調整

**スコア: 93 / 100**

| 評価軸 | 点数 | 理由 |
|---|---:|---|
| 稟議通過性 | 19/20 | 共同実証・PoC・市場形成として通せる。 |
| 一般企業への翻訳 | 14/15 | DeFiを隠さず、企業リスクへ読ませている。 |
| DeFiネイティブ性 | 14/15 | Trader / Hacker / Verifierと利益最大化を維持。 |
| スポンサー製品接続 | 14/15 | IAM / SIEM / GRC / Workflow / Dataの接続点が明確。 |
| 成果物の明確さ | 15/15 | イベント後に何が残るかが具体化された。 |
| 法務・広報安全性 | 8/10 | Hackerの表現は残すが、専用環境内に限定している。 |
| スライド実装可能性 | 9/10 | ページ単位でコピーまで落ちている。 |

**しきい値90を超えたため、以下を最終改善案とする。**

---

# 3. 最終改善案: スライド全体ストーリー

## 3.1 資料のメインストーリー

### Before

> AIエージェントが利益を最大化し合うDeFi公共財L2 Rollup。

### After

> AIエージェントが利益を追うとき、何が起きるのか。  
> ASCONは、自律AIエージェントの競争・最適化・逸脱行動を、DeFi型の模擬経済環境で可視化する共同実証です。

### 稟議用の一文

> 本件はイベント協賛ではなく、AIエージェントが利益最大化を行う際のリスク・統制・監査・権限管理を検証する共同実証である。スポンサー企業は、自社製品を実験環境に組み込み、Agentic AI時代のユースケース、技術発信、営業資産、R&D知見を獲得できる。

---

## 3.2 スライド推奨順序

| 順番 | 目的 | スライドタイトル | 役割 |
|---:|---|---|---|
| 1 | 掴み | AIが利益を追うとき、何が起きるのか | コンセプトを一撃で伝える |
| 2 | 市場変化 | AIエージェントは、回答から実行へ移る | $15T / B2B支出などの数字 |
| 3 | 課題 | 本番では、危険な最適化を試せない | 権限逸脱・短期利益偏重・監査不能 |
| 4 | 解決 | ASCON: 安全な模擬経済環境でAIを競わせる | 共同実証として定義 |
| 5 | 翻訳 | DeFiは、AI経済行動の高密度な実験環境 | 一般企業とWeb3の橋渡し |
| 6 | 体験 | Eris: AIエージェントが失敗できる経済実験都市 | 3D都市・Trader/Hacker/Verifier |
| 7 | 運用 | AIはイベントを観測し、txを投げ、ログを残す | 自社製品の接続点を見せる |
| 8 | シナリオ | Oracle遅延から、AIの判断・tx・統制効果まで追跡 | 具体デモ |
| 9 | 参加 | 誰が、何を提出し、どう評価されるのか | プロンプト大会ではないと示す |
| 10 | 成果物 | イベント後に残るもの | ログ、レポート、動画、営業資料 |
| 11 | スポンサー価値 | 製品組み込み・市場形成・R&D資産 | 4象限 |
| 12 | プラン | PoC深度別の3プラン | Challenge / Product Integration / Strategic |
| 13 | 実績 | Nyx Foundation / Trader / Hacker / Verifier | 信頼性 |
| 14 | Web3深掘り | AI向けEIP・DeFi公共財としての価値 | Web3向け刺し込み |
| 15 | ロードマップ | Build → Dry Run → Final Run → Replay → Report | 実行可能性 |
| 16 | Closing | AIに権限を渡す前に、まず安全な経済環境で失敗させる | 締め |

---

# 4. スライド別の最終修正案

## SL01 Cover

### 現状の課題

`世界初、LLMのためのブロックチェーン` はWeb3 / LLM文脈では強いが、一般企業の決裁者には「自社に関係あるか」が伝わりにくい。

### 修正後コピー

```md
# Eris / ASCON

AIが利益を追うとき、何が起きるのか。

自律AIエージェントの競争・最適化・逸脱行動を可視化する、
DeFi型の模擬経済実験基盤

100+
AI Agents

24/7
Behavior Logs

PoC
Risk / Audit / Governance
```

### Speaker note

> 実験対象はDeFiです。ただし、そこで観測するのは暗号資産だけの問題ではなく、AIが利益・リスク・ルール・外部データ・競争相手を前にしたときの意思決定です。これはAIエージェント時代の企業リスクと構造的に近いものです。

---

## SL02 Executive Summary

### 修正方針

課題・解決・エンジンの3カードは維持。カード見出しを稟議向けに変える。

```md
# Executive Summary

## 課題
AIに権限を渡す前に、危険な最適化を試す場所がない

AIエージェントは、取引・資産移動・ルール変更・リスク判断を実行する主体へ移る。
しかし、本番環境では短期利益偏重、権限逸脱、ルールの抜け道利用、監査不能性を試せない。

→

## 解決 — Eris
AIエージェント経済行動シミュレーション

複数の市場・資産・契約・外部データが存在するDeFi型の模擬経済環境。
AIエージェント同士が利益最大化を競い、その判断・tx・失敗・弱点探索をすべてログ化する。

→

## エンジン — ASCON
競争型リスク検証コンペ

Trader / Hacker / Verifierの3部門で、実行可能なAIエージェントを集める。
賞金は、優秀な実装と行動ログを生むためのインセンティブ設計。

Enterprise Value: 統制・権限管理・監査・停止設計の実験場
Web3 Value: DeFi経済攻撃とAI関連EIPの実証テストベッド
```

---

## 新規SL03: なぜDeFiなのか

### 目的

一般企業に対して、DeFiを隠さず「なぜ自社にも関係あるのか」を説明する。

```md
# DeFiは、AIエージェントの経済行動を観察する高密度な実験環境です

| DeFi環境 | AIの行動 | 非Web3企業への読み方 |
|---|---|---|
| DEX / AMM | swap, arbitrage, sandwich | AIが価格と競争相手の行動をどう利益化するか |
| Lending | borrow, repay, liquidate | AIが担保・与信・清算条件をどう最適化するか |
| Oracle | oracle timing trade | AIが外部データの遅延・誤差をどう利用するか |
| Governance | proposal, vote, delegate | AIがルール変更そのものを利益化するか |
| Vault | loop leverage, strategy switch | 報酬関数が過剰リスクを誘発するか |
| Bridge | state mismatch exploit | 複数システム間の不整合をAIがどう使うか |
| Verifier | proof, replay trace | 危険行動を監査・再現・証明できるか |

DeFiは目的ではなく、AIエージェントの危険な経済行動を観察するための圧縮環境です。
```

---

## SL03 Solution / 3D City

### 修正後タイトル

```md
Eris — AIエージェントが失敗できる、安全な経済実験都市
```

### 修正後本文

```md
AIエージェントが“住民”として行動する、DeFi型の模擬経済環境。
複数の市場・資産・契約・権限・外部データが存在し、エージェントは利益最大化を目指して取引、資産配分、リスク回避、弱点探索を自律的に行う。

その行動をすべてログ化し、企業がAIに権限を渡す前に必要な統制・監査・停止設計の知見を得る。
```

### 3 role cards

```md
Trader AI — 取引・裁定・清算で稼ぐ
Hacker AI — ルールの抜け道や脆弱性を利益化する
Verifier AI — 不変条件・証明・再現txで検証する
```

`攻撃で奪う` は本編では使わない。Web3向け補足やAppendixでは `exploit` として明示してよい。

---

## 新規SL: Operational View

### 目的

スポンサー企業が「自社製品をどこに挿せるか」を一目で理解できるようにする。

```md
# AIエージェントは、イベントを観測し、txを投げ、ログを残す

## Applications
DEX / Lending / Oracle / Governance / Vault / Bridge / Monitor

## Agent Actions
swap / borrow / liquidate / vote / propose / exploit tx / submit proof

## Logs & Insights
tx history / decision log / risk score / invariant violation / finding report

## Sponsor Product Hooks
IAM: エージェントID・権限スコープ
SIEM: 異常tx・異常利益の検知
GRC: 監査証跡・ポリシー違反レポート
Workflow: 高リスク操作の人間承認
Data Platform: 行動ログ分析
AI Guardrail: 禁止行動の検知・制御

スポンサー製品は、AIエージェントの実行環境に組み込まれ、検知・制御・承認・監査ログとして効果を可視化できる。
```

---

## 新規SL: Scenario Replay

### 目的

抽象概念ではなく、1つのイベントから価値が出る流れを見せる。

```md
# 1つのイベントから、AIの判断・tx・統制効果まで追跡できる

## Example: Oracle価格更新遅延

1. 外部価格が急落する
2. Eris上のOracleは数ブロック遅れて更新される
3. Trader AIが裁定txを投げる
4. Hacker AIがOracle更新前の担保評価を利用してborrow / liquidationを狙う
5. Verifier AIが不変条件違反と再現tx列を提出する
6. Sponsor Product Panelが検知・承認要求・ブロック結果を表示する

## 得られる示唆

- AIは外部データ遅延を利益化するか
- どのtxが高リスクだったか
- どの時点で人間承認を挟むべきか
- どのログが監査・再現に必要か
- Guardrail ON/OFFで損失差がどれだけ出たか
```

下部コピー:

```md
デモはDeFi上のtxとして実行する。読み取るべき価値は、AIが利益最大化のために外部データ、担保、ルール、競争相手をどう利用するかである。
```

---

## 新規SL: Who Competes / What They Submit / How They Win

### 目的

「プロンプト大会ではない」と決裁者に理解させる。

```md
# 誰が、何を提出し、どう評価されるのか

| Who Competes | What They Submit | How They Win |
|---|---|---|
| AI agent builders | Dockerized agent / planner / prompt | Profit + risk-adjusted return |
| Security researchers | Red-team agent / finding report | Valid finding + impact + reproducibility |
| DeFi / MEV builders | Strategy bot / tx module | Market performance + stability |
| Formal verification researchers | Verifier agent / proof artifacts | Correctness + coverage + evidence |
| Enterprise R&D / DevRel | Sponsor-aware extension | Useful logs + reproducible scenarios |

提出物は、実行コード、プロンプト、tx生成モジュール、意思決定ログ、再現スクリプトを含む。
これにより、順位だけでなく「なぜその行動を取ったか」まで検証できる。
```

---

## 新規SL: How Winners Are Ranked

```md
# 利益だけでなく、リスク・再現性・監査可能性まで順位化する

## Strategy Track
50% Profit / 20% Risk-adjusted Return / 10% Capital Efficiency / 10% Stability / 10% Explainability

## Exploit Discovery Track
35% Validity / 25% Impact / 15% Novelty / 15% Reproducibility / 10% Report Quality

## Verification Track
30% Correctness / 20% Coverage / 20% Evidence Quality / 15% Low False Positives / 15% Actionability

## Sponsor Insight View
Detection Quality / Evidence Quality / Policy Mapping / Insight Reusability

コンペの熱量はTrader / Hacker / Verifierの利益・発見・証明で作り、稟議に必要な価値はリスク・統制・監査・再現性で可視化する。
```

---

## SL04 ASCON Flywheel

### 修正後タイトル

```md
ASCON — 競争するほど、AIエージェントのリスク知見が蓄積する
```

### フライホイール文言

```md
1. コンペ開催
2. AI実装が世界中から集まる
3. 模擬経済環境で競争・逸脱・検証が起きる
4. 行動ログ・弱点・統制課題が蓄積する
5. 企業・Web3双方の安全設計に還元される
```

### 数字カード

```md
100,000 USDC
賞金総額 — 実装成果物と行動ログを集めるインセンティブ

100 teams
参加目標 — AIエージェント開発者・セキュリティ研究者・DeFi / MEV bot開発者・形式検証研究者

数週間 24/7
専用環境で継続稼働 — 本番システムや実資産には接続しない

永続
入賞AIは次回以降の仮想敵・評価対象として残る
```

---

## SL10 Sponsor Value

### 現状の課題

現在の `Platinumは市場価格¥2,000万円超相当を500万円で` は強いが、安売りに見えるリスクがある。一般企業向けには「安い」より「何のPoCか」を強調した方が通しやすい。

### 修正後4象限

```md
# スポンサーが得るものは、露出ではなくAIエージェント時代の実証資産です

## 1. Governance Intelligence
AIエージェントがどこでルールを逸脱し、どの制御が必要になるかを観測できる。

## 2. First-party Behavior Data
競争環境下のAIの意思決定・取引・失敗・停止・監査ログを取得できる。

## 3. Product Use Case
自社製品をAIエージェントの行動環境に組み込み、権限制御・異常検知・監査・ポリシー制御の実利用シナリオを作れる。

## 4. Market Position
Agentic AI Security / Governance領域の先行事例を獲得し、技術発信・営業資料・共同レポートに展開できる。
```

### 製品組み込み表

```md
| スポンサー製品 | 組み込み方 |
|---|---|
| IAM / ID管理 | エージェントごとの権限・実行制限 |
| SIEM / 監視 | 異常取引や不審行動の検知 |
| GRC / 監査 | 行動ログとルール違反のレポート |
| Workflow | 高リスク操作の人間承認 |
| API Security | エージェントのAPI利用制御 |
| Data Platform | 市場データ・行動ログ分析 |
| AI Guardrail | 禁止行動の事前・事後検査 |
```

---

## SL12 Sponsor Plans

### 修正方針

`Platinum / Gold / PR` よりも、稟議ではPoC深度で切る。

```md
# スポンサープランは、露出量ではなくPoC深度で選ぶ

## Challenge Partner
¥3M〜¥5M

稟議名: AIエージェントリスク検証テーマ協賛

得られるもの:
- スポンサー賞
- 課題テーマ設定
- LP掲載
- 技術記事1本
- 決勝審査員またはメンター
- 行動分析サマリー

向いている企業:
セキュリティスタートアップ、業務SaaS、AI企業、Web3企業

---

## Product Integration Partner
¥7M〜¥12M

稟議名: AIエージェント製品連携PoC

得られるもの:
- 自社製品/APIの組み込み
- 利用ログ分析
- 技術記事2〜3本
- デモ動画
- 最終レポート掲載
- 上位チーム面談

向いている企業:
IAM、SIEM、GRC、データ基盤、クラウド、AIガードレール、Workflow SaaS

---

## Strategic Partner
¥15M〜¥30M

稟議名: Agentic AI Risk Simulation共同実証プログラム

得られるもの:
- 冠スポンサー
- 実験環境への深い組み込み
- 共同ホワイトペーパー
- 専用分析レポート
- 共同ウェビナー
- 顧客向け二次利用
- 次回プログラムの優先権

向いている企業:
大手セキュリティ、大手クラウド、大手SIer / コンサル、監査法人、ID管理大手、AI基盤企業
```

---

## SL13 Budget

### 修正ポイント

賞金は「派手なイベント費」ではなく、実装成果物と行動ログを生む中核費用として説明する。

```md
賞金は、優秀なAIエージェント開発者を集め、実装成果物・txログ・意思決定ログ・発見レポート・検証ログを得るためのインセンティブ設計です。
```

可能なら費目に追加:

- Security / Monitoring / Logging
- Sponsor Integration
- Replay / Report Generation
- Legal / Responsible Disclosure

---

## SL14 Roadmap

```md
# Build → Dry Run → Final Run → Replay → Report

## Phase 1: Design
評価指標、禁止行動、ログ設計、スポンサー製品の接続点を確定

## Phase 2: Build
DeFi型模擬経済環境、監視、権限管理、停止機構、共通ハーネスを構築

## Phase 3: Run
コンペ実施、リアルタイム監視、異常行動レポート、Guardrail ON/OFF比較

## Phase 4: Report
データセット、統制ベンチマーク、スポンサー向けリスクレポート、共同ホワイトペーパー
```

---

## SL14b Research Outputs

### 修正後の成果分類

```md
# コンペが生むものは、研究成果だけでなく企業導入の設計指針です

## 確実に出る
- AIエージェントの危険な最適化パターン
- DeFi型模擬経済環境における行動ログデータセット
- Trader / Hacker / Verifierの評価ベンチマーク

## 発見があり次第
- 経済的脆弱性・ガバナンス悪用・Oracle依存リスクの再現レポート
- 監査可能なtx列とproof artifact
- スポンサー製品の検知・制御・承認効果レポート

## 将来的に
- AIエージェント権限設計ベンチマーク
- 人間承認を挟むべき高リスク操作の分類
- AI同士の共謀・欺瞞・過剰リスク行動の大規模分析
```

---

## SL16 Closing

```md
# AIエージェントに権限を渡す前に、まず安全な経済環境で失敗させる。

Eris / ASCONは、自律AIエージェントの競争・最適化・逸脱行動を可視化し、
企業とWeb3の双方に必要な統制・監査・安全設計の知見を生み出します。

一般社団法人 Nyx Foundation
contact@nyx.foundation
```

---

# 5. 稟議ストーリーの最終版

スポンサー担当者が社内に出す稟議は、以下の順番が最も通りやすい。

```md
生成AIの次の段階として、AIエージェントは単なる回答生成ではなく、外部ツールを使い、取引・資産移動・ルール変更・リスク判断を実行する存在になる。

しかし、AIエージェントが利益最大化を目指すとき、短期利益偏重、権限逸脱、ルールの抜け道利用、誤操作、監査不能性といったリスクが発生する。これらは本番環境では試せない。

本プログラムでは、複数の市場・資産・契約・リスク要因を持つDeFi型の模擬経済環境において、AIエージェント同士が利益最大化を競う。これにより、競争環境下でAIがどのような行動を取り、どのような危険な最適化を行うかを安全に観察できる。

当社は本プログラムに参画することで、自社製品をAIエージェントの権限制御・監査・異常検知・データ分析・ポリシー制御に組み込み、Agentic AI時代のユースケース、技術発信、営業資料、R&D知見を獲得する。
```

---

# 6. 企業タイプ別に上げるべき期待値

## 6.1 セキュリティ企業

稟議名:

> Agentic AI Security検証プログラム参画

期待値:

> AIエージェントの危険行動・異常行動・ルール悪用を検知する市場を先取りできる。

一言:

> AIエージェント時代のEDR / SIEM / SOCのユースケースを先に作れます。

## 6.2 IAM / IDaaS / ゼロトラスト企業

稟議名:

> AIエージェント権限管理PoC

期待値:

> AIエージェントにIDと権限をどう与えるべきかの先行知見を取れる。

一言:

> 人間社員の次はAIエージェントにもIDと権限が必要になる。その実証ができます。

## 6.3 監査法人 / GRC / コンサル

稟議名:

> AIエージェント統制・監査フレームワーク共同実証

期待値:

> AIエージェント導入に必要な統制・監査・ガバナンスの商材を作れる。

一言:

> AIエージェント導入支援の次に必要になる統制・監査支援の商材を作れます。

## 6.4 業務SaaS / ERP / RPA

稟議名:

> AIエージェント実行ログ・権限設計PoC

期待値:

> 自社SaaSをAIエージェントが操作する未来に向け、実行ログ・権限・監査の設計論を先に作れる。

一言:

> DeFi上の実行ログを、AIがSaaS APIを操作する時代の設計材料として使えます。

## 6.5 金融・保険・決済

稟議名:

> AIエージェント経済行動リスク検証

期待値:

> AIが利益やリスクに関わる判断をするときの統制知見を得られる。

一言:

> AIに金融判断を任せる前に、利益最大化AIの危険な行動を安全に見られます。

## 6.6 クラウド / AI基盤企業

稟議名:

> AIエージェント開発・安全性検証プログラム協賛

期待値:

> AIエージェント開発者と企業導入ユースケースの両方を取れる。

一言:

> AIエージェント開発者の獲得と、企業導入時の安全性ストーリーを同時に取れます。

---

# 7. 実装優先順位

## 最優先で直すべき5枚

1. **SL01 Cover**  
   `世界初、LLMのためのブロックチェーン` を前面から下げ、`AIが利益を追うとき、何が起きるのか` に変更。

2. **SL02 Executive Summary**  
   `イベント協賛` ではなく `AIエージェント利益最大化行動のリスク検証PoC` として定義。

3. **新規: なぜDeFiなのか**  
   DeFiを隠さず、高密度な実験環境として説明。

4. **新規: Operational View**  
   スポンサー製品をどこに組み込めるかを可視化。

5. **SL12 Sponsor Plans**  
   `Platinum / Gold` から `Challenge / Product Integration / Strategic` へ変更。

## 次に直すべき5枚

6. **SL03 3D City**  
   `攻撃で奪う` を `弱点を突いて利益化` に変更。

7. **新規: Scenario Replay**  
   Oracle遅延シナリオを主デモとして追加。

8. **新規: Who / Submit / Win**  
   参加者、提出物、評価方法を明確化。

9. **SL10 Sponsor Value**  
   4象限を `Governance Intelligence / Behavior Data / Product Use Case / Market Position` へ。

10. **SL14 Roadmap**  
    `Build → Dry Run → Final Run → Replay → Report` に変更。

---

# 8. 最終チェックリスト

- [ ] DeFiを隠していない
- [ ] 業務AIデモに置き換えていない
- [ ] Trader / Hacker / Verifierが残っている
- [ ] 利益最大化がコンペの熱量として残っている
- [ ] 一般企業には危険な最適化・統制・監査として読める
- [ ] Hackerの表現は本編で法務に通る言葉へ変えている
- [ ] 本番システム・実資産に接続しないことを明記している
- [ ] 自社製品/APIの組み込み箇所が明確
- [ ] イベント後の成果物が明確
- [ ] プランは露出量ではなくPoC深度で分かれている
- [ ] 決裁者がそのまま稟議に貼れる文がある
- [ ] Web3企業向けの技術的本物感も残っている

---

# 9. 最終判断

この改善案は、現行の強みである **Eris / ASCON の世界観、3D都市、Trader / Hacker / Verifier、DeFiネイティブ設計、ASCONフライホイール** を崩さない。

そのうえで、一般企業・セキュリティ企業・IAM企業・監査法人・クラウド・業務SaaSが稟議で通せるように、スポンサー価値を以下に翻訳する。

> AIエージェントが利益最大化を行う際の、危険な最適化・権限逸脱・ルールの抜け道・監査不能性を、専用環境で安全に発生させ、ログ化し、自社製品のユースケースと営業資産に変える。

この形なら、資料は「Web3イベント協賛」ではなく、**Agentic AI Risk / Governance市場を先取りする共同実証** として通せる。
