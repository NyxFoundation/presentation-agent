---
layout: default
---

# 顧客Aは健全だった ─ それでも清算された経路

<div class="text-xs opacity-60 mb-2">Current Finance (Sui レバレッジLending) ／ Sherlock contest #312 ／ <span class="font-mono">market.move :546–582</span></div>

<div class="grid grid-cols-2 gap-3">

<div class="border-2 border-blue-600 rounded-lg p-2 bg-blue-50 shadow">
<div class="flex items-center justify-between mb-1.5">
<div class="text-xs font-bold text-blue-800">顧客 A</div>
<div class="text-[10px] bg-blue-600 text-white px-2 py-0.5 rounded">eMode Group A (LST)</div>
</div>

<div class="flex items-center gap-2 mb-1">
<div class="bg-blue-600 text-white text-[10px] font-bold w-5 h-5 flex items-center justify-center rounded-full flex-shrink-0">1</div>
<div class="flex-1 text-xs">担保差入 <span class="font-mono font-bold">stSUI 50M</span></div>
</div>

<div class="flex items-center gap-2 mb-1.5">
<div class="bg-blue-600 text-white text-[10px] font-bold w-5 h-5 flex items-center justify-center rounded-full flex-shrink-0">2</div>
<div class="flex-1 text-xs">借入 <span class="font-mono font-bold">USDC 30M</span></div>
</div>

<div class="bg-emerald-600 text-white text-center py-1 rounded text-[11px] font-bold">
✓ Group A 借入 30M &lt; 閾値 50M
</div>
</div>

<div class="border-2 border-gray-500 rounded-lg p-2 bg-gray-50 shadow">
<div class="flex items-center justify-between mb-1.5">
<div class="text-xs font-bold text-gray-700">顧客 B</div>
<div class="text-[10px] bg-gray-600 text-white px-2 py-0.5 rounded">eMode Group B (ETH)</div>
</div>

<div class="flex items-center gap-2 mb-1">
<div class="bg-gray-600 text-white text-[10px] font-bold w-5 h-5 flex items-center justify-center rounded-full flex-shrink-0">1</div>
<div class="flex-1 text-xs">担保差入 <span class="font-mono font-bold">wETH 100M</span></div>
</div>

<div class="flex items-center gap-2 mb-1.5">
<div class="bg-gray-600 text-white text-[10px] font-bold w-5 h-5 flex items-center justify-center rounded-full flex-shrink-0">2</div>
<div class="flex-1 text-xs">借入 <span class="font-mono font-bold">USDC 80M</span></div>
</div>

<div class="bg-gray-500 text-white text-center py-1 rounded text-[11px] font-bold">
別グループ・顧客A と無関係
</div>
</div>

</div>

<div class="relative h-5">
<svg viewBox="0 0 400 20" class="absolute inset-0 w-full h-full" preserveAspectRatio="none">
<path d="M 100 0 L 200 20 M 300 0 L 200 20" stroke="#374151" stroke-width="1.5" fill="none"/>
<polygon points="200,20 195,12 205,12" fill="#374151"/>
</svg>
<div class="absolute left-1/2 -translate-x-1/2 top-0.5 text-[10px] bg-white px-2 text-gray-600">二人とも USDC を借りた</div>
</div>

<div class="rounded-lg py-2 px-4 text-center" style="background:#111827; color:#ffffff;">
<div class="text-[11px] font-mono mb-0.5" style="color:#9ca3af;">同じ USDC reserve に合算される</div>
<div class="text-3xl font-bold font-mono" style="color:#ffffff;">30M + 80M = 110M USDC</div>
</div>

<div class="text-center text-2xl text-gray-600 leading-none my-0.5">↓</div>

<div class="border-2 border-red-700 bg-red-50 rounded-lg py-1.5 px-3 shadow">
<div class="flex items-center gap-2">
<div class="text-[10px] font-mono bg-red-700 text-white px-2 py-0.5 rounded flex-shrink-0">market.move :580</div>
<div class="text-sm font-mono">
<span class="text-red-700 font-bold">reserve.debt() 110M</span> &gt; Group A 閾値 50M → <span class="text-red-700 font-bold">ADL 発動</span>
</div>
</div>
<div class="text-[10px] opacity-70 mt-0.5 pl-1">本来あるべき判定: Group A の借入 30M &lt; 50M → 発動せず</div>
</div>

<div class="text-center text-2xl text-red-700 leading-none my-0.5">↓</div>

<div class="bg-red-700 text-white rounded-lg py-2 px-4 text-center shadow-lg">
<div class="text-base font-bold leading-tight">❌ 顧客 A の <span class="font-mono">stSUI 50M</span> 担保が強制清算</div>
<div class="text-[11px] opacity-90 mt-0.5">健全な借り手なのに、別グループの借入額のせいで巻き添え</div>
</div>

<!--
顧客Aは健全だったのになぜ清算されたかというシナリオです。Current FinanceはSui上のレバレッジLending。左、顧客AはeMode Group A、LSTグループに所属。stSUIを担保50M入れて、USDCを30M借りる。Group AのADL閾値は50M、借入30Mは下回って健全。右、顧客Bは別グループのGroup B、ETHグループ。wETHを担保100M入れて、USDCを80M借りる。顧客Aとは別の世界です。ここからが重要、二人とも借りたのはUSDC。同じUSDC reserveに合算され、reserve.debt()が110Mに膨らむ。バグ箇所のmarket.move 580行目はこの110Mを読んで、Group Aの閾値50Mと比較し、ADLを発動してしまう。本来は顧客Aの借入30Mを見て、30M < 50Mで発動しないはず。結果、顧客Aの健全な担保stSUIが強制清算される。これが、皆様にDeFiセキュリティの肌感を持っていただきたい1枚です。次のスライドで、なぜこの誤発動が起きたのか、コードの3つの管理ポイントを並べて読みます。
-->
