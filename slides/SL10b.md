---
layout: default
---

# 社会的需要 ② — <span class="text-amber-700">Ethereum Scaling</span>

<div class="mt-10 text-center text-2xl font-bold text-gray-900 leading-relaxed">
データ層は解けた — 次のボトルネックは <span class="text-amber-700">proving cost</span>、<br/>
証明の効率がそのまま L2 手数料を決める
</div>

<div class="mt-12 flex items-stretch gap-3">

<div class="flex-1 bg-white rounded-xl border border-gray-200 shadow-sm p-4">
<div class="text-[11px] font-bold tracking-widest text-gray-400 mb-2">事実</div>
<div class="text-3xl font-black text-gray-900 mb-1">−85%</div>
<div class="text-xs text-gray-500 mb-3">PeerDAS による validator のデータ取得量 (750MB → 112MB/日)</div>
<div class="text-sm text-gray-700 leading-relaxed">
<span class="text-amber-500">&#9654;</span> Pectra (2025/5) で blob 6 → 9<br/>
<span class="text-amber-500">&#9654;</span> Fusaka (2025/12) で PeerDAS 導入
</div>
</div>

<div class="flex items-center text-gray-300 text-3xl font-black">→</div>

<div class="flex-1 bg-white rounded-xl border border-gray-200 shadow-sm p-4">
<div class="text-[11px] font-bold tracking-widest text-gray-400 mb-2">課題</div>
<div class="text-sm text-gray-700 leading-relaxed">
<span class="text-amber-500">&#9654;</span> データが安くなった今、手数料の支配項は <strong class="text-gray-900">proving cost</strong> に移る<br/><br/>
<span class="text-amber-500">&#9654;</span> L2 の競争軸は <strong class="text-gray-900">prover throughput</strong> へ (Linea / Scroll / Taiko / Succinct SP1)
</div>
</div>

<div class="flex items-center text-gray-300 text-3xl font-black">→</div>

<div class="flex-1 bg-amber-50 rounded-xl border border-amber-200 p-4">
<div class="text-[11px] font-bold tracking-widest text-amber-700 mb-2">答え</div>
<div class="text-sm text-gray-700 leading-relaxed">
証明系そのものを<strong class="text-gray-900">速くする</strong><br/><br/>
<span class="text-green-500">&#10003;</span> Sumcheck 系 zkVM (Jolt: 従来比 2x prover)<br/>
<span class="text-green-500">&#10003;</span> folding / IVC<br/>
<span class="text-green-500">&#10003;</span> hash-based commitment
</div>
</div>

</div>

<div class="absolute bottom-3 left-6 text-[10px] text-gray-400 leading-tight max-w-3xl">
Sources: Ethereum.org Fusaka roadmap (Dec 2025) ｜ Arun, Setty, Thaler "Jolt: SNARKs for Virtual Machines via Lookups" (2024) ｜ Thaler "Time-Optimal Interactive Proofs for Circuit Evaluation" CRYPTO 2013
</div>

<!--
Speaker Notes:

【概要】
社会的需要の 2 枚目。構図は前ページと同一 (メッセージ → 事実 → 課題 → 答え)。Ethereum Scaling のナラティブ: 「データ層はプロトコルアップグレードで解けた。残ったボトルネックは証明コストであり、それは暗号 (証明系) の研究がそのまま手数料に効く領域」。

【事実カード】
- Pectra (2025/5): blob 数 6 → 9。Fusaka (2025/12): PeerDAS 導入で validator が全 blob をダウンロードせずサンプリング検証 → データ取得量 85% 削減 (1 日 750MB → 112MB)。
- 帰結として L2 手数料は post-Fusaka で 40-60% 下落予想 (データコスト部分)。

【課題カード】
手数料 = データコスト + proving cost + 運営マージン。データコストが 1 桁下がると、proving cost が支配項になる。L2 各社の競争軸が「どれだけ速く安く証明を作れるか」(prover throughput) に移っている: Linea Type-1、Scroll、Polygon zkEVM、Taiko、Succinct SP1。

【答えカード】
証明系そのものの高速化が競争力: Sumcheck 系 (structured multilinear extension 上で concretely efficient — Thaler 2013 系。無条件に「線形時間」とは言わない)、Jolt (Sumcheck + Lasso lookup、Groth16/PLONK 比 2x prover)、folding/IVC (Nova 系)、hash-based commitment (FRI/Brakedown/BaseFold — trusted setup 不要 + hashing 高速)。技術の中身は S2-C (このあとのセクション) で扱う。ここでは「暗号研究が手数料に直結する」という経済構造だけ掴んでもらう。

【講義での強調点】
- ①のセキュリティ需要と独立に見えるが、同じ「検証可能な計算を効率よく」という要請の別経路。
- 受講者への引き: このプログラムで学ぶ Sumcheck / Jolt は、そのまま L2 の手数料競争の最前線のスキル。
-->
