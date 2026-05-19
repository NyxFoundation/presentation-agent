---
layout: default
---

# "It runs" is not "it's safe" — the machinery for verifying that is breaking down

<div class="grid grid-cols-[0.85fr_1.15fr] gap-7 mt-6 items-center">

<div>
  <div class="text-xs uppercase tracking-widest opacity-40 mb-1">Crypto stolen in 2025</div>
  <div class="text-7xl font-bold leading-none" style="font-family: 'BIZ UDPMincho', serif;">$3.4B</div>
  <div class="text-xs opacity-50 mt-2">$1.5B from the Bybit breach alone (Chainalysis 2026)</div>
</div>

<div class="oos">
  <div class="oos-x">Out of<br/>scope</div>
  <div>
    <div class="text-sm font-bold mb-1">The most damaging attacks aren't even being inspected</div>
    <div class="flex flex-wrap gap-1.5 mb-1">
      <span class="oos-tag">MEV</span>
      <span class="oos-tag">Oracle price manipulation</span>
      <span class="oos-tag">Transaction reordering</span>
      <span class="oos-tag">Economic & governance attacks</span>
    </div>
    <div class="text-xs opacity-55">These dynamic, economic vulnerabilities are <strong>explicitly out of scope</strong> in most bug bounties.</div>
  </div>
</div>

</div>

<div class="text-xs uppercase tracking-widest opacity-40 mt-7 mb-3">And the human defense net itself has begun to collapse</div>
<div class="grid grid-cols-3 gap-4">
  <div class="cl">
    <div class="cl-name">curl</div>
    <div class="cl-fact">Bug bounty <strong>ended</strong></div>
    <div class="cl-n">Flooded by AI-fabricated reports — only ~5% genuine (Jan 2026)</div>
  </div>
  <div class="cl">
    <div class="cl-name">HackerOne</div>
    <div class="cl-fact">AI-related reports <strong>+210%</strong></div>
    <div class="cl-n">Human triage cannot keep up with the flood of reports</div>
  </div>
  <div class="cl">
    <div class="cl-name">Code4rena</div>
    <div class="cl-fact">A major audit platform <strong>winding down</strong></div>
    <div class="cl-n">The human, one-shot, static audit model has hit its limit (May 2026)</div>
  </div>
</div>

<style>
.oos { display: flex; gap: 12px; align-items: center; border: 2px solid #c63a3a; border-radius: 0.6rem; padding: 0.85rem 1rem; }
.oos-x { font-family: 'BIZ UDPMincho', serif; font-size: 13px; font-weight: 700; color: #c63a3a; border: 2px solid #c63a3a; border-radius: 6px; padding: 4px 8px; flex-shrink: 0; text-align: center; line-height: 1.2; }
.oos-tag { font-size: 10.5px; padding: 2px 9px; border: 1px solid #d4d4d4; border-radius: 999px; }
.cl { border: 1px solid #e5e7eb; border-top: 4px solid #c63a3a; border-radius: 0.5rem; padding: 0.6rem 0.8rem; }
.cl-name { font-size: 12px; font-weight: 700; opacity: 0.5; letter-spacing: 0.04em; }
.cl-fact { font-size: 15px; font-weight: 700; font-family: 'BIZ UDPMincho', serif; margin: 0.15rem 0 0.3rem; }
.cl-n { font-size: 10px; line-height: 1.55; opacity: 0.6; }
</style>

<SourceCite :sources="[
  { label: 'Chainalysis 2026', url: 'https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/' },
  { label: 'Immunefi Bug Bounty Scope (out-of-scope example)', url: 'https://immunefi.com/bug-bounty/veda/information/' },
  { label: 'curl — Death by a thousand slops', url: 'https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/' },
  { label: 'HackerOne — 210% spike in AI vuln reports', url: 'https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy' },
  { label: 'Code4rena wind-down (Crypto Times)', url: 'https://www.cryptotimes.io/2026/05/13/code4rena-announces-wind-down-after-securing-billions-in-defi/' }
]" />

<!--
Speaker Notes:
The first problem. In 2025 alone, more than $3.4B in crypto assets was stolen through hacks — $1.5B from the Bybit breach alone. The troubling part is that the most damaging attacks — MEV, oracle price manipulation, transaction reordering, economic and governance attacks — are explicitly "out of scope" in most bug bounties. The dynamic, economic vulnerabilities that do the most damage are not being systematically inspected by anyone. On top of that, the human model on the defending side has itself begun to collapse. curl ended its bug bounty in January 2026 under a flood of AI-fabricated reports — only about 5% were genuine. At HackerOne, AI-related vulnerability reports rose 210% year over year. Code4rena, a major audit-contest platform, announced it is winding down in May 2026. Static, human, one-shot security has hit its limit. We need a dynamic, autonomous, permanent public good.
-->
