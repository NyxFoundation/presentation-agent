---
layout: default
---

# 「動いている」と「安全」は違う — それを確かめる仕組みが、壊れ始めた

<div class="grid grid-cols-2 gap-8 mt-5">

<div>
  <div class="text-xs uppercase tracking-widest opacity-40 mb-2">Problem ① — 被害は増え、最悪の攻撃は“対象外”</div>
  <div class="text-5xl font-bold mb-1" style="font-family: 'BIZ UDPMincho', serif;">$3.4B</div>
  <div class="text-sm opacity-50 mb-4">2025年単年でハッキングにより盗まれた暗号資産（Bybit単体で$1.5B）</div>
  <div class="text-sm leading-relaxed mb-3">
    しかも被害の大きい <strong>MEV・オラクル価格操作・取引順序操作・経済/ガバナンス攻撃</strong> は、
    多くのバグバウンティで <strong>明示的に対象外（out of scope）</strong>。
  </div>
  <div class="text-xs opacity-50">
    監査・形式検証・バグバウンティを尽くしても、<strong>最も損害の大きい動的・経済的な脆弱性</strong>を、誰も体系的には検査していません。
  </div>
</div>

<div>
  <div class="text-xs uppercase tracking-widest opacity-40 mb-2">Problem ② — 人手のセキュリティ網が崩壊し始めた</div>
  <div class="space-y-2.5">
    <div class="pl-3 border-l-2 border-black">
      <div class="text-sm font-bold">curl — バグバウンティを終了（2026年1月）</div>
      <div class="text-xs opacity-60">AI生成の偽レポートが殺到。本物の脆弱性報告は約5%、6年間でAI製レポートが真の脆弱性を見つけたことは一度もない</div>
    </div>
    <div class="pl-3 border-l-2 border-gray-300">
      <div class="text-sm font-bold">HackerOne — AI関連の脆弱性報告が前年比 +210%</div>
      <div class="text-xs opacity-60">トリアージ（選別）する人間の処理能力が、報告の洪水に追いつかない</div>
    </div>
    <div class="pl-3 border-l-2 border-gray-300">
      <div class="text-sm font-bold">Code4rena — 監査コンペ大手が事業縮小を発表（2026年5月）</div>
      <div class="text-xs opacity-60">人手による単発・静的な監査モデルそのものが、持続性の限界に直面</div>
    </div>
  </div>
</div>

</div>

<div class="mt-5 pt-4 border-t border-gray-200 text-center">
  <div class="text-base font-bold">静的・人的・単発のセキュリティは、最も必要なときに限界を迎えている。<strong>動的・自律的・永続的</strong>な公共財が要る。</div>
</div>

<SourceCite :sources="[
  { label: 'Chainalysis 2026 (Crypto Theft Report)', url: 'https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/' },
  { label: 'Immunefi Bug Bounty Scope (out-of-scope例)', url: 'https://immunefi.com/bug-bounty/veda/information/' },
  { label: 'curl — Death by a thousand slops', url: 'https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/' },
  { label: 'curl ends bug bounty (BleepingComputer)', url: 'https://www.bleepingcomputer.com/news/security/curl-ending-bug-bounty-program-after-flood-of-ai-slop-reports/' },
  { label: 'HackerOne — 210% spike in AI vuln reports', url: 'https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy' },
  { label: 'Code4rena wind-down (Crypto Times)', url: 'https://www.cryptotimes.io/2026/05/13/code4rena-announces-wind-down-after-securing-billions-in-defi/' }
]" />

<!--
Speaker Notes:
最初の課題です。2025年単年で、ハッキングにより34億ドル超の暗号資産が盗まれました。Bybitの一件だけで15億ドルです。しかも厄介なのは、最も損害の大きいタイプの攻撃——MEV、オラクル価格操作、取引順序の操作、経済・ガバナンス攻撃——が、多くのバグバウンティで明示的に「対象外」とされている点です。つまり、監査も形式検証もバグバウンティも尽くしているのに、一番損害の大きい動的・経済的な脆弱性を、誰も体系的には検査していない。さらに、守る側の人手のモデル自体が壊れ始めています。curlはAI生成の偽レポートの殺到に耐えきれず、2026年1月にバグバウンティを終了しました。本物の報告はわずか5%、6年間でAI製レポートが真の脆弱性を見つけたことは一度もありません。HackerOneではAI関連の脆弱性報告が前年比210%増。監査コンペ大手のCode4renaも2026年5月に事業縮小を発表しています。静的・人的・単発のセキュリティは、最も必要とされるこのタイミングで限界を迎えている。だからこそ、動的・自律的・永続的な公共財が必要なのです。
-->
