---
layout: default
---

# 要件が変われば、<span class="text-amber-700">使う暗号が変わる</span> — KelpDAO の例

<div class="mt-6 rounded-xl border border-gray-200 bg-gray-50 p-3 text-sm text-gray-700 text-center">
共通の要件: <strong class="text-gray-900">AI Auditor が</strong> ｜ <strong class="text-gray-900">攻撃手順 W を事業者 / サードパーティ / 他ユーザーから隠して</strong> ｜ <strong class="text-gray-900">on-chain コントラクトが検証</strong> — 変えるのは STEP 3 (どういう計算をして) だけ
</div>

<div class="mt-6 space-y-4">

<div class="flex items-stretch gap-3">
<div class="flex-1 bg-amber-50 rounded-xl border border-amber-200 p-4 text-sm text-gray-800 flex items-center"><div><span class="text-[11px] font-bold tracking-widest text-amber-700 mr-3">パターン A</span>単独の Auditor が「W でコントラクトが壊れる」ことを計算する</div></div>
<div class="flex items-center text-gray-300 text-2xl font-black">→</div>
<div class="w-90 bg-white rounded-xl border border-gray-200 shadow-sm p-4 flex items-center"><div><div class="text-lg font-black text-gray-900">ZK 証明</div><div class="text-xs text-gray-500 mt-1">単一の計算者が、秘密を隠したまま正しさを証明する</div></div></div>
</div>

<div class="flex items-stretch gap-3">
<div class="flex-1 bg-amber-50 rounded-xl border border-amber-200 p-4 text-sm text-gray-800 flex items-center"><div><span class="text-[11px] font-bold tracking-widest text-amber-700 mr-3">パターン B</span>複数の監査ノードが、互いの判定基準を隠したまま合議で計算する</div></div>
<div class="flex items-center text-gray-300 text-2xl font-black">→</div>
<div class="w-90 bg-white rounded-xl border border-gray-200 shadow-sm p-4 flex items-center"><div><div class="text-lg font-black text-gray-900">MPC</div><div class="text-xs text-gray-500 mt-1">複数の参加者が、入力を隠したまま共同で計算する</div></div></div>
</div>

<div class="flex items-stretch gap-3">
<div class="flex-1 bg-amber-50 rounded-xl border border-amber-200 p-4 text-sm text-gray-800 flex items-center"><div><span class="text-[11px] font-bold tracking-widest text-amber-700 mr-3">パターン C</span>LLM が脆弱性を判定し、その推論が規定通り実行されたことまで検証する</div></div>
<div class="flex items-center text-gray-300 text-2xl font-black">→</div>
<div class="w-90 bg-white rounded-xl border border-gray-200 shadow-sm p-4 flex items-center"><div><div class="text-lg font-black text-gray-900">ZK + LLM (zkML)</div><div class="text-xs text-gray-500 mt-1">LLM の推論そのものを ZK で検証可能にする</div></div></div>
</div>

</div>

<!--
Speaker Notes:

【概要】
前ページの 4 ステップ要件定義の続き。同じ KelpDAO Circuit-Breaker でも、STEP 3 (どういう計算をして) の置き方を変えるだけで、使う暗号プロトコルが変わることをマップで見せる。STEP 1 (AI Auditor)・STEP 2 (W を事業者 / サードパーティ / 他ユーザーから隠す)・STEP 4 (on-chain 検証) は 3 パターンとも共通。

【3 パターンの読み方】
- パターン A (基本形): 単独の Auditor が「W で壊れる」ことを計算 → 単一 prover の検証可能計算なので ZK 証明が自然な選択。検証者が on-chain なので証明が短く検証が軽い SNARK 系に絞れる。
- パターン B: 複数の監査ノードが、互いの判定基準 (シグネチャ・検知ロジック) を開示せずに合議で判定したい → 「複数当事者が入力を隠して共同計算」は MPC の定義そのもの。threshold 合議にすれば 1 ノードの誤検知で誤遮断しない、という運用要件も同時に満たせる。
- パターン C: 判定そのものを LLM にやらせたい。ただし「規定のモデルとプロンプトで推論された」ことまで検証しないと、攻撃者が LLM の判定を偽装できる → LLM 推論の検証可能化 = zkML (ZK + LLM)。現状は推論の完全な ZK 化はコストが高く、モデルのコミットメント + 部分検証が現実解 — と正直に言う。
- 教訓: 技術から入るのではなく、要件 (特に「誰が計算するか」「何を隠すか」) がプロトコルを決める。午後のホワイトボードでは各グループがこの分岐を自分で辿る。
-->
