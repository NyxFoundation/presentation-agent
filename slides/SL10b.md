---
layout: default
---

<div class="nx-kicker">実験 ／ Eris</div>
<h1 class="nx-display">自作シミュレータは、<em>意図・実行・検証</em>を回す。</h1>

<div class="lp"><svg class="lp-svg" viewBox="0 0 980 360" preserveAspectRatio="xMidYMid meet"><path d="M390,175 A100,100 0 0 1 590,175" class="lp-arc lp-arc-h"/><path d="M590,175 A100,100 0 0 1 390,175" class="lp-arc"/><path d="M0,-5 L8,0 L0,5 Z" class="lp-tri" transform="translate(419.3 245.7) rotate(45)"/><path d="M0,-5 L8,0 L0,5 Z" class="lp-tri" transform="translate(560.7 245.7) rotate(-45)"/><path d="M0,-5 L8,0 L0,5 Z" class="lp-tri lp-tri-h" transform="translate(490 75) rotate(180)"/><line x1="348" y1="175" x2="306" y2="175" class="lp-conn"/><line x1="632" y1="175" x2="674" y2="175" class="lp-conn"/><text x="300" y="116" class="lp-grp lp-grp-h" text-anchor="end">意図 ／ 戦略の調整</text><text x="300" y="143" class="lp-item" text-anchor="end">戦略別に version を更新</text><text x="300" y="167" class="lp-item" text-anchor="end">threshold を上げる</text><text x="300" y="191" class="lp-item" text-anchor="end">size・slippage を締める</text><text x="300" y="215" class="lp-item" text-anchor="end">多 revert は rollback</text><text x="680" y="116" class="lp-grp lp-grp-h" text-anchor="start">検証 ／ onchain state</text><text x="680" y="143" class="lp-item" text-anchor="start">約定 ／ revert 数</text><text x="680" y="167" class="lp-item" text-anchor="start">PnL（self ↔ frozen）</text><text x="680" y="191" class="lp-item" text-anchor="start">ポジション・残高</text><text x="680" y="215" class="lp-item" text-anchor="start">fair price からの乖離</text><circle cx="390" cy="175" r="42" class="lp-human"/><text x="390" y="171" class="lp-h" text-anchor="middle">意図</text><text x="390" y="190" class="lp-tag lp-tag-h" text-anchor="middle">LLM</text><circle cx="590" cy="175" r="42" class="lp-human"/><text x="590" y="171" class="lp-h" text-anchor="middle">検証</text><text x="590" y="190" class="lp-tag lp-tag-h" text-anchor="middle">onchain</text><circle cx="490" cy="275" r="42" class="lp-ai"/><text x="490" y="271" class="lp-h lp-h-ai" text-anchor="middle">実行</text><text x="490" y="290" class="lp-tag lp-tag-a" text-anchor="middle">tx</text><text x="490" y="338" class="lp-aisub" text-anchor="middle">署名して onchain 提出</text></svg></div>

<style>
.lp { display: flex; justify-content: center; margin-top: 0.5rem; }
.lp-svg { width: 100%; max-width: 860px; height: auto; }
.lp-arc { fill: none; stroke: var(--ink-faint); stroke-width: 2; }
.lp-arc-h { stroke: var(--accent); stroke-width: 3; }
.lp-tri { fill: var(--ink-faint); }
.lp-tri-h { fill: var(--accent); }
.lp-conn { stroke: var(--line-strong); stroke-width: 1; }
.lp-human { fill: #e7ecf1; stroke: var(--accent); stroke-width: 2.4; }
.lp-ai { fill: #fff; stroke: var(--line-strong); stroke-width: 1.6; }
.lp-h { font-family: var(--font-jp-serif); font-size: 21px; font-weight: 700; fill: var(--accent); }
.lp-h-ai { fill: var(--ink-dim); }
.lp-tag { font-family: var(--font-mono); font-size: 11px; font-weight: 600; letter-spacing: 0.06em; }
.lp-tag-h { fill: var(--accent); }
.lp-tag-a { fill: var(--ink-faint); }
.lp-aisub { font-family: var(--font-jp-serif); font-size: 12px; fill: var(--ink-dim); }
.lp-grp { font-family: var(--font-mono); font-size: 12.5px; font-weight: 700; letter-spacing: 0.06em; }
.lp-grp-h { fill: var(--accent); }
.lp-item { font-family: var(--font-jp-serif); font-size: 14.5px; font-weight: 500; fill: var(--ink); }
</style>

<SourceCite :sources="[
  { label: 'Eris Competition examples/agents（各戦略と調整パラメータ）', url: 'https://github.com/NyxFoundation/eris-competition-poc/tree/main/examples/agents' }
]" />

<!--
Speaker Notes:
- p9 の「意図 → 実行 → 検証」ループを、そのまま実験設定に当てはめた図
- 意図（LLM）：各戦略ごとに次の tx を設計。version を更新し、threshold を上げ、size・slippage を締め、revert が増えたら rollback
- 実行（tx）：署名して onchain に提出。毎 block 実行される
- 検証（onchain state）：約定/revert 数・PnL（self vs frozen）・ポジション・fair price 乖離をフィードバックとして読む
- 上の青い弧 = 検証 → 意図 のフィードバック（onchain state が次の意図に効く）
- これを 17 戦略・block 1851–2176 で回したのが次ページからの結果
-->
