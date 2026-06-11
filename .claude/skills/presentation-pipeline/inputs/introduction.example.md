---
target_audience: "Advanced Cryptography Program Week 1 受講者 (オンサイト20-25名 / 学部生〜社会人エンジニア混在 / バックグラウンドにばらつきあり)"
audience_type: group
constraints:
  max_slides: 30
  max_duration_minutes: 120
output_language: Japanese
event:
  name: "Advanced Cryptography Program — Week 1"
  parent_event: "Merkle Japan × 東京大学ブロックチェーンイノベーション寄付講座"
  date: "2026 年度"
  location: "東京大学 講義室 (オンサイト)"
---

# Advanced Cryptography Program — Week 1: Programmable Cryptography Overview

担当: gohan
構成: 2 時間講義 + 30 分休憩 + 3 時間ホワイトボードセッション
形式: オンサイト、20-25 名想定

> 出典: Notion 教材管理 / Merkle Japan / Week1 ページ (`https://www.notion.so/grandchildrice/Week1-359d05af0d5a806196bfc4795f766f10`)

---

## 学習成果 (Learning Outcomes)

Week 1 終了時に、受講者は以下ができるようになる:

1. AI 時代に最先端暗号が社会的に必要になっている理由を、2025-2026 年の事例 3 つ以上で説明できる
2. ZK / MPC / FHE を敵対モデル・信頼前提・用途で区別できる
3. Sumcheck 系 SNARKs (Jolt) と Longfellow を 2026 年の代表的革新として認識し、その意義を述べられる
4. サービス設計の 4 つの問い (何を守る/誰が計算/いつ/誰が検証) を任意のサービスに適用できる
5. 自分のプロジェクトに関連する実装上の罠を 3 つ以上特定できる
6. KelpDAO×LayerZero $292M exploit をシステムレベルで分析し、オフチェーン構成要素に分解できる
7. 実世界の事件に対する暗号的再設計案を作り、技術選択を正当化できる
8. 他グループの設計を評価し、トレードオフを言語化できる

---

## 認知レベル割り当て (講師用・スライドには出さない)

| セクション | 認知レベル | 到達状態 |
|---|---|---|
| S0 Welcome | (運営) | — |
| S1 Why | 理解 | 必要性を自分の言葉で説明できる |
| S2-A 機能差 | 記憶+理解 | 3 者を区別、敵対モデルが分かる |
| S2-B Programmable Crypto | 理解 | 合成パターンを説明できる |
| S2-C 最前線 | 記憶+理解 | 主役技術 (Sumcheck/Jolt/Longfellow) の革命性を言える |
| S2-D Longfellow デモ | 理解 | 具体例の観察を通じて社会実装を認識 |
| S3-A 4 つの問い | 応用 | 自分のテーマに当てはめられる |
| S3-B 罠 | 理解+評価 | 罠の意味と影響度が判断できる |
| WB Phase 1-2 | 分析 | KelpDAO 事件を構造分解 |
| WB Phase 3 | 創造 | 新設計を作る |
| WB Phase 4 | 評価 | 他グループの設計を評価 |

---

## 全体タイムテーブル

| フェーズ | 所要 | 内容 |
|---|---|---|
| 講義 | 120 分 | Why / What / How (プリ/ポストテスト含む) |
| 休憩 + 軽食 | 30 分 | グループ移行 |
| ホワイトボード | 180 分 | KelpDAO×LayerZero exploit を題材に |

---

## レクチャー (120 分)

### タイムテーブル

| 時間 | セクション | 認知レベル | 内容 |
|---|---|---|---|
| 0–3 | プリテスト | (測定) | スマホで MCQ 5 問 |
| 3–13 | S0. Welcome | — | カリキュラム / AI 利用ルール / ホワイトボード予告 / ルーブリック提示 / 多様性配慮告知 |
| 13–48 | S1. Why | 理解 | スコープ乖離 → フェイルストップ → 3 つの社会需要 + 倫理的考察 → "証明"の意味 |
| 48–85 | S2. What | 記憶〜理解 | ZK/MPC/FHE + Programmable Crypto + 最前線 + Longfellow デモ |
| 85–95 | 休憩 |  |  |
| 95–115 | S3. How | 応用〜評価 | 4 つの問い (板書実演) + 罠 5 選 + プロジェクト発表 |
| 115–118 | クロージング | (反省) | one-minute paper / 課題 / Week 2 予告 |
| 118–120 | ポストテスト | (測定) | プリと同 5 問 + 追加 5 問 |

### S0. Welcome (10 分)

- カリキュラムマップ (1 枚、依存関係を矢印で)
- 課題提出: GitHub PR、TA レビュー、対面週 1
- ETH Global Tokyo 最終 Demo の概要、去年のハイライト写真 3 枚
- ホワイトボードセッションの予告: 講義後に KelpDAO×LayerZero $292M 事件
- AI 利用ルール:
  - グループ 1 台以上、ノート PC 持参歓迎
  - Claude / ChatGPT / Perplexity 等、好きなものを使ってよい
  - グループのうち 1 人が画面共有して全員で見る形を推奨
  - プロンプトは Notion で配布する 6 種を出発点に、自由に発展
- ルーブリック提示: 課題の評価基準を Notion で公開、講義中に 1 スライドで概観
- 多様性配慮の告知:
  - Notion ドキュメントは日英併記
  - 技術的バックグラウンドの差は TA が個別サポート
  - アクセシビリティ配慮が必要な方は事前に Discord で運営に連絡
- 自己紹介は Discord 投稿で代替

### S1. Why — なんとなく重要や (35 分)

#### S1-A. 攻撃と防御のスコープ乖離 (15 分)

防御側 (バグバウンティ、セキュリティ監査) のスコープ: ソースコード、既知の脆弱性パターン、スマートコントラクト ロジック
攻撃側のスコープ: ソースコード + ガバナンス + ソーシャルエンジニアリング + オペレーション (KMS、RPC ノード等) + AI による無人化攻撃

**事実 → スコープ乖離 (3 つの代表事例)**

| 事例 | 攻撃面 | 防御は届いていたか |
|---|---|---|
| KelpDAO×LayerZero $292M (Apr 2026) | RPC ノード侵害 + DDoS、オンチェーンは全部 valid | ソースコード監査では絶対届かない |
| Mexican government breach (2025-26) | Claude Code 悪用、社会工学で「正規 bug bounty」装う、9 機関 195M 納税者 | 静的解析の射程外 |
| Bybit $1.5B (Feb 2025) | Safe Web UI が悪意ある JS で書き換え、署名 UI と実 tx が乖離 | コントラクト・ハードウェア署名は機能 |

**Open Question**: 「あなたなら、KelpDAO の事件を防ぐためにどこにレイヤーを足しますか? なぜそこなのか?」

結論: 攻撃側はガバナンス・ソーシャル・運用に手を伸ばしている。ガバナンス・運用・社会工学の正しさを暗号で証明可能にするしかない。

#### S1-B. それだけでは不十分 — フェイルストップ機構の証明 (10 分)

- 暗号で守ったとしても、安全装置自体が正しく機能した証拠を出さないと、紛争時に何も主張できない
- 福島第一の教訓: 安全装置が「作動した証拠」を出す手段がなかった
- 最先端暗号は「機構が規定通りに発火した」を ZK 証明で出力できる

具体例: Proof-of-Exploit

- AI エージェントが脆弱性発見 → exploit を成立させた事実を ZK 証明
- DeFi コントラクトが ZK verifier として受理 → 自動停止
- これが社会実装版のフェイルストップ機構

#### S1-C. 3 つの社会的需要 + 倫理的考察 + 個人事例 (10 分)

用語注釈: 「社会実装」とは、暗号技術が研究室から出て実際の社会的取引・行政・金融サービスで稼働している状態 (学術的には deployment / real-world cryptography に対応)

**1. AI 時代のセキュリティ・プライバシー**
- AI agent identity (IETF 関連ドラフト群)、Proof-of-Exploit、Verifiable AI inference (zkML)
- Private inference (FHE-LLM, Concrete ML)、連合学習 (mpcML)
- 個人事例: 「あなたが医療データを診断 AI に預けたとき、データを保持されないと信じていいか? FHE+ZK なら検証可能」

**2. プライバシーとコンプライアンスの両立**
- 「すべて公開」 vs 「すべて秘密」の二項対立を超える
- EU 年齢確認義務 → Google が Longfellow を OSS 化 (2025 年 7 月、Sparkasse 提携)
- 個人事例: 「あなたが将来海外に住むとき、日本のマイナンバーカードで現地サービスにログインできるか? Longfellow なら可能」
- DeFi で「サンクションリストに載っていない」を ZK 証明 (Privacy Pools)

**3. Ethereum スケーリング = 効率性**
- L2 手数料の構成: proving cost が支配的になる場面が多い
- Sumcheck/Jolt で 2x 高速化 → 手数料に直結

**倫理的考察 (1 分)**
暗号によるプライバシー保護は、合法的取引も非合法な活動も同じく覆い隠す。Tornado Cash が OFAC 制裁を受けた事例 (2022) や、暗号通貨の犯罪利用の議論がある。Privacy Pools のような「規制対応プライバシー」は、この緊張を解く一つの方向性。Programmable Cryptography は中立的なツールであり、社会実装にあたっては「何を可能にするか」だけでなく「何を防ぐべきか」も同時に設計する必要がある。

#### S1-D. "証明 (proof)" の 3 つの意味 (3 分)

| 種類 | 性質 | 例 |
|---|---|---|
| 数学的証明 | 命題の真偽を formal logic で確立 | フェルマーの最終定理 |
| 情報論的暗号証明 | 確率 1 で正しい (情報論的に偽造不可能) | One-time pad、Σ-protocols |
| 計算論的暗号証明 | 計算量仮定下で偽造不可能 | デジタル署名、MAC、SNARKs/SNARGs |

橋渡し: 2026 年の最先端暗号は、3 つ目の意味で「社会的活動を検証可能にする」

### S2. What — 何ができるか (37 分)

#### S2-A. ZK/MPC/FHE の機能差 — 敵対モデルで整理 (10 分)

| | ZK | MPC | FHE |
|---|---|---|---|
| 隠す対象 | prover の証言 (witness) | 各参加者の入力 | 計算データと中間状態 |
| 信頼前提 | prover を信頼しない、verifier も信頼しない (ZK 性) | k-of-n を信頼 | server にデータ機密は信頼しない (計算正しさは別途) |
| 敵対モデル | malicious prover (soundness) + malicious verifier (ZK) | up to t corrupt parties (semi-honest / malicious) | 素の FHE: semi-honest server / malicious server には追加で ZK が必要 |
| 計算正しさ保証 | proof で保証 | 多数決 / cryptographic check | 素の FHE には無い → Verifiable FHE で補う |
| 主な用途 | 計算の正しさ証明 | 共同計算 | 計算の委託 (機密のみ) |

**Open Question**: 「結婚相手のマッチングサービスを ZK / MPC / FHE で作るとして、各選択肢のトレードオフは何ですか?」

#### S2-B. Programmable Cryptography (10 分)

**コミュニティで使われる実践的枠組み** (査読論文の formal 定義ではなく、設計者の語彙) — 暗号プリミティブをブラックボックスとして組み合わせ、新しい機能を実装可能にするフレームワーク。

設計者が意識する 3 軸:
- 異なる暗号プリミティブの sequential composition
- 共有された信頼前提下での concurrent composition
- 合成自体の verifiability

起源: 0xPARC, Barry Whitehat (2022-) のスローガン
formal な合成性: UC framework (Canetti, FOCS 2001) — UC の simulation-based security とは強さが質的に異なる点に注意

**合成パターンと例**

| 合成パターン | 何が合成されているか | 例 |
|---|---|---|
| ZK over 既存暗号 | 既存暗号スキーム (ECDSA, SHA-256) on identity standards (mDOC, JWT, W3C VC) を ZK 化 | Longfellow (Google) |
| ZK + FHE | 計算秘匿 + 計算正しさ | Verifiable FHE |
| MPC + FHE | 鍵分散 + 計算秘匿 | threshold FHE (Zama, NIST 提出) |
| ZK + ML | 推論 + 検証 | zkML |
| MPC + ML | 学習 + 入力秘匿 | mpcML (連邦学習) |
| ZK + Multisig | 操作 + 認証 | proof of multisig operation (Nyx) |
| ZK + Bridge | cross-chain message + state proof | ZK light client |

**Open Question**: 「Longfellow は学術的にどう分類できますか? なぜ既存の zkSNARK では足りなかったと考えますか?」

#### S2-C. 2026 年の最前線 — 1 つの物語 (12 分)

中心メッセージ: 「2026 年、ZK は証明系の根本が変わった。Sumcheck 系 (汎用 zkVM) と MPC-in-the-head 系 (既存 ID への適合) という、2 つの独立した革命が同時に production に入った」

> ⚠ 注: Longfellow と Sumcheck/Jolt は別系統。前者は Ligero / MPC-in-the-head 系の系譜、後者は GKR / Sumcheck 系の系譜。混同しないこと。

**系統 A: Sumcheck + Jolt (4 分)**

定義: Sumcheck とは、多変数多項式 f(x₁, ..., xₙ) の総和 ∑f を、verifier に少ない通信で確信させるインタラクティブプロトコル (Lund, Fortnow, Karloff, Nisan. JACM 39(4), 1992)

ラウンド構造:
1. prover が現在のラウンドの 1 変数についての partial sum 多項式 g(X) を送る
2. verifier がランダム点 r を選んで挑戦
3. 次のラウンドで f(...,r,...) について同じことを繰り返す
4. 最終ラウンドで f を 1 点で実際に計算する

「なぜ革命か」: structured multilinear extension 上で concretely efficient な prover (Thaler 2013 系) / 制約系を回路に書き直さなくてよい / Fiat-Shamir で SNARK 化、再帰化が容易。soundness error ≤ d·n / |𝔽| (Schwartz-Zippel)

Jolt (Arun, Setty, Thaler 2024) = Sumcheck + Lasso:
- RISC-V の全命令を lookup table T に入れる → CPU step を T 内エントリ参照と等価に
- Groth16/PLONK 比で 2x 高速 prover
- zkVM の本質: 任意プログラムを書き直さず証明できる
- (実装注意: Lasso の precompute table はメモリ要求が大きい)

**補強する側面 (4 分)**

- コミットメントの進化: KZG (pairing, trusted setup) → FRI/Brakedown/Ligero/BaseFold (hash-based)。利点: trusted setup 不要、量子耐性、Blake3 で hashing 高速
- 再帰・folding: Halo2 (accumulation) ↔ Nova (folding scheme) — 別系統が並走。Nova → LatticeFold+ / hash-based folding (2025-26)。用途: IVC で「永続的に積み上がる計算」

**系統 B: MPC-in-the-head 系 — Longfellow (3 分)**

- 設計思想: 「世界中で既に発行されている mDOC/JWT/W3C VC をそのまま ZK 化」
- 技術: MPC-in-the-head (Ligero 系) + Σ-protocol で既存署名 (ECDSA, SHA-256) を ZK 化
- ステータス: Google Wallet で deploy 済、Bumble 認証稼働、EUDI Wallet 採用検討、IETF CFRG で標準化議論

**ZK Bridge / light client (1 分)**: source chain の状態を ZK で証明 → destination chain の light client コントラクトが verify。例: Polyhedra zkBridge, Succinct Telepathy。「KelpDAO の RPC 侵害は、ZK light client なら防げたか?」をホワイトボードで議論する。

#### S2-D. Longfellow ライブデモ (5 分)

- スマホ画面ミラーリング: Google Wallet の年齢証明 → 検証サイトでの応答
- 「いま使っている運転免許証が、暗号で生年月日を隠したまま `>=18` だけ伝えている」
- 「これが Programmable Cryptography の最高の社会実装」

### (休憩 10 分)

### S3. How — どうやるか (20 分)

#### S3-A. サービス設計の出発点: 4 つの問い (8 分)

ZK/MPC/FHE をサービスに組み込む前に必ず答える 4 つの問い:

1. 何を守りたいのか? → 入力の秘密 / 計算の正しさ / 結果の秘密 / 計算した事実
2. 誰が計算するのか? → ユーザ自身 / 複数人 / 第三者 / オンチェーン
3. いつ計算するのか? → リアルタイム / 後追い / 紛争時のみ
4. 誰が検証するのか? → 個人 / コントラクト / 規制当局 / ピア

**板書テンプレ実演 (2 例)**

例 1: SMBC 日興証券 DeFi API privacy (脅威モデル: SMBC は規制当局に対し semi-honest だが、悪意ある内部者・将来の不正査問に備えたい)
1. 何を守る? → クライアント口座情報 + DeFi 取引履歴
2. 誰が計算? → SMBC のオフチェーンサーバ (運用者)
3. いつ? → リアルタイム + 監査時に後追い
4. 誰が検証? → 規制当局 + クライアント
→ 結論: ZK proof of compliance + ZK audit trail

例 2: 結婚マッチングサービス
1. 何を守る? → 各ユーザのプロフィール
2. 誰が計算? → 全参加者 (相互マッチング)
3. いつ? → リアルタイム
4. 誰が検証? → ユーザ自身
→ 結論: MPC で相互マッチング (FHE は重すぎ、ZK は片方向過ぎる)

#### S3-B. サービス開発の罠 — 5 選を解説、残りはカード配布 (8 分)

**罠 #1: 制約系・証明系の選択 (設計)**
- R1CS / Plonkish / AIR / CCS、後から変えられない、性能が桁違い
- Groth16/PLONK/Halo2/Jolt/SP1/Longfellow、検証コスト・対応言語・prover メモリ要求が変わる
- 例: Jolt は prover メモリ要求が大きいため、small device には不向き

**罠 #2: soundness と zero-knowledge は別物、両方とも壊れうる (安全性)**
- 「証明できる」と「秘密が漏れない」は独立した性質、両方を別個に保証する必要
- 実事例: Semaphore の signal hash bug (ZK Bug Tracker 収録)
  - public input が回路内で実際に計算に使われていなかった
  - 攻撃者は valid な proof を取得後、signal hash だけ書き換えて任意の signal を偽装可能
  - 修正: signalHashSquared = signalHash² として回路に組み込んだ

**罠 #3: Fiat-Shamir の RO instantiation (安全性)**
- KRS25 (Khovratovich, Rothblum, Soukhanov, eprint 2025/611) で GKR-based SNARK の現実的攻撃が示された
- 「論文は安全」≠「実装は安全」

**罠 #4: witness generation がボトルネック (性能)**
- 「proving time 5 秒」は witness 生成を含むかどうかで意味が変わる
- ベンチマークを読む時の最重要ポイント

**罠 #5: on-chain verifier gas + off-chain prover インフラ (運用)**
- verifier gas は L2 経済性に直結
- prover サーバの GPU/メモリ要件は地味に高い

**カード配布のみ (残り 8 つ)**: 設計: ハッシュ関数選択 / trusted setup vs transparent。安全性: サイドチャネル+鍵管理 / 回路と仕様の乖離。性能: FHE ノイズ管理 / MPC 通信ラウンド数。運用: アップグレード時の回路互換性 / クライアント体験

**Open Question**: 「自分のプロジェクトで一番怖い罠はどれですか? その罠が表面化するのはいつだと思いますか?」

#### S3-C. プロジェクト発表 (4 分)

各テーマに [難易度 / 前提 / 推奨スタック]:
- **Intmax 系**: MPC Wallet 鍵復元 [高] / Channel-based note discovery + PIR [中] / zERC20 transfer tree [中] / Formal-verified tornado clone [高]
- **Nyx 系**: ZK proof of multisig operation [中] / FHE で完全データレスな EC サイト [中-高] / Proof-of-Exploit + DeFi 自動停止 [高] / SPECA で ZK/FHE/MPC 回路バグ探索 [高]
- **SMBC 日興証券**: Off-chain finance system → DeFi API privacy [中]
- **ソニー銀行 + もう一社**: TBD
- **オリジナル**: 提案ベース

### クロージング (3 分) + ポストテスト (2 分)

#### One-Minute Paper (1 分)
- 「今日一番分かった概念は?」
- 「今日一番分からなかった概念は?」
- スマホで匿名 Google Forms 入力

Week 2 運用フロー:
- TA が結果を集計、「分からなかった」のトップ 3 を抽出
- Discord で共有、Week 2 冒頭 5 分で応答

#### クロージング (2 分)
- 学習成果 1-8 の達成度を学生自己評価 (Discord で 5 段階)
- 課題説明 (Track A/B/C/D)
- ホワイトボードへの橋渡し: KelpDAO×LayerZero、4 つの問い、13 の罠 がツール
- Week 2 予告: MPC で「電卓を 3 人で割って計算する」(中江)

#### ポストテスト (2 分)
- プリテストと同じ MCQ 5 問 + 追加 5 問
- Discord で結果を集約

---

## ホワイトボードセッション

### お題

**「KelpDAO × LayerZero $292M Exploit (April 18, 2026) を最先端暗号で防げただろうか?」**

2026 年最大の DeFi exploit。スマートコントラクトには bug がなく、オフチェーンインフラ (RPC ノード) を侵害された。S1-A のスコープ乖離テーマと完全一致する事例。

### Phase タイムテーブル

| Phase | 所要 | 内容 | 認知レベル |
|---|---|---|---|
| Phase 1 | 30 分 | 事件の理解 + AI で attack tree | 分析 |
| Phase 2 | 45 分 | 4 つの問いをチェックリスト形式で埋める | 分析〜応用 |
| Phase 3 | 50 分 | 設計案構築、A3 にまとめる | 創造 |
| Phase 4 | 55 分 | 発表 (7 分) + 質疑 (4 分) × 5 グループ | 評価 |
| 合計 | 180 分 |  |  |

### 情報パッケージ (各グループに事前配布、A4 1 枚)

**何が起きたか**
- KelpDAO の rsETH bridge (LayerZero 経由) から 116,500 rsETH (~$292M) 流出
- LayerZero による preliminary attribution: Lazarus Group / TraderTraitor (北朝鮮系)
- Aave の TVL が連鎖で蒸発 (数値は配布 Chainalysis レポート参照)

**攻撃フロー (LayerZero 公式発表に基づく)**
1. 攻撃者が LayerZero verifier が参照する RPC ノード一覧を入手
2. 内部 RPC ノード 2 台のバイナリを悪意あるバージョンに置換
3. 外部 RPC ノードを DDoS で落とし、failover を強制
4. verifier に偽の cross-chain メッセージを承認させた
5. Ethereum 側コントラクトが「ソースチェーンで burn が起きた」と信じて release

**重要な事実**
- スマートコントラクトには bug なし (オンチェーンは全部正しく動いた)
- 1-of-1 DVN configuration が単一障害点
- LayerZero と Kelp で責任の押し付け合い中

**従来のセキュリティが届かなかった理由**
- 全てのオンチェーン tx が valid に見えた
- 監査スコープは smart contract、攻撃面は off-chain RPC infrastructure

### Phase 1-4 詳細

Phase 1 (30 分): 資料読み込み (5 分) + AI と対話して攻撃フローを理解 (25 分)。Notion 配布の完成形プロンプト 6 種をコピペで活用。グループでホワイトボードに attack tree を描く。

Phase 2 (45 分): A3 用紙にチェックリスト形式テンプレ。1) 何の正しさを保証 / 2) 誰が証明を作る / 3) いつ証明を作る / 4) 誰が検証 / 5) ZK / MPC / 複合のどれを採用。

Phase 3 (50 分): 4 つの方向性から 1 つ — ZK 路線 (ZK light client) / MPC 路線 (threshold MPC) / 複合 / 暗号で防げない派。A3 用紙に: 採用方向と理由、必要な暗号プリミティブ、残るリスク (13 の罠から 3 つ)、限界。

Phase 4 (55 分): 5 グループ × 11 分 (発表 7 分 + 質疑 4 分)。他グループから 1 つ質問必須。講師からの突っ込み弾を必ず 1 つ入れる。

**講師の突っ込み弾**:
- 「ZK light client なら、source chain の RPC が同じく侵害されたらどう?」
- 「threshold MPC で何台に分散すれば現実的に攻撃が止まる? Lazarus は国家アクターだぞ」
- 「あなた方の案、KelpDAO の運営チームは導入できる? gas コストは?」
- 「LayerZero と Kelp の責任論争、あなた方の設計だとどっちのせいになる?」

**Closing Question**: 「ZK と MPC のトレードオフ、5 年後にはどう変わると思いますか?」

---

## 実装課題

### Track A: 読む (全員必須)
- a16z Jolt blog (2026): 3 行サマリ
- Google Longfellow 公式 blog + IETF draft Introduction: 3 行
- Zama TFHE Handbook イントロ: 3 行
- KRS25 paper (eprint 2025/611) の introduction (1 ページ): 教訓 1 行
- Chainalysis の KelpDAO bridge exploit blog: 復習として再読

### Track B: 書く (レベル選択、いずれか 1 つ)
- Easy: commit-reveal で秘密入札を実装
- Medium: Schnorr signature を Python で実装、テスト通す
- Hard: Sumcheck protocol の最小実装 (3 変数多項式)

### Track C: 選ぶ (全員必須)
- ホワイトボードセッションのグループ成果物を清書 (Notion 1 ページ)
- 自分のプロジェクトテーマでも 4 つの問い + 罠 3 枚を埋める

### Track D: 環境 (全員必須)
- Rust toolchain, Node.js/TS, Docker
- Nyx Foundation/acp-week1-template repo を fork → CI 通過
- 13 の罠カードを GitHub Issue として fork した repo に複製

---

## 参考文献

**SNARK 革命 (Sumcheck 系)**
- Lund, Fortnow, Karloff, Nisan. "Algebraic methods for interactive proof systems." JACM 39(4), 1992. (Sumcheck の原論文)
- Arun, Setty, Thaler. "Jolt: SNARKs for Virtual Machines via Lookups." (2024). a16z crypto.
- Setty, Thaler, Wahby. "Unlocking the lookup singularity with Lasso." eprint 2023/1216.
- Thaler. "Time-Optimal Interactive Proofs for Circuit Evaluation." CRYPTO 2013.

**コミットメント**
- Ben-Sasson et al. "Brakedown: Linear-time and Field-agnostic SNARKs." CRYPTO 2023.
- Ames et al. "Ligero: Lightweight Sublinear Arguments." CCS 2017.
- Zeilberger et al. "BaseFold." (2024)

**Folding / IVC**
- Kothapalli, Setty. "Nova: Recursive Zero-Knowledge Arguments from Folding Schemes." CRYPTO 2022.
- Bünz, Chen. "LatticeFold+: Faster, Simpler, Shorter Lattice-Based Folding." eprint 2025/247.

**セキュリティ**
- Khovratovich, Rothblum, Soukhanov. "On Black-Box Verifiability of GKR Protocols." eprint 2025/611. (KRS25)

**Programmable Cryptography**
- Barry Whitehat. "Programmable Cryptography." 0xPARC blog (2022).
- Canetti. "Universally Composable Security." FOCS 2001.

**Longfellow**
- Google. "Longfellow: ZK over Existing Identity Standards." OSS release (Jul 2025).
- Trail of Bits + Ligero. "Longfellow Security Review." (2025).
- Frigo & shelat. eprint 2024/2010.

**FHE/MPC**
- Zama. "TFHE-rs Handbook." (2024-25).
- Chillotti et al. "TFHE: Fast Fully Homomorphic Encryption." Journal of Cryptology 2020.

**事件レポート**
- Chainalysis. "Inside the KelpDAO Bridge Exploit." (Apr 2026).
- LayerZero Labs. "Post-mortem: April 18 Exploit." (Apr 2026).
- KelpDAO. "Response to LayerZero Statement." (Apr 2026).

**ZK Bug Tracker**
- 0xPARC. github.com/0xPARC/zk-bug-tracker

**Privacy Pools**
- Buterin et al. "Blockchain Privacy and Regulatory Compliance: Towards a Practical Equilibrium." eprint 2023/1322.
