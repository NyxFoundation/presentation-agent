---
layout: default
---

# 次の数年、DeFiが向き合う領域

<div class="text-sm opacity-70 mt-1 mb-3 max-w-5xl">
  二本柱の外側に出た問題 ── 業界としてはまだ着手されていない、共通の論点
</div>

<div class="grid grid-cols-3 gap-4 mt-1 max-w-6xl">

<div class="border border-gray-300 rounded-lg p-3 bg-gray-50">
  <div class="text-xs tracking-widest text-blue-900 font-bold mb-2">論点 1</div>
  <div class="text-base font-bold leading-tight mb-2">失敗様式 ↔ 既存統制 の対応辞書</div>
  <div class="text-xs opacity-80 leading-relaxed mb-2">
    1-of-1 マルチシグ / 運用設定の不備 / 外部ベンダー連携 ── DeFiの失敗様式を、<span class="font-bold">ITGC / FISC / SoC2</span> の語彙へ翻訳する公開辞書が未整備
  </div>
  <div class="text-xs opacity-60 border-t border-gray-200 pt-2">必要なのは: 横断対応表 / 共通言語</div>
</div>

<div class="border border-gray-300 rounded-lg p-3 bg-gray-50">
  <div class="text-xs tracking-widest text-emerald-800 font-bold mb-2">論点 2</div>
  <div class="text-base font-bold leading-tight mb-2">運用の正しさの継続的保証</div>
  <div class="text-xs opacity-80 leading-relaxed mb-2">
    監査はリリース時点のスナップショット。稼働中の <span class="font-bold">マルチシグ・ノード・権限</span> を見続け、<span class="font-bold">形式検証</span> と <span class="font-bold">残高証明 (PoR) の運用版</span> で守るべき条件を証明し続ける仕組みが未整備
  </div>
  <div class="text-xs opacity-60 border-t border-gray-200 pt-2">必要なのは: 運用モニタリング / 形式検証 / 運用版 PoR</div>
</div>

<div class="border border-gray-300 rounded-lg p-3 bg-gray-50">
  <div class="text-xs tracking-widest text-red-700 font-bold mb-2">論点 3</div>
  <div class="text-base font-bold leading-tight mb-2">バグバウンティを置き換える発見モデル</div>
  <div class="text-xs opacity-80 leading-relaxed mb-2">
    人手判定のコンテスト型 (Sherlock 等) は研究者を萎縮させる。<span class="font-bold">AIによる動的監視</span> と <span class="font-bold">形式検証付きの報告</span> でチェックを自動化する仕組みが未整備
  </div>
  <div class="text-xs opacity-60 border-t border-gray-200 pt-2">必要なのは: AI動的監視 / 形式検証付き報告</div>
</div>

</div>

<div class="text-center mt-4 text-sm opacity-80 max-w-5xl mx-auto leading-relaxed">
  <span class="font-bold">運用統制 + 数学的保証 + 発見の自動化</span> ── この三つの接続が、次の数年の最大論点
</div>

<!--
本日のお話を、最後に業界全体の論点として置き直します。二本柱の外側に出た問題は、特定の会社が解く話ではなくて、DeFi業界としてまだ着手できていない論点です。三つ挙げます。一つ目、失敗様式と既存統制の対応辞書。1-of-1 マルチシグ、運用開始時の設定不備、外部ベンダー連携といったDeFiの失敗様式を、ITGCやFISC、SoC2の既存統制語彙に翻訳する公開辞書がまだない。共通言語が要ります。二つ目、運用の正しさの継続的保証。監査はリリース時点のスナップショットでしかなく、稼働中のマルチシグ設定・ノード接続・権限を見続けて、形式検証つまり数学的証明と、Proof of Reserve残高証明の運用版で守るべき条件を証明し続ける仕組みが業界に未整備です。三つ目、バグバウンティを置き換える発見モデル。今のバウンティは人手による起票と判定で、研究者を萎縮させ判定者の負担も大きい。AIによる動的監視と、形式検証付きの報告でチェックを自動化する仕組みが、次世代の脆弱性発見の鍵になります。運用統制+数学的保証+発見の自動化、この三つの接続が、次の数年のDeFiセキュリティの最大論点になります。
-->
