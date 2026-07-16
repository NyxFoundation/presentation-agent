---
layout: default
---

# ProgCrypto は<span class="text-amber-700">ブロックチェーンの耐量子移行</span>の最後の鍵だ

<div class="mt-1 flex justify-center">
<img src="/images/zkvm_proving_time.png" class="max-h-[330px] w-auto object-contain" />
</div>

<div class="mt-3 text-sm font-bold text-gray-700">ZK 中心のイーサリアム</div>

<div class="mt-2 grid grid-cols-2 gap-3">

<div class="bg-white rounded-xl border border-gray-200 shadow-sm p-3 text-sm text-gray-700 leading-relaxed">
<div class="text-base font-bold text-gray-900 mb-1">耐量子移行 — lean Ethereum</div>
署名・コミットメントをハッシュベースへ。<strong class="text-gray-900">実行の検証は zkVM の ZK 証明</strong>が担う
</div>

<div class="bg-white rounded-xl border border-gray-200 shadow-sm p-3 text-sm text-gray-700 leading-relaxed">
<div class="text-base font-bold text-gray-900 mb-1">zkVM as Smart Contract — native rollups</div>
L1 バリデータが <strong class="text-gray-900">zkVM の証明を検証</strong>し、rollup の実行を L1 が直接保証する
</div>

</div>

<div class="absolute bottom-3 left-6 text-[10px] text-gray-400 leading-tight max-w-3xl">
Sources: RISC Zero "Zeth" PR (Aug 2023) ｜ Succinct "SP1 Reth" (Feb 2024) / "SP1 Hypercube" (May 2025) ｜ Brevis "Pico Prism" (Oct 2025) / "Pico Prism 2.0" (May 2026) ｜ EF Blog "Realtime Proving" (Jul 2025) / "zkEVM Security Foundations" (Dec 2025) / "lean Ethereum" (Jul 2025) ｜ NIST IR 8547 (2024) ｜ EIP-8079 "Native Rollups"
</div>

<!--
Speaker Notes:

【概要 (需要 ②)】
需要 ① はセキュリティだった。② は Ethereum 本体のロードマップ。「Ethereum の最重要問題の一つである耐量子移行 — そのボトルネックが zkVM になっている」という 1 枚。WHY のセクションなので時間をかけてよい。

【グラフの読み方】
- 縦軸は Ethereum 1 ブロックの証明時間 (log)。2022 年には数時間かかっていた (RISC Zero の記述)。
- SP1 Reth (2024/2, Succinct): 実測 41.8-64.3 分 (CPU のみ)。ここで初めて「分オーダーの実測値」が公表された。
- SP1 Hypercube (2025/5, Succinct): mainnet 1 万ブロックの 93% を 12 秒未満、平均 10.3 秒 (RTX 4090 クラスタ)。証明系を univariate STARK から multilinear (Sumcheck 系) に全面刷新した結果。
- Pico Prism (2025/10, Brevis): 45M gas ブロックの 99.6% を 12 秒未満、平均 6.9 秒 (RTX 5090 × 64)。Pico Prism 2.0 (2026/5) は同 99.9% ・平均 6.1 秒を RTX 5090 × 16 (マシン 2 台) で達成 — ハードウェア要件が 1/4 に。
- 緑の帯 = 12 秒 (Ethereum の 1 スロット)。EF の公式定義は厳密には「スロット 12 秒 − 伝播 1.5 秒 → P99 で 10 秒以下」(EF Blog "Realtime Proving")。
- EF 総括 (2025/12): 「証明レイテンシは 9 ヶ月で 16 分 → 16 秒、コストは 1/45、target hardware で全ブロックの 99% を 10 秒未満で証明」。

【12 秒を超えた (下回った) 後の世界 — 下の 2 カード】
- 耐量子移行: lean Ethereum (Justin Drake, EF Blog 2025/7/31)。BLS 署名は楕円曲線ペアリングベースで Shor のアルゴリズムに脆弱。コンセンサス層はハッシュベース集約署名 (leanXMSS)、データ層は KZG → ハッシュベースコミットメント、実行層は hash-based real-time zkVM に置換する。つまり耐量子 Ethereum の実行層は zkVM が前提 — zkVM が 12 秒を切れないと移行計画自体が成立しない。NIST IR 8547 は従来公開鍵暗号を 2030 非推奨 / 2035 廃止としており、期限は外部から与えられている。
- zkVM as Smart Contract: native rollups (Justin Drake, ethresear.ch 2025/1 → EIP-8079)。EXECUTE precompile で L1 バリデータが rollup の状態遷移を zkVM 証明の検証によって直接検証する。rollup は独自の fraud proof / prover 網 / security council への信頼が不要になり L1 セキュリティを継承。Optimism・Base が採用意向。
- どちらも「real-time zkVM がある」ことを前提に書かれた公式ロードマップ / EIP。だから需要 ② の結論も聞き手に補完させる: 「zkVM の性能競争は L2 の手数料の話ではなく、Ethereum 本体の耐量子化と L1 セキュリティ継承の前提条件なのか」。

【正確性の注意】
- 「数時間」(2022-23) は RISC Zero の 2023/8 プレスリリースの記述 ("proofs for Ethereum blocks take many hours")。当時の単一実測値は公表されていない。
- Zeth (2023/8) は「数分」と発表されたが正確な実測値非公表のためグラフの頂点には採用していない。
- 各点はハードウェアが異なる (CPU → GPU クラスタ → コンシューマ GPU 16 枚)。「同一条件の推移」ではなく「最速公表値の推移」。
-->
