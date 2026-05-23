---
layout: default
---

# Current Finance のコード地図 ─ ADL が走るまで

<div class="text-xs opacity-60 mb-2">Sui上のレバレッジLending ／ <span class="font-mono">market.move</span> (1,301行) ／ Sherlock contest #312</div>

<div class="grid grid-cols-2 gap-4 mt-1">

<!-- LEFT: user flow with function mapping -->
<div>
<div class="text-xs font-bold tracking-wider mb-1 opacity-70">ユーザフロー × 担当関数</div>

<div class="space-y-1">

<div class="flex items-center gap-2 border border-gray-300 rounded p-1.5 bg-gray-50">
  <div class="bg-gray-600 text-white font-bold w-6 h-6 flex items-center justify-center rounded-full text-xs flex-shrink-0">1</div>
  <div class="flex-1 min-w-0">
    <div class="text-xs font-bold leading-tight">ポジション作成</div>
    <code class="text-[10px] opacity-70">handle_new_obligation</code>
  </div>
  <div class="text-[10px] font-mono opacity-50">:243</div>
</div>

<div class="text-center text-[10px] opacity-30 leading-none">↓</div>

<div class="flex items-center gap-2 border border-gray-300 rounded p-1.5 bg-gray-50">
  <div class="bg-gray-600 text-white font-bold w-6 h-6 flex items-center justify-center rounded-full text-xs flex-shrink-0">2</div>
  <div class="flex-1 min-w-0">
    <div class="text-xs font-bold leading-tight">担保を預ける</div>
    <code class="text-[10px] opacity-70">handle_mint</code>
  </div>
  <div class="text-[10px] font-mono opacity-50">:258</div>
</div>

<div class="text-center text-[10px] opacity-30 leading-none">↓</div>

<div class="flex items-center gap-2 border border-gray-300 rounded p-1.5 bg-gray-50">
  <div class="bg-gray-600 text-white font-bold w-6 h-6 flex items-center justify-center rounded-full text-xs flex-shrink-0">3</div>
  <div class="flex-1 min-w-0">
    <div class="text-xs font-bold leading-tight">借入 (eMode グループ指定)</div>
    <code class="text-[10px] opacity-70">handle_borrow</code>
  </div>
  <div class="text-[10px] font-mono opacity-50">:366</div>
</div>

<div class="text-center text-[10px] opacity-30 leading-none">↓</div>

<div class="flex items-center gap-2 border-2 border-red-700 rounded p-1.5 bg-red-50 relative">
  <div class="absolute -right-2 -top-2 bg-red-700 text-white text-[9px] font-bold px-1.5 py-0.5 rounded-full shadow">問題関数</div>
  <div class="bg-red-700 text-white font-bold w-6 h-6 flex items-center justify-center rounded-full text-xs flex-shrink-0">4</div>
  <div class="flex-1 min-w-0">
    <div class="text-xs font-bold leading-tight text-red-700">ADL 実行 (強制縮退)</div>
    <code class="text-[10px] opacity-70">handle_debt_auto_deleverage</code>
  </div>
  <div class="text-[10px] font-mono opacity-50">:546</div>
</div>

<div class="text-center text-[10px] opacity-30 leading-none">↓</div>

<div class="flex items-center gap-2 border border-gray-300 rounded p-1.5 bg-gray-50">
  <div class="bg-gray-600 text-white font-bold w-6 h-6 flex items-center justify-center rounded-full text-xs flex-shrink-0">5</div>
  <div class="flex-1 min-w-0">
    <div class="text-xs font-bold leading-tight">停止判定</div>
    <code class="text-[10px] opacity-70">try_stop_borrow_deleverage</code>
  </div>
  <div class="text-[10px] font-mono opacity-50">:685</div>
</div>

</div>
</div>

<!-- RIGHT: zoom into the problem function + attack path overlay -->
<div>

<div class="text-xs font-bold tracking-wider mb-1 opacity-70">ステップ 4 を開いた中身 ─ <span class="text-red-700">3つの管理ポイント</span></div>

<div class="border-2 border-red-700 rounded bg-white p-2 mb-2">
  <div class="text-[10px] opacity-60 mb-1">handle_debt_auto_deleverage の内側</div>
  <div class="text-[10px] space-y-0.5 font-mono leading-tight">
    <div class="flex"><span class="opacity-50 w-12">:575</span><span class="text-emerald-700">✓ 登録</span><span class="ml-2 opacity-70">グループ別</span></div>
    <div class="flex bg-red-100 rounded px-1"><span class="opacity-50 w-12">:580</span><span class="text-red-700 font-bold">❌ 実行</span><span class="ml-2 opacity-70">reserve 全体</span></div>
    <div class="flex"><span class="opacity-50 w-12">:686</span><span class="text-emerald-700">✓ 停止</span><span class="ml-2 opacity-70">グループ別</span></div>
  </div>
</div>

<div class="text-xs font-bold tracking-wider mb-1 opacity-70 mt-3">攻撃経路 ─ どの段で何が起きるか</div>

<div class="text-[11px] space-y-1">
  <div class="flex gap-2 items-start">
    <div class="bg-blue-700 text-white font-bold w-4 h-4 flex items-center justify-center rounded text-[9px] flex-shrink-0 mt-0.5">3</div>
    <div>顧客A (Group A) 借入 <span class="font-mono font-bold">30M</span> ／ 顧客B (Group B) 借入 <span class="font-mono font-bold">80M</span></div>
  </div>
  <div class="flex gap-2 items-start">
    <div class="bg-gray-700 text-white font-bold w-4 h-4 flex items-center justify-center rounded text-[9px] flex-shrink-0 mt-0.5">↓</div>
    <div>同じ USDC reserve に合算 → <code class="font-mono font-bold">reserve.debt() = 110M</code></div>
  </div>
  <div class="flex gap-2 items-start">
    <div class="bg-red-700 text-white font-bold w-4 h-4 flex items-center justify-center rounded text-[9px] flex-shrink-0 mt-0.5">4</div>
    <div class="text-red-700 font-bold">:580 が 110M &gt; 50M で誤発動 (本来 30M &lt; 50M で発動せず)</div>
  </div>
  <div class="flex gap-2 items-start mt-1 border-t-2 border-red-700 pt-1">
    <div class="text-red-700 font-bold flex-1">❌ Group A の健全な顧客Aが強制清算 ─ 次スライドで詳細</div>
  </div>
</div>

</div>

</div>

<!--
Current Financeのコード全体像です。market.move約1,300行のうち、ユーザが触る経路は5ステップ。ポジション作成、担保預け、借入(eModeグループ指定)、ADL実行、停止判定。それぞれ担当関数が1つずつあって、コードを横並びに読めば1本道です。問題はステップ4のhandle_debt_auto_deleverage。この1つの関数の中に3つの管理ポイントがある。575行が登録、580行が実行、686行が停止。本来3つともグループ別の借入額を見るべきところ、実行ガード580行だけがreserve全体を見ていた。攻撃経路もこのフロー図に重なります。顧客Aと顧客Bが別グループで借りる、同じreserveに合算される、ステップ4で誤発動、Group Aの健全な顧客Aが巻き添え清算。次のスライドで、3つの管理ポイントを並べて読みます。
-->
