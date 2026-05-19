---
layout: default
---

# AIエージェントが実経済に出てくる — なのに、安全に試す場所がない

<div class="grid grid-cols-[0.85fr_1.15fr] gap-7 mt-6 items-center">

<div>
  <div class="text-xs uppercase tracking-widest opacity-40 mb-1">AIエージェントが仲介するB2B支出</div>
  <div class="text-7xl font-bold leading-none" style="font-family: 'BIZ UDPMincho', serif;">$15T</div>
  <div class="text-xs opacity-50 mt-2">2028年予測（Gartner）。2030年には金融取引の20%がプログラマブルに</div>
</div>

<div class="pay">
  <div class="pay-flow">
    <span class="pay-node">AI</span>
    <span class="pay-arrow">— ¥ →</span>
    <span class="pay-node">AI</span>
  </div>
  <div>
    <div class="text-sm font-bold mb-1">AIは、人間を介さず支払い始めた</div>
    <div class="flex flex-wrap gap-1.5 mb-1">
      <span class="pay-tag">Google AP2（60社以上）</span>
      <span class="pay-tag">x402（Coinbase × EF × MetaMask）</span>
    </div>
    <div class="text-xs opacity-55">AIエージェントがエージェントに決済する仕組みは、<strong>もう動いている</strong>。</div>
  </div>
</div>

</div>

<div class="grid grid-cols-2 gap-4 mt-6">
  <div class="gp">
    <div class="gp-h">エージェント同士は、欺き合える</div>
    <div class="gp-n">Sumsubは「<strong>機械が機械を騙す</strong> agentic AI 詐欺が2026年に急増する」と警告。</div>
  </div>
  <div class="gp gp-hi">
    <div class="gp-h">本番で試すしかない、という空白</div>
    <div class="gp-n">本物のインセンティブ下で、AI同士が取引・攻撃・検証し合う<strong>公共の実環境が存在しない</strong>。</div>
  </div>
</div>

<div class="mt-5 conc">本番にお金が流れる前に、AIを<strong>安全に戦わせ・確かめる「実環境」</strong>が要る。</div>

<style>
.pay { display: flex; gap: 14px; align-items: center; border: 2px solid #111; border-radius: 0.6rem; padding: 0.85rem 1rem; }
.pay-flow { display: flex; align-items: center; gap: 6px; flex-shrink: 0; }
.pay-node { font-family: 'BIZ UDPMincho', serif; font-size: 13px; font-weight: 700; border: 2px solid #111; border-radius: 50%; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; }
.pay-arrow { font-size: 11px; font-weight: 700; opacity: 0.6; }
.pay-tag { font-size: 10.5px; padding: 2px 9px; border: 1px solid #d4d4d4; border-radius: 999px; }
.gp { border: 1px solid #e5e7eb; border-radius: 0.5rem; padding: 0.8rem 1rem; }
.gp.gp-hi { border: 2px solid #111; }
.gp-h { font-size: 14px; font-weight: 700; font-family: 'BIZ UDPMincho', serif; margin-bottom: 0.3rem; }
.gp-n { font-size: 11px; line-height: 1.6; opacity: 0.7; }
.conc { text-align: center; font-size: 15px; font-weight: 700; font-family: 'BIZ UDPMincho', serif; border-top: 2px solid #111; padding-top: 0.7rem; }
</style>

<SourceCite :sources="[
  { label: 'Gartner — AI agents $15T B2B spend by 2028', url: 'https://www.digitalcommerce360.com/2025/11/28/gartner-ai-agents-15-trillion-in-b2b-purchases-by-2028/' },
  { label: 'Google — Agent Payments Protocol (AP2)', url: 'https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol' },
  { label: 'Coinbase × Google — A2A x402', url: 'https://www.coinbase.com/developer-platform/discover/launches/google_x402' },
  { label: 'Sumsub Identity Fraud Report 2025-2026', url: 'https://www.prnewswire.com/news-releases/sumsubs-annual-report-fraud-shifts-to-complex-multi-step-schemes-in-2025-agentic-ai-scams-poised-to-surge-in-2026-302625287.html' }
]" />

<!--
Speaker Notes:
二つ目の課題です。AIエージェントは、もう本物のお金を動かし始めています。GartnerはAIエージェントが2028年までにB2B支出の15兆ドル超を仲介し、2030年には金融取引の2割がプログラマブルになると予測。GoogleはAP2を60社以上と発表し、Coinbase・イーサリアム財団・MetaMaskのx402では、AIエージェントが人間を介さず別のエージェントに支払います。AIエージェント経済は、構想ではなく進行中の現実です。問題は二つ。一つ、自律エージェントは互いを欺き合えます。Sumsubは「機械が機械を騙す」agentic AI詐欺が2026年に急増すると警告しています。二つ、にもかかわらず、本物のインセンティブの下でAI同士が取引・攻撃・検証し合い、本番前に試される公共の実環境が存在しません。本番にお金が流れる前に、AIを安全に戦わせ、確かめる実環境が必要です。
-->
