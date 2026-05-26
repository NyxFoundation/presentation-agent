---
layout: default
---

# セキュリティ監査の仕組みは壊れ始めている

<div class="grid grid-cols-[0.85fr_1.15fr] gap-7 mt-6 items-center">

<div>
  <div class="text-xs uppercase tracking-widest opacity-40 mb-1">2025年・暗号資産の盗難</div>
  <div class="text-7xl font-bold leading-none" style="font-family: 'BIZ UDPMincho', serif;">$3.4B</div>
  <div class="text-xs opacity-50 mt-2">Bybit 一件だけで $1.5B（Chainalysis 2026）</div>
</div>

<div class="oos">
  <div class="oos-x">対象外</div>
  <div>
    <div class="text-sm font-bold mb-1">被害の大きい攻撃ほど、そもそも検査されていない</div>
    <div class="flex flex-wrap gap-1.5 mb-1">
      <span class="oos-tag">MEV</span>
      <span class="oos-tag">オラクル価格操作</span>
      <span class="oos-tag">取引順序の操作</span>
      <span class="oos-tag">経済・ガバナンス攻撃</span>
    </div>
    <div class="text-xs opacity-55">これらの動的・経済的な脆弱性は、多くのバグバウンティで <strong>明示的に out of scope</strong>。</div>
  </div>
</div>

</div>

<div class="text-xs uppercase tracking-widest opacity-40 mt-6 mb-2">しかも、守る側の「人手の網」が崩れ始めた</div>
<div class="grid grid-cols-3 gap-4">
  <div class="cl">
    <div class="cl-name">curl</div>
    <div class="cl-fact">バグバウンティ<strong>終了</strong></div>
    <div class="cl-n">AI偽レポートが殺到。本物の報告は約5%（2026年1月）</div>
  </div>
  <div class="cl">
    <div class="cl-name">HackerOne</div>
    <div class="cl-fact">AI関連報告 <strong>+210%</strong></div>
    <div class="cl-n">人手のトリアージが、報告の洪水に追いつかない</div>
  </div>
  <div class="cl">
    <div class="cl-name">Code4rena</div>
    <div class="cl-fact">監査コンペ大手が<strong>事業縮小</strong></div>
    <div class="cl-n">人手・単発・静的な監査モデルが限界に（2026年5月）</div>
  </div>
</div>

<div class="mt-5 conc">静的・人的・単発のセキュリティは限界。<strong>動的・自律・永続</strong>の公共財が要る。</div>

<style>
.oos { display: flex; gap: 12px; align-items: center; border: 2px solid #c63a3a; border-radius: 0.6rem; padding: 0.85rem 1rem; }
.oos-x { font-family: 'BIZ UDPMincho', serif; font-size: 17px; font-weight: 700; color: #c63a3a; border: 2px solid #c63a3a; border-radius: 6px; padding: 4px 8px; flex-shrink: 0; }
.oos-tag { font-size: 10.5px; padding: 2px 9px; border: 1px solid #d4d4d4; border-radius: 999px; }
.cl { border: 1px solid #e5e7eb; border-top: 4px solid #c63a3a; border-radius: 0.5rem; padding: 0.7rem 0.85rem; }
.cl-name { font-size: 12px; font-weight: 700; opacity: 0.5; letter-spacing: 0.04em; }
.cl-fact { font-size: 16px; font-weight: 700; font-family: 'BIZ UDPMincho', serif; margin: 0.15rem 0 0.3rem; }
.cl-n { font-size: 10px; line-height: 1.55; opacity: 0.6; }
.conc { text-align: center; font-size: 15px; font-weight: 700; font-family: 'BIZ UDPMincho', serif; border-top: 2px solid #111; padding-top: 0.7rem; }
</style>

<SourceCite :sources="[
  { label: 'Chainalysis 2026', url: 'https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/' },
  { label: 'Immunefi Bug Bounty Scope (out-of-scope例)', url: 'https://immunefi.com/bug-bounty/veda/information/' },
  { label: 'curl — Death by a thousand slops', url: 'https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/' },
  { label: 'HackerOne — 210% spike in AI vuln reports', url: 'https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy' },
  { label: 'Code4rena wind-down (Crypto Times)', url: 'https://www.cryptotimes.io/2026/05/13/code4rena-announces-wind-down-after-securing-billions-in-defi/' }
]" />

<!--
Speaker Notes:
最初の課題です。2025年単年で、ハッキングにより34億ドル超の暗号資産が盗まれました。Bybitの一件だけで15億ドルです。厄介なのは、最も損害の大きい攻撃——MEV、オラクル価格操作、取引順序の操作、経済・ガバナンス攻撃——が、多くのバグバウンティで明示的に「対象外」とされている点です。一番損害の大きい動的・経済的な脆弱性を、誰も体系的には検査していない。さらに、守る側の人手のモデル自体が壊れ始めています。curlはAI生成の偽レポートの殺到で2026年1月にバグバウンティを終了——本物の報告はわずか5%でした。HackerOneではAI関連の脆弱性報告が前年比210%増。監査コンペ大手のCode4renaも2026年5月に事業縮小を発表。静的・人的・単発のセキュリティは限界です。動的・自律・永続の公共財が要ります。
-->
