---
layout: default
---

<div class="nx-kicker">権限管理 ／ Agent Wallet</div>
<h1 class="nx-display">鍵ではなく権限を渡す、<em>Agent Wallet</em></h1>

<div class="aw-lead">人間が決めた委任の範囲をウォレット層でコードとして強制する。AI は権限の内側でしか動けない。</div>

<div class="aw"><svg class="aw-svg" viewBox="0 0 980 330" preserveAspectRatio="xMidYMid meet"><defs><marker id="awa" markerWidth="9" markerHeight="9" refX="6.5" refY="3.4" orient="auto"><path d="M0,0 L7,3.4 L0,6.8 Z" class="aw-tri"/></marker><marker id="awg" markerWidth="9" markerHeight="9" refX="6.5" refY="3.4" orient="auto"><path d="M0,0 L7,3.4 L0,6.8 Z" class="aw-tri-g"/></marker><marker id="aws" markerWidth="9" markerHeight="9" refX="6.5" refY="3.4" orient="auto"><path d="M0,0 L7,3.4 L0,6.8 Z" class="aw-tri-s"/></marker></defs><circle cx="470" cy="46" r="27" class="aw-hum"/><text x="470" y="52" class="aw-hum-t" text-anchor="middle">人間</text><line x1="470" y1="76" x2="470" y2="108" class="aw-ed" marker-end="url(#awa)"/><text x="486" y="97" class="aw-ed-lbl" text-anchor="start">委任の範囲を設定</text><circle cx="128" cy="205" r="44" class="aw-ai"/><text x="128" y="201" class="aw-ai-t" text-anchor="middle">AI</text><text x="128" y="222" class="aw-ai-tag" text-anchor="middle">agent</text><text x="128" y="277" class="aw-desc" text-anchor="middle">取引を試みる</text><line x1="180" y1="205" x2="292" y2="205" class="aw-ed" marker-end="url(#awa)"/><text x="236" y="192" class="aw-ed-lbl" text-anchor="middle">tx</text><rect x="302" y="118" width="336" height="174" rx="12" class="aw-box"/><text x="470" y="150" class="aw-box-name" text-anchor="middle">Agent Wallet</text><line x1="330" y1="166" x2="610" y2="166" class="aw-box-line"/><text x="330" y="196" class="aw-pol" text-anchor="start">支出の上限</text><text x="330" y="226" class="aw-pol" text-anchor="start">許可先のリスト</text><text x="330" y="256" class="aw-pol" text-anchor="start">委任の期限・失効</text><text x="610" y="196" class="aw-pol-m" text-anchor="end">max_spend</text><text x="610" y="226" class="aw-pol-m" text-anchor="end">allowlist</text><text x="610" y="256" class="aw-pol-m" text-anchor="end">expiry</text><line x1="638" y1="172" x2="742" y2="146" class="aw-ed-g" marker-end="url(#awg)"/><text x="688" y="140" class="aw-lbl-g" text-anchor="middle">✓ 権限内の取引</text><line x1="638" y1="240" x2="742" y2="266" class="aw-ed-s" marker-end="url(#aws)"/><text x="688" y="288" class="aw-lbl-s" text-anchor="middle">✗ 権限外の取引</text><rect x="752" y="112" width="186" height="58" rx="9" class="aw-out-g"/><text x="845" y="138" class="aw-out-gt" text-anchor="middle">実行</text><text x="845" y="158" class="aw-out-gs" text-anchor="middle">オンチェーンへ</text><rect x="752" y="242" width="186" height="58" rx="9" class="aw-out-s"/><text x="845" y="268" class="aw-out-st" text-anchor="middle">拒否</text><text x="845" y="288" class="aw-out-ss" text-anchor="middle">実行されない</text></svg></div>

<style>
.aw-lead { font-family: var(--font-jp-serif); font-size: 15px; line-height: 1.7; color: var(--ink-dim); background: var(--bg-2); border-left: 2px solid var(--accent); padding: 0.45rem 0.95rem; display: inline-block; }
.aw { display: flex; justify-content: center; margin-top: 0.7rem; }
.aw-svg { width: 100%; max-width: 880px; height: auto; }
.aw-tri { fill: var(--ink-faint); }
.aw-tri-g { fill: var(--accent); }
.aw-tri-s { fill: var(--severe); }
.aw-ed { stroke: var(--ink-faint); stroke-width: 1.8; }
.aw-ed-g { stroke: var(--accent); stroke-width: 1.8; }
.aw-ed-s { stroke: var(--severe); stroke-width: 1.8; }
.aw-ed-lbl { font-family: var(--font-jp-serif); font-size: 13px; font-weight: 600; fill: var(--ink-dim); }
.aw-hum { fill: #fff; stroke: var(--accent); stroke-width: 1.6; }
.aw-hum-t { font-family: var(--font-jp-serif); font-size: 15px; font-weight: 700; fill: var(--ink); }
.aw-ai { fill: #fff; stroke: var(--line-strong); stroke-width: 1.6; }
.aw-ai-t { font-family: var(--font-jp-serif); font-size: 20px; font-weight: 700; fill: var(--ink-dim); }
.aw-ai-tag { font-family: var(--font-mono); font-size: 11.5px; font-weight: 600; letter-spacing: 0.06em; fill: var(--ink-faint); }
.aw-desc { font-family: var(--font-jp-serif); font-size: 13.5px; font-weight: 500; fill: var(--ink-dim); }
.aw-box { fill: #e7ecf1; stroke: var(--accent); stroke-width: 2.6; }
.aw-box-name { font-family: var(--font-serif); font-style: italic; font-size: 23px; fill: var(--accent); }
.aw-box-line { stroke: var(--accent-line); stroke-width: 1; }
.aw-pol { font-family: var(--font-jp-serif); font-size: 14.5px; font-weight: 600; fill: var(--ink); }
.aw-pol-m { font-family: var(--font-mono); font-size: 12px; fill: var(--accent); letter-spacing: 0.02em; }
.aw-lbl-g { font-family: var(--font-jp-serif); font-size: 13px; font-weight: 700; fill: var(--accent); }
.aw-lbl-s { font-family: var(--font-jp-serif); font-size: 13px; font-weight: 700; fill: var(--severe); }
.aw-out-g { fill: #fff; stroke: var(--accent); stroke-width: 1.6; }
.aw-out-gt { font-family: var(--font-jp-serif); font-size: 16px; font-weight: 700; fill: var(--accent); }
.aw-out-gs { font-family: var(--font-jp-serif); font-size: 12.5px; fill: var(--ink-dim); }
.aw-out-s { fill: #fff7f6; stroke: var(--severe); stroke-width: 1.4; stroke-dasharray: 5 4; }
.aw-out-st { font-family: var(--font-jp-serif); font-size: 16px; font-weight: 700; fill: var(--severe); }
.aw-out-ss { font-family: var(--font-jp-serif); font-size: 12.5px; fill: var(--ink-dim); }
</style>

<SourceCite :sources="[
  { label: 'ERC-4337 — スマートアカウントとセッションキーによる権限制御', url: 'https://eips.ethereum.org/EIPS/eip-4337' },
  { label: 'Coinbase AgentKit — AIエージェント向けウォレットの権限設計', url: 'https://docs.cdp.coinbase.com/agent-kit/welcome' }
]" />

<!--
Speaker Notes:
- 前ページ「事前 ／ 自律」の具体化。権限管理の自律化を担うのが Agent Wallet
- 発想の転換：AI に秘密鍵そのものを渡さない。渡すのは「権限」だけ
- 人間は委任の範囲（支出の上限・許可先のリスト・期限と失効）をポリシーとして設定する
- ポリシーはウォレット層（スマートアカウント／セッションキー）でコードとして強制される。運用でなく機構で守る
- 権限内の取引はそのままオンチェーンへ、権限外の取引は署名されず実行されない
- AI がどれだけ賢く（あるいは暴走）しても、越えられない上限が機械的に決まっている ── これが「事前の自律化」
-->
