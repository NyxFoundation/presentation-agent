---
layout: default
---

<div class="nx-kicker">インサイト ／ Eris</div>
<h1 class="nx-display">賢いAIでも、<em>経済の法則からは逃げられない</em>。</h1>

<div class="cv"><svg class="cv-svg" viewBox="0 0 980 400" preserveAspectRatio="xMidYMid meet"><line x1="190" y1="200" x2="790" y2="200" class="qm-axis"/><line x1="490" y1="36" x2="490" y2="364" class="qm-axis"/><text x="180" y="205" class="qm-axlbl" text-anchor="end">協調・単体</text><text x="800" y="205" class="qm-axlbl" text-anchor="start">敵対競争</text><text x="490" y="28" class="qm-axlbl" text-anchor="middle">モデル</text><text x="490" y="384" class="qm-axlbl" text-anchor="middle">現実</text><circle cx="338" cy="86" r="4.5" class="qm-dot"/><text x="338" y="112" class="qm-name" text-anchor="middle">LLM 経済シミュ</text><text x="338" y="131" class="qm-find" text-anchor="middle">AIの群れからバブル・暴落が創発</text><text x="338" y="149" class="qm-tag" text-anchor="middle">TwinMarket · ABM-LLM</text><circle cx="642" cy="86" r="4.5" class="qm-dot"/><text x="642" y="112" class="qm-name" text-anchor="middle">経済モデルの古典</text><text x="642" y="131" class="qm-find" text-anchor="middle">競争で混雑し、効率が落ちる</text><text x="642" y="149" class="qm-tag" text-anchor="middle">Minority Game · El Farol</text><circle cx="338" cy="250" r="4.5" class="qm-dot"/><text x="338" y="276" class="qm-name" text-anchor="middle">AI trading bot</text><text x="338" y="295" class="qm-find" text-anchor="middle">儲け口を狙うが、競争で枯れる</text><text x="338" y="313" class="qm-tag" text-anchor="middle">TradingAgents · AlphaAgent</text><rect x="508" y="246" width="268" height="94" rx="10" class="qm-eris-card"/><image href="/logos/eris_logo.svg" x="600" y="256" width="84" height="31"/><text x="642" y="307" class="qm-eris-desc" text-anchor="middle">本物の敵対競争で、理論を再現</text><text x="642" y="326" class="qm-eris-why" text-anchor="middle">── 勝つAIほど、危ない取引を減らしたから</text></svg></div>

<SourceCite :sources="[
  { label: 'TradingAgents — AI trading bot（arXiv 2412.20138）', url: 'https://arxiv.org/abs/2412.20138' },
  { label: 'AlphaAgent — alpha decay（arXiv 2502.16789）', url: 'https://arxiv.org/abs/2502.16789' },
  { label: 'TwinMarket — LLM 市場シミュ, NeurIPS 2025（arXiv 2502.01506）', url: 'https://arxiv.org/abs/2502.01506' },
  { label: 'Agent-Based Simulation of a Financial Market with LLMs（arXiv 2510.12189）', url: 'https://arxiv.org/abs/2510.12189' },
  { label: 'Minority Game — Challet & Zhang 1997 ／ El Farol — Arthur 1994', url: 'https://ideas.repec.org/a/eee/phsmap/v246y1997i3p407-418.html' }
]" />

<style>
.cv { display: flex; justify-content: center; margin-top: 0.55rem; }
.cv-svg { width: 100%; max-width: 880px; height: auto; }
.qm-axis { stroke: var(--line-strong); stroke-width: 1.2; }
.qm-axlbl { font-family: var(--font-mono); font-size: 13px; font-weight: 700; fill: var(--ink-dim); letter-spacing: 0.06em; }
.qm-dot { fill: var(--ink-faint); }
.qm-name { font-family: var(--font-jp-serif); font-size: 14px; font-weight: 700; fill: var(--ink); }
.qm-find { font-family: var(--font-jp-serif); font-size: 12px; fill: var(--ink-dim); }
.qm-tag { font-family: var(--font-mono); font-size: 9px; fill: var(--ink-faint); letter-spacing: 0.01em; }
.qm-eris-card { fill: var(--accent-soft); stroke: var(--accent); stroke-width: 1.5; }
.qm-eris-desc { font-family: var(--font-jp-serif); font-size: 12.5px; font-weight: 700; fill: var(--accent); }
.qm-eris-why { font-family: var(--font-jp-serif); font-size: 11px; fill: var(--ink-dim); }
</style>

<!--
Speaker Notes:
- 4象限マップ：横＝協調・単体 ↔ 敵対競争、縦＝モデル ↔ 現実。各点に「研究名＋示したこと」
  - 協調×モデル：LLM 経済シミュ（TwinMarket 2502.01506 / ABM-LLM 2510.12189）── 作り物の市場でバブル創発
  - 敵対×モデル：経済モデルの古典（Minority Game 1997 / El Farol 1994）── 競争で混雑・非効率
  - 協調×現実：AI trading bot（TradingAgents 2412.20138 / AlphaAgent 2502.16789）── 実データだが単体/協調、α はすぐ decay
  - 敵対×現実：Eris ── 多数の独立戦略が本物の DeFi 機構で敵対競争。ここが空いていた角
- 横軸を「理論↔実装」から「敵対競争の度合い」に変更した理由：理論↔実装だと Eris が中間に落ちて曖昧。敵対競争軸なら Eris が現実×敵対の角を独占でき、「Eris＝Minority Game を本物にした」対角ストーリーが立つ
- 「理論を再現」は軸でなく Eris の点の所見に（軸＝環境特徴、点＝示したこと）
- 「マクロも測れる」等は明言しない。視聴者に空き角から気付かせる
- 考察・仮説（AIエージェントならではの戦略性／多様性とトークン経済）は次ページ p16 へ
-->
