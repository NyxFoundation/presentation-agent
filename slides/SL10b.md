---
layout: default
---

<div class="nx-kicker">実験 ／ Eris</div>

<div class="dg"><svg class="dg-svg" viewBox="0 0 980 340" preserveAspectRatio="xMidYMid meet"><defs><marker id="dga" markerWidth="9" markerHeight="9" refX="6.5" refY="3.4" orient="auto"><path d="M0,0 L7,3.4 L0,6.8 Z" class="dg-tri"/></marker><marker id="dgh" markerWidth="9" markerHeight="9" refX="6.5" refY="3.4" orient="auto"><path d="M0,0 L7,3.4 L0,6.8 Z" class="dg-tri-h"/></marker><marker id="dgf" markerWidth="9" markerHeight="9" refX="6.5" refY="3.4" orient="auto"><path d="M0,0 L7,3.4 L0,6.8 Z" class="dg-tri-f"/></marker></defs><rect x="110" y="30" width="350" height="196" rx="12" class="dg-box dg-box-a"/><text x="132" y="62" class="dg-tag dg-tag-a">A ／ 自己改善あり</text><rect x="520" y="30" width="350" height="196" rx="12" class="dg-box dg-box-b"/><text x="542" y="62" class="dg-tag">B ／ 固定</text><line x1="236" y1="160" x2="330" y2="160" class="dg-ed-h" marker-end="url(#dgh)"/><line x1="345" y1="136" x2="311" y2="112" class="dg-ed-h" marker-end="url(#dgh)"/><line x1="259" y1="112" x2="225" y2="136" class="dg-ed-h" marker-end="url(#dgh)"/><circle cx="205" cy="160" r="27" class="dg-n dg-n-a"/><text x="205" y="166" class="dg-nt dg-nt-a" text-anchor="middle">実行</text><circle cx="365" cy="160" r="27" class="dg-n dg-n-a"/><text x="365" y="166" class="dg-nt dg-nt-a" text-anchor="middle">検証</text><circle cx="285" cy="98" r="27" class="dg-n dg-n-a"/><text x="285" y="104" class="dg-nt dg-nt-a" text-anchor="middle">調整</text><text x="285" y="212" class="dg-cap" text-anchor="middle">結果を見て、設定を直し続ける</text><line x1="646" y1="160" x2="740" y2="160" class="dg-ed-f" marker-end="url(#dgf)"/><line x1="755" y1="136" x2="721" y2="112" class="dg-ed-f" marker-end="url(#dgf)"/><line x1="669" y1="112" x2="635" y2="136" class="dg-ed-f" marker-end="url(#dgf)"/><circle cx="615" cy="160" r="27" class="dg-n dg-n-b"/><text x="615" y="166" class="dg-nt" text-anchor="middle">実行</text><circle cx="775" cy="160" r="27" class="dg-n dg-n-g"/><text x="775" y="166" class="dg-nt dg-nt-g" text-anchor="middle">検証</text><circle cx="695" cy="98" r="27" class="dg-n dg-n-g"/><text x="695" y="104" class="dg-nt dg-nt-g" text-anchor="middle">調整</text><text x="695" y="212" class="dg-cap" text-anchor="middle">最初の設定のまま、走り続ける</text><line x1="285" y1="230" x2="285" y2="262" class="dg-ed" marker-end="url(#dga)"/><line x1="695" y1="230" x2="695" y2="262" class="dg-ed" marker-end="url(#dga)"/><rect x="110" y="268" width="760" height="54" rx="9" class="dg-mkt"/><text x="490" y="301" class="dg-mkt-t" text-anchor="middle">同じ戦略の対を、同一市場で並走させる（同じ価格・同じイベント・同じ元手）</text></svg></div>

<style>
.dg { display: flex; justify-content: center; margin-top: 3.4rem; }
.dg-svg { width: 100%; max-width: 880px; height: auto; }
.dg-tri { fill: var(--ink-faint); }
.dg-tri-h { fill: var(--accent); }
.dg-tri-f { fill: rgba(154, 149, 140, 0.45); }
.dg-ed { stroke: var(--ink-faint); stroke-width: 1.8; }
.dg-ed-h { stroke: var(--accent); stroke-width: 1.8; }
.dg-ed-f { stroke: rgba(154, 149, 140, 0.45); stroke-width: 1.6; stroke-dasharray: 4 4; }
.dg-box { fill: #fff; }
.dg-box-a { stroke: var(--accent); stroke-width: 2.4; }
.dg-box-b { stroke: var(--line-strong); stroke-width: 1.4; }
.dg-tag { font-family: var(--font-mono); font-size: 13px; font-weight: 700; letter-spacing: 0.1em; fill: var(--ink-dim); }
.dg-tag-a { fill: var(--accent); }
.dg-n-a { fill: #e7ecf1; stroke: var(--accent); stroke-width: 1.8; }
.dg-n-b { fill: #fff; stroke: var(--line-strong); stroke-width: 1.6; }
.dg-n-g { fill: #fff; stroke: var(--ink-faint); stroke-width: 1.2; stroke-dasharray: 4 4; opacity: 0.55; }
.dg-nt { font-family: var(--font-jp-serif); font-size: 15px; font-weight: 700; fill: var(--ink-dim); }
.dg-nt-a { fill: var(--accent); }
.dg-nt-g { fill: var(--ink-faint); }
.dg-cap { font-family: var(--font-jp-serif); font-size: 13.5px; font-weight: 600; fill: var(--ink-dim); }
.dg-mkt { fill: var(--bg-2); stroke: var(--line-strong); stroke-width: 1.2; }
.dg-mkt-t { font-family: var(--font-jp-serif); font-size: 15px; font-weight: 600; fill: var(--ink); }
</style>

<!--
Speaker Notes:
- 実験設計＝matched pair（反実仮想統制）。同じ戦略を 2 体ずつ用意する
  - A（自己改善あり / Dynamic）：実行 → onchain の結果を検証 → パラメータを調整、のループを回し続ける
  - B（固定 / Fixed）：同じ戦略・同じ初期設定のまま、一切直さずに走り続ける
- 調整対象のパラメータ：entry 閾値（spread/gap/z）・size・leverage・slippage・fee 上限・LP レンジ・リスク guard（LTV/stop/hedge/high-revert/rollback）
- 検証で読む onchain state：約定/revert 数・PnL・ポジション・残高・fair price からの乖離
- 2 体は同一市場で並走：同じ価格系列・同じイベント・同じ元手（例：equity $49.1K スタート）
- だから Δ ＝ A − B を取れば、市場の運・イベントの偶然は相殺され、自己改善の寄与だけが残る
- これを 17 戦略・block 1851–2176 で回した結果が次ページ
-->
