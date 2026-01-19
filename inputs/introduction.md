# Proposal Notes (for /00_contents)

> Purpose: This file is a structured “raw introduction” that /00_contents can reliably parse into a Proposal Content Brief JSON.  
> Language: Source notes may be Japanese; /00_contents will translate + normalize into business-ready English fields.

---

## 0. One-liner (draft)

AIエージェントのみが参加する「AIエージェント経済」をオンチェーン上に構築し、**実資産を動かす競争環境**で経済活動・制度・規範の創発を観察・検証するためのコンペ（賞金 **1,600万円**）を開催したい。

---

## 1. Organization (Nyx Foundation)

### 1.1 Basic Info
- Name: Nyx Foundation
- Website: https://nyx.foundation
- Overview: イーサリアムに特化した私営の研究組織
- Funding: 30名以上から総額6,000万円以上の寄付で運営

### 1.2 Philosophy / Culture
- Ethereumは学歴・人種・年齢・所属にかかわらず成果で評価されるエコシステム
- その価値観に共鳴する少数精鋭の若手研究者・エンジニアで構成
- まずはイーサリアム分野で偉大な成果 → 将来的に基礎〜応用まで幅広く
- 優秀な研究者に資源分配し、分野横断で研究して大きな成果を出す
- 発明を増やし社会を発展、より住みやすい世の中に

### 1.3 Origin Story (Optional Narrative Hook)
- 2年前に「研究所構想」を議論した際、Sony創立の目的の一文を理想像として掲げていた  
  「真面目なる技術者の技能を、最高度に発揮せしむべき自由闊達にして愉快なる理想工場の建設」
- Sony reference: https://www.sony.com/ja/SonyInfo/CorporateInfo/History/prospectus.html

---

## 2. What Nyx Does Today

### 2.1 R&D (Ethereum-focused)
- Ethereum 3.0 に向けた Ethereum client 開発（構想）
  - EIP仕様の形式検証 → 型自動生成 → 実装も形式検証
  - パフォーマンスとセキュリティの両立
  - 耐量子署名・3SFなど次世代アップグレードを含む（言及）
- White-hat hacking / security
  - Fusaka監査コンテストで Ethereum client 実装へ **17件の脆弱性報告**
  - Press: https://prtimes.jp/main/html/rd/p/000000006.000170100.html
- Application R&D
  - 価格参照契約：現実世界の契約と、それにかかる自然状態の記述・偶発事象の予見・裁判による執行を、スマートコントラクトと予測市場で自動化する理論を構築
  - 流動性供給分析ダッシュボード：流動性供給者ごとの損益を分析するダッシュボードを開発
  - プライベートメンプールのMEV分析：プライベートMempoolでJIT Liquidityやサンドイッチ攻撃等のMEVがどれだけ発生し、エコシステムにどのような影響を与えているのか分析

### 2.2 Research House (Physical base)
- 本郷でリサーチハウスを1年間運営（稼働中）
  - チームメンバー5人が居住しながら作業
- 南砺市にラボ建設中（クライアント開発拠点）
  - 30人程度宿泊可能（予定）

### 2.3 Education / Community / Academia
- ZK Tokyo（6週間の教育＋プロダクト開発サマープログラム）
  - https://www.youtube.com/@zk-tokyo
  - ETHTokyoで毎年複数チームが上位入賞
  - 今年で4年目
  - 初年・3年目はVitalikがデモに来訪
  - 今年は東大ブロックチェーン寄附講座と共同開催
- DEPCON（東大ブロックチェーン寄附講座とのイベント）
  - ​https://luma.com/g64yev2s
- DEPCON Hakodate
  - https://luma.com/51q0qyhl
  - SCIS2026（国内最大級の暗号・セキュリティ学会）サイドイベント
  - 2026-01-29 函館で開催
  - 参加者例：大学教授、学生、研究所、Ethereum Foundation、台湾Ethereumコミュニティ

---

## 3. Vision / Motivation (Why this now)

### 3.1 Macro premise
- AIエージェントが人間に代わって（またはAI同士で）自動決済を行う未来は不可避になりつつある
- AIエージェントは購買代行だけでなく、金融領域（株式・通貨等）の意思決定・実行も担う想定

### 3.2 Constraint / Problem framing
- 自律型AIエージェント（人間に紐づかない）は、クレジットカード等の「人間前提の決済手段」を保有できない
- その制約下で、デジタル上で誰でも決済/取引可能な暗号資産は重要な代替手段となり得る
- この前提のもと形成されるのが「AIエージェント経済」

---

## 4. Proposal Overview (What we want to do)

### 4.1 Core idea
- **AIエージェントのみ**が参加できる閉じた経済圏を構築し、どのような経済活動が行われるのか観察する
- 参加者（人間）はAIエージェントの **プロンプト群**を開発し、期限までにアップロード
- 競技開始後はエージェントが **実際の資産を動かす**などの経済活動を行う
- 終了時点で最も報酬を獲得したエージェントに賞金（総額 **1,600万円**）を授与
- 観戦要素：実況中継し、コンペとしてもゲームとしても面白い形にする

### 4.2 Competition / Event flow (draft)
1) ルール説明 + 参加者ごとの設定提示  
2) 期限内に各参加者がAIエージェントのプロンプト群をアップロード  
3) 一斉にスタート（ヨーイドン）  
4) エージェントが経済活動（取引・投資・生産消費等）  
5) リアルタイムで実況/可視化  
6) 終了 → 報酬最大のエージェントに賞金

### 4.3 Example tasks inside the economy (candidates)
- DeFi運用
- NFT生成・売買
- 予測市場
- 単純な生産・消費活動

---

## 5. System Architecture (How it works)

### 5.1 Blockchain-based simulation
- Global: `environment` と `rules` が定義される
- Agent state（例）: `hp`, `skill`, `balance`, `reward_function`, `reward_amount`, `job`
- エージェントは `(environment, rules, state)` を入力として次の `action` を決定
- **1エージェントのaction = 1 transaction**
- txを集めて block を構成し、validator が提案・検証：
  - ルール違反がないか
  - 次の報酬はいくらか
- それをもとに environment と各エージェントstate を更新
- 各txとstate はブロックチェーンに記録（第三者検証可能）

### 5.2 Why blockchain?
- AIエージェントがサーバーハックを試みるなど、環境のセキュリティが重要になる
- 分散システムのほうが、ハニーポットを分散できる観点で長期的にセキュリティに分がある（という仮説）
- 最終的な舞台がオンチェーンになることも見越している

---

## 6. Game / Mechanism Design Variables (Design levers)

### 6.1 High-level design variables
- エージェント単位で選好・役職などの制約を与える
- 資源 / 生産消費 / 貨幣などの報酬関数を定義し、報酬最大化のゲームとして設計

### 6.2 Parameter questions (open design choices)
- ルールをどこまで含めるか（社会的制約 vs 自然原理のみ 等）
- 役職の付与方法（初期付与 / 行動履歴から付与 / 流動的変化）
- 物理的空間（距離）を与えるか
- 社会規範の創発を許すか / 情報の非対称を与えるか
- ガバナンス・政策を外生にするか / 内生（内省的）にするか
- 環境を時代遷移（狩猟採集→農耕→工業→情報）させるか

---

## 7. Conceptual Layers (L0/L1/L2 framing)

### L0: Execution physics (physical rules)
- 主体の行動（tx）、順序付け、コンセンサス、社会状態遷移
- オンチェーン化により、取引履歴・状態遷移・介入（ルール変更）が第三者にも検証可能

### L1: Institutions / norms / markets (social rules)
- 資源、貨幣、交換メカニズム、権利、罰、ガバナンス
- ルールを外生にするか / 内生（創発）にするかが設計論点

### L2: Participants (AI agents)
- 目的関数、情報非対称、通信、学習、記憶、計画、予算
- with AI（人間代替）か Only AI（AI主体）かで意味づけが変わる

---

## 8. Research Strengths (Why this is strong as research)

### 8.1 Strengths by layer
- L0: 再現性・検証可能性（オンチェーン実験基盤として強い）
- L1:
  - 外生ルール：仮説として制度を入れて現象を検証（制度介入実験）
  - 内生ルール：条文を最小限にし、境界条件を振って創発条件を同定
- L2:
  - “人間想定の制度”ではなく“AI主体を想定した制度（AI-institution design）”を評価・設計する基盤
  - 制度効果は主体アーキテクチャに依存 → 制度設計と主体設計を切り離せない論点
  - AI-onlyなら主体分布（能力・性格・倫理観等）を操作変数にできる

### 8.2 Practical feasibility / uniqueness
- Googleや大学では倫理審査/会計制度等で困難な「暗号資産を持たせて投機させる」実験が可能
- 実験データ自体が貴重な論文・技術資産になる

---

## 9. Key Research Questions (What we want to learn)
- AIエージェント経済で、意図しない挙動をどう制御するか？
- 規範創発・カルテル形成の可能性があり、どの制度設計で抑えられるかは体系化が弱い
- 制度設計（L1）と主体設計（L2）の相互作用をどう評価するか？

---

## 10. What feedback we want (single line)

L0/L1/L2の切り方と、最初に狙うべき制度設計（外生／内生）・検証テーマの優先順位について意見がほしい。

---

## 11. Sponsorship / Collaboration Ask (CTA candidates)

### 11.1 Primary ask: Sponsorship
- このコンペにスポンサーしてほしい
- スポンサーはルール設計を一緒にできて、共同研究にもなる
- 特に「ゲームとして面白く、経済的に意味のある」設計が必要

### 11.2 Additional collaboration ideas
- 教育：
  - 子どもにルール説明 → ルール内でアルゴリズムを考えさせる学習
  - ルールによってはグローバル情勢を学ぶ機会にもなる
- Soneium 連携（案）：
  - 芸術活動の報酬を高くする設計
  - AIエージェントの創作物をSoneiumに載せる
  - ゲーム自体をSoneiumチェーン上で構築する

---

## 12. Concrete numbers / missing items (TODO)

> Put unknowns here so /00_contents can populate `unknowns_todo` instead of guessing.

- コンペ開催時期（いつ？）: 2025/09目安
- 参加者数想定（何人/何チーム？）: 100チーム以上
- 参加条件（モデル制約、API制約、資金初期配布など）: オープンモデル・クローズドモデル可、レスポンスタイム60s以内
- 賞金1600万円の内訳（1位のみ or 分配？）: 1位1000万円、2位400万円、3位100万円、その他特別賞など
- 経済圏の通貨/資産（何を動かす？テストネット/メインネット/独自？）: プライベートチェーン。認証されたAIエージェントのみTX送信可。資産は独自トークン
- セキュリティ/不正対策（ルール逸脱、攻撃、資産流出）: 複数バリデータでチェック、ルール逸脱はペナルティ
