---
layout: default
---

# 2件報告して、受け取った報酬 ¥27

<div class="text-sm opacity-60 mb-6">Lending サービス Current Finance ／ Sherlock contest #312 (2025-09)</div>

<div class="grid grid-cols-2 gap-8 mt-2">

<div class="border-2 border-gray-400 rounded-lg p-5 bg-gray-50">
  <div class="flex items-baseline gap-3 mb-3">
    <span class="bg-amber-600 text-white text-xs px-3 py-1 font-bold tracking-wider">Medium</span>
    <span class="text-xs opacity-60">Bug 1 ／ 清算の基準ズレ</span>
    <span class="text-xs opacity-60 ml-auto">CVSS 5.3</span>
  </div>
  <div class="text-lg font-bold leading-snug mb-1">資格判定は<span class="font-mono">EMA価格</span>、執行は<span class="font-mono">Spot価格</span></div>
  <div class="text-sm opacity-80 leading-relaxed">借り手から余分に担保を奪える経路 (CWE-682)</div>
</div>

<div class="border-2 border-red-700 rounded-lg p-5 bg-red-50">
  <div class="flex items-baseline gap-3 mb-3">
    <span class="bg-red-700 text-white text-xs px-3 py-1 font-bold tracking-wider">High</span>
    <span class="text-xs opacity-60">Bug 2 ／ グループ管理の不整合</span>
    <span class="text-xs opacity-60 ml-auto">CVSS 7.4</span>
  </div>
  <div class="text-lg font-bold leading-snug mb-1">顧客Aを見るべき場所で、銀行全体を見ていた</div>
  <div class="text-sm opacity-80 leading-relaxed">健全な顧客の<span class="font-bold">巻き添え清算</span> (CWE-840)</div>
</div>

</div>

<div class="grid grid-cols-[1fr_2fr] gap-8 items-center mt-10">
  <div class="border-l-4 border-red-700 pl-5">
    <div class="text-xs opacity-60 tracking-wider mb-1">受取報酬の合計</div>
    <div class="text-7xl font-bold text-red-700 leading-none">¥27</div>
    <div class="text-xs opacity-60 mt-1">= 0.18 USDC</div>
  </div>
  <div class="text-sm opacity-80 leading-relaxed">
    Current Financeは業界平均より真面目に対応している会社です。<br/>
    それでも、High1件・Medium1件で <span class="font-bold">¥27</span>
    <div class="text-xs opacity-60 mt-2">出典: Sherlock contest #312 公開判定書</div>
  </div>
</div>

<!--
これが私たちが受け取った報酬の合計です。前スライドで掘ったHighの『グループ管理の不整合』と、Mediumの『EMA価格とSpot価格の使い分けズレ』、2件合計で0.18 USDC、約27円。Current Financeが特別ダメなのではなく、業界平均より真面目に対応している会社です。Sherlockコンテスト#312、2025年9月開催の公開判定書ベース。次のスライドで、攻撃側との収支対比を見ます。
-->
