---
layout: default
---

<div class="nx-kicker">検証 ／ SPECA</div>
<h1 class="nx-display">仕様から脆弱性を見つける、<em>SPECA</em></h1>

<div class="sp-lead">検証の自律化はすでに動いている。SPECA は、Nyx が開発する<b>仕様駆動の AI 監査エージェント</b>。</div>

<div class="sp-flow"><div class="sp-card"><div class="sp-tag">STEP 01 ／ 仕様を読む</div><div class="sp-h">守るべき性質を導出</div><div class="sp-b">自然言語の仕様から、セキュリティプロパティを導き出す。</div></div><svg class="sp-arr" viewBox="0 0 26 14"><line x1="1" y1="7" x2="16" y2="7"/><path d="M16,2.5 L24,7 L16,11.5 Z"/></svg><div class="sp-card sp-card-hl"><div class="sp-tag sp-tag-hl">STEP 02 ／ 証明を試みる</div><div class="sp-h">実装との食い違いを特定</div><div class="sp-b">性質が成立するか実装ごとに証明を試み、破れる箇所＝脆弱性を突き止める。</div></div><svg class="sp-arr" viewBox="0 0 26 14"><line x1="1" y1="7" x2="16" y2="7"/><path d="M16,2.5 L24,7 L16,11.5 Z"/></svg><div class="sp-card"><div class="sp-tag">STEP 03 ／ 報告</div><div class="sp-h">監査レポートを提出</div><div class="sp-b">検出した脆弱性を根拠つきで報告し、人手の監査を補完する。</div></div></div>

<div class="sp-facts"><div class="sp-f"><span class="sp-fl">Sherlock 監査コンテスト</span><span class="sp-fv">既知の H/M/L <b>15件</b> を全検出</span></div><div class="sp-f"><span class="sp-fl">新規発見</span><span class="sp-fv">366人が見逃した <b>4件</b>（開発者確認済み）</span></div><div class="sp-f"><span class="sp-fl">C/C++ 15プロジェクト</span><span class="sp-fv">精度 <b>88.9%</b></span></div></div>

<style>
.sp-lead { font-family: var(--font-jp-serif); font-size: 15px; line-height: 1.7; color: var(--ink-dim); background: var(--bg-2); border-left: 2px solid var(--accent); padding: 0.45rem 0.95rem; display: inline-block; }
.sp-lead b { font-weight: 600; color: var(--ink); }
.sp-flow { display: flex; align-items: stretch; justify-content: center; gap: 0.7rem; max-width: 910px; margin: 1.5rem auto 0; }
.sp-card { flex: 1; background: #fff; border: 1px solid var(--line); border-radius: 10px; padding: 0.9rem 1.05rem 1rem; }
.sp-card-hl { background: var(--bg-2); border: 2px solid var(--accent); }
.sp-tag { font-family: var(--font-mono); font-size: 12px; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-faint); }
.sp-tag-hl { color: var(--accent); }
.sp-h { font-family: var(--font-jp-serif); font-size: 16.5px; font-weight: 700; color: var(--ink); margin-top: 0.42rem; }
.sp-b { font-family: var(--font-jp-serif); font-size: 13px; line-height: 1.68; color: var(--ink-dim); margin-top: 0.4rem; }
.sp-arr { width: 26px; flex-shrink: 0; align-self: center; }
.sp-arr line { stroke: var(--ink-faint); stroke-width: 1.6; }
.sp-arr path { fill: var(--ink-faint); }
.sp-facts { display: flex; justify-content: center; gap: 0; margin: 1.5rem auto 0; }
.sp-f { display: flex; flex-direction: column; gap: 0.22rem; padding: 0.15rem 1.6rem; border-left: 1px solid var(--line-strong); flex: 0 0 auto; }
.sp-f:first-child { border-left: none; }
.sp-fl { font-family: var(--font-mono); font-size: 11.5px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: var(--ink-faint); }
.sp-fv { font-family: var(--font-jp-serif); font-size: 14px; color: var(--ink-dim); }
.sp-fv b { font-family: var(--font-mono); font-size: 15px; font-weight: 700; color: var(--accent); }
</style>

<SourceCite :sources="[
  { label: 'NyxFoundation/speca — Specification-to-Checklist Agentic Auditing Framework（実績数値の出典）', url: 'https://github.com/NyxFoundation/speca' },
  { label: 'SPECA Documentation', url: 'https://speca.pages.dev/' }
]" />

<!--
Speaker Notes:
- 前ページ「事後 ／ 自律」の具体化。検証の自律化を担うのが SPECA（Nyx のフラッグシップ研究）
- SPECA = Specification-to-Checklist Agentic Auditing Framework。既知バグパターンの検索ではなく、仕様から導いたプロパティを実装ごとに「証明できるか」試す proof-attempt 型の監査
- Sherlock（Fusaka Audit Contest）：既知の H/M/L 15件を全検出、さらに 366人の監査者が見逃した 4件を新規発見（開発者コミットで確認済み）
- RepoAudit ベンチマーク（C/C++ 15プロジェクト・35脆弱性）：精度 88.9%（Sonnet 4.5）。既知以外に12候補、うち2件は上流メンテナー確認済み
- 誤検知も 3 つの解釈可能な原因に帰着＝ブラックボックスでない検証
- エージェント経済の文脈：取引相手のコントラクトや自分のコードを、人手を待たずにエージェントが検証できるようになる
-->
