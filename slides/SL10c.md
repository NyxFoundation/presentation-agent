---
layout: default
---

<div class="nx-kicker">インサイト ／ Eris</div>
<h1 class="nx-display">競争するAIは、<em>儲け方より損の減らし方</em>を学ぶ。</h1>

<div class="in"><svg class="in-svg" viewBox="0 0 980 372" preserveAspectRatio="xMidYMid meet"><defs><marker id="in-ar" markerWidth="10" markerHeight="10" refX="6.5" refY="3.4" orient="auto"><path d="M0,0 L7,3.4 L0,6.8 Z" fill="var(--severe)"/></marker></defs><rect x="36" y="38" width="392" height="216" rx="12" class="card-a"/><text x="60" y="70" class="hd-a">個体レベル</text><text x="146" y="70" class="hd-note">── AI は自分を絞る</text><text x="60" y="102" class="bd">閾値を上げ・サイズを下げ・slippage を締める</text><text x="60" y="122" class="tiny">勝ち戦略 crossvenue / cvbal に共通の調整</text><text x="60" y="150" class="bd">危険な変更は rollback で即時に撤回する</text><line x1="60" y1="172" x2="404" y2="172" class="divider"/><text x="60" y="210" class="big-a">取引を自分から絞る</text><text x="60" y="236" class="sub">＝ 個体は自制する（安心材料）</text><rect x="552" y="38" width="392" height="216" rx="12" class="card-s"/><text x="576" y="70" class="hd-s">系全体</text><text x="640" y="70" class="hd-note">── 一斉に起きると</text><text x="576" y="102" class="bd">その守り（de-risk）が戦略間でそろい</text><text x="576" y="128" class="bd">流動性が一度に引き上がる</text><line x1="576" y1="172" x2="920" y2="172" class="divider"/><text x="576" y="210" class="big-s">流動性が枯れる</text><text x="576" y="236" class="sub">＝ 未解決の systemic risk（本丸）</text><text x="490" y="104" class="pivot" text-anchor="middle">全員が</text><text x="490" y="122" class="pivot" text-anchor="middle">同時だと</text><line x1="432" y1="150" x2="546" y2="150" class="arrow" marker-end="url(#in-ar)"/><line x1="36" y1="302" x2="944" y2="302" class="foot-div"/><text x="36" y="326" class="foot-h">理論が予測 → Eris が実証</text><text x="36" y="350" class="foot">El Farol・Minority Game（&#39;94–97）と Generation–Verification Gap（ICLR&#39;25）の予測を、敵対競争＋本物の検証信号＋Self／Frozen 比較で初めて実機実証した。</text></svg></div>

<style>
.in { display: flex; justify-content: center; margin-top: 0.45rem; }
.in-svg { width: 100%; max-width: 930px; height: auto; }
.card-a { fill: #f4f7fa; stroke: var(--accent); stroke-width: 1.6; }
.card-s { fill: #fbf4f1; stroke: var(--severe); stroke-width: 1.6; }
.hd-a { font-family: var(--font-mono); font-size: 13px; font-weight: 700; letter-spacing: 0.06em; fill: var(--accent); }
.hd-s { font-family: var(--font-mono); font-size: 13px; font-weight: 700; letter-spacing: 0.06em; fill: var(--severe); }
.hd-note { font-family: var(--font-jp-serif); font-size: 12.5px; fill: var(--ink-faint); }
.bd { font-family: var(--font-jp-serif); font-size: 14.5px; fill: var(--ink); }
.tiny { font-family: var(--font-mono); font-size: 10px; fill: var(--ink-faint); letter-spacing: 0.01em; }
.divider { stroke: var(--line); stroke-width: 1; }
.big-a { font-family: var(--font-jp-serif); font-size: 23px; font-weight: 800; fill: var(--accent); }
.big-s { font-family: var(--font-jp-serif); font-size: 23px; font-weight: 800; fill: var(--severe); }
.sub { font-family: var(--font-jp-serif); font-size: 13px; fill: var(--ink-dim); }
.pivot { font-family: var(--font-jp-serif); font-size: 12.5px; font-weight: 700; fill: var(--severe); }
.arrow { stroke: var(--severe); stroke-width: 3; }
.foot-div { stroke: var(--line-strong); stroke-width: 1; }
.foot-h { font-family: var(--font-mono); font-size: 12.5px; font-weight: 700; letter-spacing: 0.04em; fill: var(--accent); }
.foot { font-family: var(--font-jp-serif); font-size: 12px; fill: var(--ink-dim); }
</style>

<!--
Speaker Notes:
- 主役インサイト：敵対的な競争＋本物の検証信号（PnL・revert）があると、AI の自己改善は「新しい儲け方の発見」ではなく「損の減らし方・取引の選別」に向かう（閾値↑・サイズ↓・slippage↓・有害変更の rollback）
- 二面で語る：
  - 個体レベル＝AI が自分から取引を絞る self-throttle。これは「権限を渡しても暴走しない」安心材料
  - 系全体＝その守りが戦略間でそろうと、流動性が一斉に抜ける。相関 de-risk・crowding は未解決の systemic risk（AESS の本丸）
- データの裏：勝ち戦略 crossvenue / cvbal は一貫して 閾値↑・サイズ↓・slippage↓。変更量は勝敗を予測しない（gmxtrend は 43 変更で大敗）。効果は revert 減として観測
- 信頼づけ（footer）：これは El Farol / Minority Game（Arthur 1994 / Challet–Zhang 1997）の「競争＝変動が効率を決める」、Generation–Verification Gap（Song–Zhang–Kakade, ICLR'25, arXiv 2412.02674）の「検証が改善を駆動」の予測通り。Eris は検証コスト0・敵対競争・Self/Frozen 反実仮想統制で初の実機実証
  - 関連：LLM Cannot Self-Correct Yet（Huang+ ICLR'24, 2310.01798）／ TradingAgents（Xiao+ 2024, 2412.20138）
- 正直な穴（聞かれたら）：n 小・1 seed/1 regime、0.00 戦略の正体（crowding-out / no-fill）未確定、operator が LLM か heuristic か、regime 依存（trend 相場で勝者が反転するか）
- 結果図（Self-vs-Frozen 散布など）はこのスライドの前に差し込む
-->
