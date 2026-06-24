---
layout: default
---

<div class="nx-kicker">インサイト ／ Eris</div>
<h1 class="nx-display">賢いAIほど、<em>新しい儲けより〈守り〉</em>を選ぶ。</h1>

<div class="cv"><svg class="cv-svg" viewBox="0 0 980 408" preserveAspectRatio="xMidYMid meet"><defs><marker id="fl-ar" markerWidth="10" markerHeight="10" refX="6.5" refY="3.4" orient="auto"><path d="M0,0 L7,3.4 L0,6.8 Z" fill="var(--accent)"/></marker></defs><rect x="22" y="68" width="280" height="304" rx="10" class="p-box"/><text x="40" y="98" class="p-head">① 先行研究で言われてきた</text><line x1="40" y1="108" x2="284" y2="108" class="p-rule"/><text x="40" y="146" class="p-find">儲け口は、競争ですぐ枯れる</text><text x="40" y="163" class="p-tag">AIに売買させる研究</text><text x="40" y="206" class="p-find">バブルや暴落がひとりでに起きる</text><text x="40" y="223" class="p-tag">市場をAIで丸ごと再現</text><text x="40" y="266" class="p-find">儲けの奪い合いは早い者勝ち</text><text x="40" y="283" class="p-tag">経済モデルの古典</text><line x1="304" y1="220" x2="346" y2="220" class="flow-arrow" marker-end="url(#fl-ar)"/><rect x="300" y="204" width="50" height="16" rx="3" class="flow-chip"/><text x="325" y="216" class="flow-lbl" text-anchor="middle">本物の市場で</text><rect x="350" y="68" width="280" height="304" rx="10" class="p-box-hl"/><text x="368" y="98" class="p-head-a">② Eris が本物の市場で確かめた</text><line x1="368" y1="108" x2="612" y2="108" class="p-rule-a"/><text x="368" y="144" class="p-body">① の予測を、本物の DeFi 市場で再現。</text><text x="368" y="186" class="p-body">敵対競争 ＋ 本物の損益・失敗tx で、</text><text x="368" y="204" class="p-body">自己改善の〈向き〉を初めて実測。</text><text x="368" y="256" class="p-result">→ 賢いAIも〈守り〉に入る</text><text x="368" y="278" class="p-sub">新しい儲けより、危ない手を控える</text><line x1="632" y1="220" x2="674" y2="220" class="flow-arrow" marker-end="url(#fl-ar)"/><rect x="628" y="204" width="50" height="16" rx="3" class="flow-chip"/><text x="653" y="216" class="flow-lbl" text-anchor="middle">次の問いへ</text><rect x="678" y="68" width="280" height="304" rx="10" class="p-box-fwd"/><text x="696" y="98" class="p-head-a">③ Eris なら、これも測れる</text><line x1="696" y1="108" x2="940" y2="108" class="p-rule-a"/><text x="696" y="146" class="p-body">理論では言われるが、</text><text x="696" y="164" class="p-body">まだ誰も測っていないこと：</text><text x="696" y="206" class="p-q">「みんなが同時に守ったら、</text><text x="696" y="224" class="p-q">　市場は一気に細る？」</text><text x="696" y="268" class="p-fwd">→ Eris なら、実際に測れる。</text></svg></div>

<style>
.cv { display: flex; justify-content: center; margin-top: 0.4rem; }
.cv-svg { width: 100%; max-width: 940px; height: auto; }
.p-box { fill: #fff; stroke: var(--line-strong); stroke-width: 1.2; }
.p-box-hl { fill: var(--bg-2); stroke: var(--accent); stroke-width: 2; }
.p-box-fwd { fill: #fff; stroke: var(--accent); stroke-width: 1.5; stroke-dasharray: 6 4; }
.p-head { font-family: var(--font-jp-serif); font-size: 13px; font-weight: 700; fill: var(--ink-dim); }
.p-head-a { font-family: var(--font-jp-serif); font-size: 13px; font-weight: 700; fill: var(--accent); }
.p-rule { stroke: var(--line); stroke-width: 1; }
.p-rule-a { stroke: var(--accent-line); stroke-width: 1; }
.p-find { font-family: var(--font-jp-serif); font-size: 12.5px; font-weight: 600; fill: var(--ink); }
.p-tag { font-family: var(--font-mono); font-size: 9px; fill: var(--ink-faint); letter-spacing: 0.02em; }
.p-body { font-family: var(--font-jp-serif); font-size: 12px; fill: var(--ink-dim); }
.p-result { font-family: var(--font-jp-serif); font-size: 15px; font-weight: 800; fill: var(--accent); }
.p-sub { font-family: var(--font-jp-serif); font-size: 10px; fill: var(--ink-dim); }
.p-q { font-family: var(--font-jp-serif); font-size: 12px; fill: var(--ink); }
.p-fwd { font-family: var(--font-jp-serif); font-size: 14px; font-weight: 800; fill: var(--accent); }
.flow-arrow { stroke: var(--accent); stroke-width: 2.2; fill: none; }
.flow-chip { fill: var(--bg); }
.flow-lbl { font-family: var(--font-jp-serif); font-size: 10px; font-weight: 700; fill: var(--accent); }
</style>

<!--
Speaker Notes:
- 構造を「収束」から「左→右の流れ」に変更：先行研究（理論・部分実証）→ Eris が本物の市場で再現＋実測 → 理論止まりも Eris で測れる（前向き）
- ① 先行研究（平易化／正確な中身は口頭）:
  - AIに売買させる研究（TradingAgents 2412.20138 / AlphaAgent 2502.16789）：α はすぐ decay。多くは backtest 止まり
  - 市場をAIで再現（TwinMarket 2025 / ABM-LLM 2510.12189）：バブル・群集が創発。報酬は擬似的
  - 経済モデルの古典（Minority Game: Challet–Zhang 1997 / El Farol: Arthur 1994）：希少資源の競争＝crowding・分散縮小
- ② Eris の貢献＝「再現」かつ「強化」：①の予測を本物の DeFi 市場（敵対競争・MEV・本物の PnL/revert・Self–Frozen 統制）で再現し、さらに「自己改善の“向き”」という新しい量を実測。結果＝賢いAIも守り（リスク削減・取引の選別）に入る
- ③ 前向き：理論では言われるが未測定のこと（自制の相関＝一斉退避・流動性枯れ）も、Eris は実機で測れる。severe の不安でなく、capability として提示
- 正直な穴：n 小・1 regime・0.00 戦略の正体未確定・operator が LLM か heuristic か
-->
