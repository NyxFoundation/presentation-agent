---
layout: default
---

<div class="nx-kicker">インサイト ／ Eris</div>
<h1 class="nx-display">Eris が埋めるのは、<em>理論 × 現実</em>の空白。</h1>

<div class="cv"><svg class="cv-svg" viewBox="0 0 980 300" preserveAspectRatio="xMidYMid meet"><rect x="215" y="145" width="275" height="121" class="qm-eris-zone"/><line x1="205" y1="145" x2="775" y2="145" class="qm-axis"/><line x1="490" y1="16" x2="490" y2="274" class="qm-axis"/><text x="196" y="150" class="qm-axlbl" text-anchor="end">理論</text><text x="784" y="150" class="qm-axlbl" text-anchor="start">実装</text><text x="490" y="9" class="qm-axlbl" text-anchor="middle">モデル</text><text x="490" y="289" class="qm-axlbl" text-anchor="middle">現実</text><circle cx="348" cy="66" r="4" class="qm-dot"/><text x="348" y="90" class="qm-name" text-anchor="middle">経済モデルの古典</text><text x="348" y="105" class="qm-tag" text-anchor="middle">Minority Game · El Farol</text><circle cx="634" cy="66" r="4" class="qm-dot"/><text x="634" y="90" class="qm-name" text-anchor="middle">LLM 経済シミュ</text><text x="634" y="105" class="qm-tag" text-anchor="middle">TwinMarket · ABM-LLM</text><circle cx="634" cy="196" r="4" class="qm-dot"/><text x="634" y="220" class="qm-name" text-anchor="middle">AI trading bot</text><text x="634" y="235" class="qm-tag" text-anchor="middle">TradingAgents · AlphaAgent</text><circle cx="350" cy="184" r="11" class="qm-eris-ring"/><circle cx="350" cy="184" r="4.5" class="qm-eris-core"/><text x="350" y="214" class="qm-eris" text-anchor="middle">Eris</text><text x="350" y="233" class="qm-eris-desc" text-anchor="middle">理論を現実で再現</text></svg></div>

<div class="fwd">ここから問う ── この<b>現実の検証環境</b>で、<em>意図と検証</em>をどこまで洗練できるか。</div>

<SourceCite :sources="[
  { label: 'TradingAgents — AI trading bot（arXiv 2412.20138）', url: 'https://arxiv.org/abs/2412.20138' },
  { label: 'AlphaAgent — alpha decay（arXiv 2502.16789）', url: 'https://arxiv.org/abs/2502.16789' },
  { label: 'TwinMarket — LLM 市場シミュ, NeurIPS 2025（arXiv 2502.01506）', url: 'https://arxiv.org/abs/2502.01506' },
  { label: 'Agent-Based Simulation of a Financial Market with LLMs（arXiv 2510.12189）', url: 'https://arxiv.org/abs/2510.12189' },
  { label: 'Minority Game — Challet & Zhang 1997 ／ El Farol — Arthur 1994', url: 'https://ideas.repec.org/a/eee/phsmap/v246y1997i3p407-418.html' }
]" />

<style>
.cv { display: flex; justify-content: center; margin-top: 0.5rem; }
.cv-svg { width: 100%; max-width: 820px; height: auto; }
.qm-axis { stroke: var(--line-strong); stroke-width: 1.2; }
.qm-axlbl { font-family: var(--font-mono); font-size: 12px; font-weight: 700; fill: var(--ink-dim); letter-spacing: 0.08em; }
.qm-eris-zone { fill: var(--accent-soft); }
.qm-dot { fill: var(--ink-faint); }
.qm-name { font-family: var(--font-jp-serif); font-size: 13px; font-weight: 700; fill: var(--ink); }
.qm-tag { font-family: var(--font-mono); font-size: 8.5px; fill: var(--ink-faint); letter-spacing: 0.01em; }
.qm-eris-ring { fill: none; stroke: var(--accent); stroke-width: 2; }
.qm-eris-core { fill: var(--accent); }
.qm-eris { font-family: var(--font-jp-serif); font-size: 17px; font-weight: 800; fill: var(--accent); }
.qm-eris-desc { font-family: var(--font-jp-serif); font-size: 11.5px; font-weight: 600; fill: var(--accent); }
.fwd { display: flex; justify-content: center; margin: 0.8rem auto 0; max-width: 820px; padding: 0.5rem 0.9rem; background: var(--bg-2); border-left: 2px solid var(--accent); font-family: var(--font-jp-serif); font-size: 15px; color: var(--ink-dim); }
.fwd b { color: var(--ink); font-weight: 700; }
.fwd em { color: var(--accent); font-style: normal; font-weight: 700; }
</style>

<!--
Speaker Notes:
- 4象限マップ：横＝理論↔実装、縦＝モデル↔現実
  - 理論×モデル：経済モデルの古典（Minority Game 1997 / El Farol 1994）
  - 実装×モデル：LLM 経済シミュ（TwinMarket 2502.01506 / ABM-LLM 2510.12189）── 作り物の市場
  - 実装×現実：AI trading bot（TradingAgents 2412.20138 / AlphaAgent 2502.16789）── 実データだが理論は検証しない
  - 理論×現実：Eris ── 本物の DeFi 機構で理論（alpha decay・crowding・〈守り〉）を再現。ここが空いていた象限
- 「マクロも測れる」等は明言しない。視聴者に空白象限から気付かせる
- 前向きの接続：この現実の検証環境を土台に、意図（事前設計）と検証（事後検知）をどこまで洗練できるか ＝ デッキの 意図/検証 ループ（SL09・実験設定）へ戻す
- 正直な範囲：本物のコントラクトコード＋実行意味論で動く“閉じた経済”。「本物の機構・本物の検証」までは強く言え、外部流動性まで現実かは設計次第
- 考察・仮説（AIエージェントならではの戦略性／多様性とトークン経済）は次ページ p16 へ
-->
