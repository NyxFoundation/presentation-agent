---
layout: default
---

<div class="nx-kicker">インサイト ／ Eris</div>
<h1 class="nx-display">作り物でない市場で、<em>理論を再現した</em>。</h1>

<div class="cv"><svg class="cv-svg" viewBox="0 0 980 400" preserveAspectRatio="xMidYMid meet"><defs><marker id="fl-ar" markerWidth="10" markerHeight="10" refX="6.5" refY="3.4" orient="auto"><path d="M0,0 L7,3.4 L0,6.8 Z" fill="var(--accent)"/></marker></defs><rect x="24" y="64" width="300" height="120" rx="10" class="p-box"/><text x="40" y="90" class="p-head">AI trading bot 研究</text><text x="40" y="116" class="p-body">個のリターン（Sharpe 等）を競う</text><text x="40" y="139" class="p-limit">系全体（マクロ）は見ない</text><text x="40" y="170" class="p-tag">TradingAgents · AlphaAgent</text><rect x="24" y="210" width="300" height="120" rx="10" class="p-box"/><text x="40" y="236" class="p-head">LLM 経済シミュ研究</text><text x="40" y="262" class="p-body">作り物の市場で創発を見せる</text><text x="40" y="285" class="p-limit">検証は擬似的・現実に転移しにくい</text><text x="40" y="316" class="p-tag">TwinMarket · ABM-LLM</text><line x1="324" y1="124" x2="596" y2="152" class="flow-arrow" marker-end="url(#fl-ar)"/><line x1="324" y1="270" x2="596" y2="254" class="flow-arrow" marker-end="url(#fl-ar)"/><rect x="402" y="112" width="118" height="17" rx="3" class="flow-chip"/><text x="461" y="124" class="flow-lbl" text-anchor="middle">＋ 系全体＝マクロ</text><rect x="400" y="246" width="124" height="17" rx="3" class="flow-chip"/><text x="462" y="258" class="flow-lbl" text-anchor="middle">＋ 本物の機構・転移</text><rect x="600" y="92" width="356" height="224" rx="10" class="p-box-hl"/><text x="622" y="126" class="p-eris-h">Eris</text><text x="622" y="158" class="p-body">本物の DeFi 機構で、AIエージェント</text><text x="622" y="178" class="p-body">同士の敵対競争を再現。</text><text x="622" y="216" class="p-eris-big">→ 理論を再現した</text><text x="622" y="250" class="p-sub">alpha decay・crowding・〈守り〉が、</text><text x="622" y="268" class="p-sub">本物の機構から “創発” した。</text><line x1="24" y1="350" x2="956" y2="350" class="foot-div"/><text x="24" y="371" class="nov-h">DeFi だからできた</text><text x="172" y="371" class="nov">── 作り物のマクロは“仮定”が混じる。本物の機構から創発したマクロは、現実に転移する。</text></svg></div>

<style>
.cv { display: flex; justify-content: center; margin-top: 0.4rem; }
.cv-svg { width: 100%; max-width: 940px; height: auto; }
.p-box { fill: #fff; stroke: var(--line-strong); stroke-width: 1.2; }
.p-box-hl { fill: var(--bg-2); stroke: var(--accent); stroke-width: 2; }
.p-head { font-family: var(--font-jp-serif); font-size: 13px; font-weight: 700; fill: var(--ink); }
.p-body { font-family: var(--font-jp-serif); font-size: 12.5px; fill: var(--ink-dim); }
.p-limit { font-family: var(--font-jp-serif); font-size: 12px; fill: var(--severe); }
.p-tag { font-family: var(--font-mono); font-size: 9px; fill: var(--ink-faint); letter-spacing: 0.02em; }
.p-eris-h { font-family: var(--font-mono); font-size: 13px; font-weight: 700; fill: var(--accent); letter-spacing: 0.18em; }
.p-eris-big { font-family: var(--font-jp-serif); font-size: 21px; font-weight: 800; fill: var(--accent); }
.p-sub { font-family: var(--font-jp-serif); font-size: 11px; fill: var(--ink-dim); }
.flow-arrow { stroke: var(--accent); stroke-width: 2.2; fill: none; }
.flow-chip { fill: var(--bg); }
.flow-lbl { font-family: var(--font-jp-serif); font-size: 11px; font-weight: 700; fill: var(--accent); }
.foot-div { stroke: var(--line); stroke-width: 1; }
.nov-h { font-family: var(--font-mono); font-size: 10px; font-weight: 700; fill: var(--accent); letter-spacing: 0.04em; }
.nov { font-family: var(--font-jp-serif); font-size: 11.5px; fill: var(--ink-dim); }
</style>

<!--
Speaker Notes:
- p15 の主張：本物の DeFi オンチェーンで AIエージェント同士の敵対競争を再現 → 理論（alpha decay・crowding・〈守り〉）を再現。かつ先行2系統を超える
- vs AI trading bot 研究（TradingAgents 2412.20138 / AlphaAgent 2502.16789）：個のリターンしか見ない → Eris は系全体＝マクロも可視化
- vs LLM 経済シミュ研究（TwinMarket 2025 / ABM-LLM 2510.12189）：作り物の市場で創発は見せるが検証は擬似的・転移しにくい → Eris は本物の機構・本物の検証・現実への転移
- DeFi だからできたこと（footer・認識論キッカー）：シミュのマクロは作った人の“仮定”が半分仕込まれる。DeFi のマクロは本物のコントラクト機構（AMM式・清算・MEV入札・gas・revert）から“創発”する。だから理論の再現が本物の証拠になり、現実に転移する
- 正直な範囲：Eris は本物のコントラクトコード＋実行意味論で動く“閉じた経済”。「本物の機構・本物の検証」までは強く言え、「mainnet で実マネー」とは言い過ぎない（外部流動性まで現実かは設計次第）
- 考察・仮説（AIエージェントならではの戦略性／多様性とトークン経済）は次ページ p16 へ
-->
