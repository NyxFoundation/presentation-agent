---
layout: default
---

# Current Finance のコード地図 ─ ADL が走るまで

<div class="text-xs opacity-60 mb-3">Sui上のレバレッジLending ／ <span class="font-mono">market.move</span> (1,301行) ／ Sherlock contest #312</div>

<div class="relative">

<div class="grid grid-cols-9 items-center gap-0">

<div class="col-span-1 border border-gray-400 rounded bg-gray-50 px-1 py-1.5 text-center">
<div class="text-[9px] font-bold opacity-60">STEP 1</div>
<div class="text-[11px] font-bold leading-tight">ポジション作成</div>
<code class="text-[8px] opacity-50 block leading-tight mt-0.5">handle_new_<br/>obligation</code>
</div>

<div class="col-span-1 text-center text-2xl opacity-30 font-bold">→</div>

<div class="col-span-1 border border-gray-400 rounded bg-gray-50 px-1 py-1.5 text-center">
<div class="text-[9px] font-bold opacity-60">STEP 2</div>
<div class="text-[11px] font-bold leading-tight">担保を預ける</div>
<code class="text-[8px] opacity-50 block leading-tight mt-0.5">handle_mint</code>
</div>

<div class="col-span-1 text-center text-2xl opacity-30 font-bold">→</div>

<div class="col-span-1 border border-gray-400 rounded bg-gray-50 px-1 py-1.5 text-center">
<div class="text-[9px] font-bold opacity-60">STEP 3</div>
<div class="text-[11px] font-bold leading-tight">借入 (eMode)</div>
<code class="text-[8px] opacity-50 block leading-tight mt-0.5">handle_borrow</code>
</div>

<div class="col-span-1 text-center text-2xl opacity-30 font-bold">→</div>

<div class="col-span-1 border-2 border-red-700 rounded bg-red-50 px-1 py-1.5 text-center relative shadow-md">
<div class="absolute -top-2 right-0.5 bg-red-700 text-white text-[8px] font-bold px-1 py-0.5 rounded shadow">問題関数</div>
<div class="text-[9px] font-bold text-red-700">STEP 4</div>
<div class="text-[11px] font-bold leading-tight">ADL 実行</div>
<code class="text-[8px] opacity-60 block leading-tight mt-0.5">handle_debt_<br/>auto_deleverage</code>
</div>

<div class="col-span-1 text-center text-2xl opacity-30 font-bold">→</div>

<div class="col-span-1 border border-gray-400 rounded bg-gray-50 px-1 py-1.5 text-center">
<div class="text-[9px] font-bold opacity-60">STEP 5</div>
<div class="text-[11px] font-bold leading-tight">停止判定</div>
<code class="text-[8px] opacity-50 block leading-tight mt-0.5">try_stop_<br/>borrow_deleverage</code>
</div>

</div>

<div class="absolute left-0 right-0" style="top: 100%;">
<div class="grid grid-cols-9">
<div class="col-span-6"></div>
<div class="col-span-1 flex flex-col items-center pt-1">
<div class="text-[9px] text-red-700 font-bold tracking-wider">拡大</div>
<div class="text-red-700 text-lg leading-none">▼</div>
</div>
<div class="col-span-2"></div>
</div>
</div>

</div>

<div class="grid grid-cols-2 gap-3 mt-12">

<div class="border-2 border-gray-300 rounded p-2 bg-gradient-to-br from-gray-50 to-white">

<div class="text-[10px] font-bold tracking-wider opacity-70 mb-1.5">ステップ4 の中身 ─ 3つの管理ポイント</div>

<div class="space-y-1">

<div class="flex items-center gap-2">
<div class="text-[10px] font-mono opacity-50 w-10">:575</div>
<div class="flex-1 h-6 bg-emerald-200 border-l-4 border-emerald-600 rounded-sm flex items-center px-2">
<div class="text-[10px] font-bold text-emerald-900">✓ 登録</div>
<div class="text-[10px] ml-auto opacity-70">グループ別</div>
</div>
</div>

<div class="flex items-center gap-2">
<div class="text-[10px] font-mono opacity-50 w-10">:580</div>
<div class="flex-1 h-7 bg-red-200 border-l-4 border-red-700 rounded-sm flex items-center px-2 shadow-md">
<div class="text-[11px] font-bold text-red-900">❌ 実行ガード</div>
<div class="text-[11px] font-bold text-red-700 ml-auto">reserve 全体</div>
</div>
</div>

<div class="flex items-center gap-2">
<div class="text-[10px] font-mono opacity-50 w-10">:686</div>
<div class="flex-1 h-6 bg-emerald-200 border-l-4 border-emerald-600 rounded-sm flex items-center px-2">
<div class="text-[10px] font-bold text-emerald-900">✓ 停止</div>
<div class="text-[10px] ml-auto opacity-70">グループ別</div>
</div>
</div>

</div>

<div class="mt-2 text-[10px] text-center opacity-70 leading-tight border-t pt-1">
<span class="font-bold">3 箇所のうち 1 箇所だけ</span>が違う粒度を見ている
</div>

</div>

<div class="border-2 border-gray-300 rounded p-2 bg-gradient-to-br from-gray-50 to-white">

<div class="text-[10px] font-bold tracking-wider opacity-70 mb-1.5">攻撃データフロー</div>

<div class="grid grid-cols-2 gap-2">
<div class="border border-blue-500 bg-blue-50 rounded p-1 text-center">
<div class="text-[9px] font-bold text-blue-800">顧客A (Group A)</div>
<div class="text-sm font-bold font-mono">30M</div>
<div class="text-[8px] text-emerald-700 font-bold">健全 (&lt;50M)</div>
</div>
<div class="border border-gray-500 bg-gray-100 rounded p-1 text-center">
<div class="text-[9px] font-bold text-gray-700">顧客B (Group B)</div>
<div class="text-sm font-bold font-mono">80M</div>
<div class="text-[8px] opacity-60">無関係</div>
</div>
</div>

<div class="grid grid-cols-2 -my-0.5">
<div class="text-right text-lg leading-none text-gray-500">↘</div>
<div class="text-left text-lg leading-none text-gray-500">↙</div>
</div>

<div class="bg-gray-900 text-white text-center py-1 rounded">
<div class="text-[8px] opacity-70 font-mono">reserve.debt()  ← :580 が読む</div>
<div class="text-base font-bold font-mono">110M USDC</div>
</div>

<div class="text-center text-sm leading-none text-gray-500 my-0.5">↓</div>

<div class="border-2 border-red-700 bg-red-100 rounded p-1 text-center">
<div class="text-[9px] opacity-70">:580 比較</div>
<div class="text-xs font-bold font-mono text-red-700">110M &gt; 50M = TRUE</div>
<div class="text-[9px] text-red-700 font-bold">→ Group A に ADL 発動 (誤)</div>
</div>

</div>

</div>

<!--
Current Financeのコード全体像です。market.move約1,300行ですが、ユーザが触る経路は上のパイプラインの5ステップ。ポジション作成、担保、借入、ADL実行、停止判定。問題があるのはステップ4のhandle_debt_auto_deleverage。その関数を拡大鏡で覗いたのが下段。左下、関数の中に3つの管理ポイントがある。575行が登録、580行が実行ガード、686行が停止。本来3つともグループ別の借入額を見るべきところ、580行だけがreserve全体を見ていた。右下が攻撃データフロー。顧客Aが30M借りる、別グループの顧客Bが80M借りる、同じUSDC reserveに合算され110M。580行はこの110Mを読んで、Group Aの閾値50Mと比較してしまう。本来は顧客Aの借入30Mを見て30M < 50Mで発動しないはずが、110M > 50Mで誤発動。Group Aの健全な顧客Aが巻き添え清算されます。次のスライドで、3つの管理ポイントを実コードで並べて読みます。
-->
