---
layout: default
---

<div class="nx-kicker">05 ／ Eris</div>
<h1 class="nx-display">AIエージェント専用の<em>模擬経済環境</em></h1>

<div class="ov-lead">Eris は、自律エージェントが取引し続ける専用チェーン上で、DeFi プロトコルを<b>継続的にストレステスト</b>する基盤。</div>

<div class="ov-flow"><div class="ov-card"><div class="ov-tag">STAGE 01 ／ 投入</div><div class="ov-h">コントラクトとエージェント</div><div class="ov-b">DeFi 事業者は検証したいコントラクトを、開発者は自作のエージェントをデプロイする。</div></div><svg class="ov-arr" viewBox="0 0 26 14"><line x1="1" y1="7" x2="16" y2="7"/><path d="M16,2.5 L24,7 L16,11.5 Z"/></svg><div class="ov-card ov-card-hl"><div class="ov-tag ov-tag-hl">STAGE 02 ／ 敵対的な取引</div><div class="ov-h">エージェントの群れが競う</div><div class="ov-b">裁定・清算・スナイピングなどで利益を競うなか、急落・depeg・大口注文をシナリオとして注入する。</div></div><svg class="ov-arr" viewBox="0 0 26 14"><line x1="1" y1="7" x2="16" y2="7"/><path d="M16,2.5 L24,7 L16,11.5 Z"/></svg><div class="ov-card"><div class="ov-tag">STAGE 03 ／ 検出</div><div class="ov-h">失敗モードのレポート</div><div class="ov-b">AMM の脆弱性・清算経路・オラクル遅延など、静的監査に現れない弱点を報告する。</div></div></div>

<div class="ov-doms"><span class="ov-doms-l">対象領域</span><span class="ov-chip">AMM</span><span class="ov-chip">Lending</span><span class="ov-chip">Flashloan</span><span class="ov-chip">Oracle</span><span class="ov-chip">Stablecoin</span><span class="ov-chip">Token Launch</span><span class="ov-chip">Perpetuals</span></div>

<div class="absolute bottom-3 left-6 text-[10px] text-gray-400 leading-tight max-w-3xl">
Sources: Nyx Foundation "Eris — The Agentic Financial Simulation Layer" erisnet.xyz 2026
</div>

<style>
.ov-lead { font-family: var(--font-jp-serif); font-size: 15px; line-height: 1.7; color: var(--ink-dim); background: var(--bg-2); border-left: 2px solid var(--accent); padding: 0.45rem 0.95rem; display: inline-block; }
.ov-lead b { font-weight: 600; color: var(--ink); }
.ov-flow { display: flex; align-items: stretch; justify-content: center; gap: 0.7rem; max-width: 910px; margin: 2rem auto 0; }
.ov-card { flex: 1; background: #fff; border: 1px solid var(--line); border-radius: 10px; padding: 0.9rem 1.05rem 1rem; }
.ov-card-hl { background: var(--bg-2); border: 2px solid var(--accent); }
.ov-tag { font-family: var(--font-mono); font-size: 12px; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-faint); }
.ov-tag-hl { color: var(--accent); }
.ov-h { font-family: var(--font-jp-serif); font-size: 16.5px; font-weight: 700; color: var(--ink); margin-top: 0.42rem; }
.ov-b { font-family: var(--font-jp-serif); font-size: 13px; line-height: 1.68; color: var(--ink-dim); margin-top: 0.4rem; }
.ov-arr { width: 26px; flex-shrink: 0; align-self: center; }
.ov-arr line { stroke: var(--ink-faint); stroke-width: 1.6; }
.ov-arr path { fill: var(--ink-faint); }
.ov-doms { display: flex; align-items: center; justify-content: center; gap: 0.5rem; flex-wrap: wrap; max-width: 910px; margin: 1.7rem auto 0; }
.ov-doms-l { font-family: var(--font-mono); font-size: 12px; font-weight: 500; letter-spacing: 0.14em; color: var(--ink-dim); margin-right: 0.4rem; }
.ov-chip { font-family: var(--font-mono); font-size: 12px; color: var(--ink-dim); background: var(--bg-2); border: 1px solid var(--line); border-radius: 999px; padding: 0.18rem 0.7rem; }
</style>

<!--
Speaker Notes:
- Eris = The Agentic Financial Simulation Layer（erisnet.xyz）。AI エージェント専用の L2 で、DeFi マーケットの模擬経済環境
- 思想: "Real failure modes live in adversarial flow" ── 本当の失敗モードは敵対的な取引フローの中にしか現れない。静的監査の補完
- 使い方は 2 面: DeFi 事業者はコントラクトをデプロイして AI テストレポートを受け取る / エージェント開発者はエージェントを投入して設計されたシナリオで取引する
- シナリオ注入: CEX drift・informed flow・whale order・lending incident・stablecoin depeg・crash event を調整可能なスケジュールで流す
- 対象領域: AMM（atomic arb・JIT・CEX-DEX arb・range LP）/ Lending（清算競争・レート裁定）/ Flashloan / Oracle（遅延悪用・価格乖離）/ Stablecoin（depeg 裁定）/ Token launch（sniping・価格発見）/ Perpetuals（funding arb・basis trade）
- 運営: Nyx Foundation。ステータスは Coming soon
- 次ページ: この環境の中身（プロトコルと戦略の全体像）へ
-->
