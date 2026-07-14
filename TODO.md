# TODO — ACP26 Week 1 デッキ改修 (第 2 ラウンド)

ページ番号は現行 `slides.md` の include 順 (2026-07-14 時点):
p1=SL01, p2=SL02, p3=SL07, p4=SL08b, p5=SL08c, p6=SL09, p7=SL10, p8=SL10b, p9=SL10c,
p10=SL12, p11=SL14, p12=SL15, p13=SL17, p14=SL18, p15=SL20, p16=SL21, p17=SL22,
p18=SL23, p19=SL25, p20=SL26, p21=SL27, p22=SL28, p23=SL29, p24=SL31, p25=SL32

## p7 (slides/SL10.md) — ナラティブヒート化

- [x] p3-6 の内容に自然と続く形で「Programmable Cryptography はセキュリティの足りない部分を埋める」
      を見せる。(figures/hack_pie.py — Hacken 2025 内訳ドーナツ + 右側に暗号の対応表)
      2025 ハッキング内訳を円グラフで出し、各領域に「ZK でこう防げる」「MPC / FHE で
      こう防げる」を添える。伝えたいことをドンと出すのではなく、客観的事実で上品に理解させ、
      相手が「つまりこういうことなんだ！」と自分で補完する構成にする。

## p8 (slides/SL10b.md) — 耐量子移行 × zkVM ナラティブ

- [x] p3-7 のナラティブフローに沿わせる (WHY は時間をかける)。
      (figures/zkvm_proving.py — log 軸の証明時間推移 + 12s 閾値 + lean Ethereum / EIP-8079 カード)
      「Ethereum の最重要問題の一つである耐量子移行。そのボトルネックが zkVM になっている」。
      zkVM の Ethereum block proving time を年ごとのグラフで出す。各数値にどの企業の製品かを
      表すアイコンを添える。12s に閾値線 (超えたら実用化)。実用化後に「耐量子移行」と
      「zkVM as Smart Contract」が実現しより強固になることを、別の客観的事実で示す。

## p9 (slides/SL10c.md) — 機関マネー TVL ナラティブ + ZK Bridge 例の移設

- [ ] 近年の TVL 推移を全ブロックチェーンで出し、その中に機関系サービス
      (Lighter, Tempo, Ondo, Hyperliquid, ...) がどれだけ含まれるかを示す図を出す。
      「それらの機関マネーを 2026-27 で 10 倍にするには？？？」もグラフに添える。
      その後に課題として「プライバシー」「コンプライアンス」をでかでかと見せる。
      視聴者が「これが実現したら Web3 めっちゃくるやん！」と分かる構成に。
- [ ] p17 (SL22) の ZK Bridge は、この機関マネーナラティブの「例えばこういう仕組み」の
      一例としてここへ移動する (slides.md の include 順を変更)。

## p10 (slides/SL12.md) — タイトルと図の整理

- [x] 「①は adversary を想定しない——」の注釈的な行は削除。(内容は speaker notes に移設)
- [x] タイトルは『「ゼロ知識証明」の「証明」とは何を指すか』に。
- [x] 図から「2026 年の社会実装はここ」を削除 (figures/proof_meanings.py)。
      (バンドラベルは新タイトルの答えとして「ZK の「証明」はここ」に差し替え)
- [x] ③ の例から Longfellow を削除。

## p11 (slides/SL14.md) — タイトル変更

- [x] タイトルを「ZK / MPC / FHE」に。

## p12 (slides/SL15.md) — タイトル変更

- [x] S2-B を削除し、タイトルを
      「Programmable Cryptography — 暗号とシステムを一体化するパラダイム」に。

## p13-16 (slides/SL17/18/20/21.md) — 1 枚に統合 + 定量軸化

- [ ] p13 (SL17): 一番上の S2-C の行は削除。縦軸の「実用性」をやめ、スピード等の
      定量的な値にする。Sumcheck 系の他に STARK 系も入れる。
      「(既存 ID)」と「回路書き直し + ...」の注記は削除。
      Groth16 は Sumcheck 系ではない (pairing 系) — 分類を修正する。
- [ ] p14 (SL18) 削除 — p13 で説明を完結させる。
- [ ] p15 (SL20) 削除 — 省略。
- [ ] p16 (SL21) 削除 — p13 にマージ。

## p18 (slides/SL23.md) — デモ動画のみに

- [x] デモ動画だけを出す。説明類はすべて削除。タイトルは「Longfellow ライブデモ」。
      (public/videos/longfellow-demo.mp4 はプレースホルダ — 録画版に差し替えるだけで反映)
- [x] デモ用の環境レポジトリを用意する。(demo/longfellow/ に README + setup.sh —
      外部リポジトリに切り出す場合はこのディレクトリをそのまま移せば OK)

## p19 (slides/SL25.md) — 考え方 + KelpDAO Circuit Breaker 例

- [x] タイトルを「ProgCrypto をサービスに組み込むときの考え方」に。
      4 つの流れを書いた上で、下に例を 1 個書く。例は p6 の KelpDAO Circuit Breaker にして、
      「要件をこう変えたら、こういう対策になる」が視聴者に分かるようにする。
      (4 問カード + 各問いへの KelpDAO の答え + 「答えが 1 つ変われば設計も変わる」行)

## p20-22 (slides/SL26/27/28.md) — 削除

- [x] p20 (SL26) 削除 — 例は p19 に移動するので不要。
- [x] p21 (SL27) / p22 (SL28) 削除 — 今回は省略。
      (未使用になった components/{DevTraps,FourQuestions,Jolt,ProofMeanings,SocialDemands}Demo.vue と
      4_questions.svg も削除)

## p23 (slides/SL29.md) — テーマ一覧表化

- [x] Notion「Advanced Cryptography Program Output Themes」にまとめてあるものを
      そのまま一覧表として表示する。レクなので変な囲い・装飾・省略はしない。
      (12 行のプレーン表: Intmax 4 / Nyx 4 / SMBC 日興 2 / キリフダ 1 / HODL1 追加予定)
      https://app.notion.com/p/grandchildrice/Advanced-Cryptography-Program-Output-Themes-359d05af0d5a80dbbaa9dd231add14db

## p24 (slides/SL31.md) — ホワイトボードセッション

- [x] タイトルを「本日のホワイトボードセッション: KelpDAO 事件を防ぐためのシステムを
      一つ考えてください」に。Phase 1-4 のボックスと Closing Question は削除。
      「ホワイトボードに書く内容」として 1. アーキテクチャ図、2. 要件、3. 選定技術。

## p25 (slides/SL32.md) — 削除

- [x] スライドごと削除 (slides.md の include も外す)。
