---
layout: default
---

<div class="nx-kicker">考察 ／ Eris</div>
<h1 class="nx-display">AIエージェントは、<em>botと何が違うか</em>。</h1>
<div class="dc-wrap"><div class="dc-card"><div class="dc-num">論点 ①</div><div class="dc-head">速さでなく、適応</div><div class="dc-line">tx の速さは bot 並み（考える分むしろ低頻度）</div><div class="dc-line">でも、起きた事ごとに学んで戦略を直す</div><div class="dc-line">→ 想定外の急変・新手に強いはず</div><div class="dc-punch">bot は“速さ”、AIは“適応”で勝つ</div></div><div class="dc-card"><div class="dc-num">論点 ②</div><div class="dc-head">多様性とコストの経済学</div><div class="dc-line">幅広く戦略を探せるが、トークンを多く食う</div><div class="dc-line">→ 勝ち筋を真似て効率化／特化 ⇒ 結局多様化</div><div class="dc-line">鍵は「データ取得とコンテキスト管理の効率」</div><div class="dc-punch">＝ AIエージェント開発の課題と地続き</div></div></div>
<div class="dc-foot"><b>どちらも仮説。</b> この現実の環境（Eris）でこそ、<em>確かめにいける</em>。</div>

<style>
.dc-wrap { display: flex; gap: 1.5rem; justify-content: center; max-width: 900px; margin: 1.1rem auto 0; }
.dc-card { flex: 1; background: #fff; border: 1px solid var(--line); border-left: 3px solid var(--accent); border-radius: 10px; padding: 0.9rem 1.2rem 1rem; }
.dc-num { font-family: var(--font-mono); font-size: 11px; font-weight: 700; letter-spacing: 0.08em; color: var(--accent); }
.dc-head { font-family: var(--font-jp-serif); font-size: 19px; font-weight: 800; color: var(--ink); margin: 0.12rem 0 0.6rem; }
.dc-line { font-family: var(--font-jp-serif); font-size: 14px; line-height: 1.72; color: var(--ink-dim); }
.dc-punch { font-family: var(--font-jp-serif); font-size: 14.5px; font-weight: 700; color: var(--accent); border-top: 1px solid var(--line); margin-top: 0.6rem; padding-top: 0.55rem; }
.dc-foot { display: block; max-width: 900px; margin: 1rem auto 0; padding: 0.55rem 0.95rem; background: var(--bg-2); border-left: 2px solid var(--accent); font-family: var(--font-jp-serif); font-size: 15px; color: var(--ink-dim); text-align: center; }
.dc-foot b { color: var(--ink); font-weight: 700; }
.dc-foot em { color: var(--accent); font-style: normal; font-weight: 700; }
</style>

<!--
Speaker Notes:
- p15 までの「測ったこと」から一段、ここは「考察・仮説」。AIエージェントだから生まれる論点を2つ
- 論点①（速さでなく適応／vs bot）:
  - tx 頻度は bot と同等か、reasoning latency でむしろ低頻度になりうる
  - だが各イベントで学習して戦略を自己改善する＝bot にない性質
  - よって想定外の事象（相場の急変・新種の攻撃・regime 変化）への対応力が高いはず
  - トレードオフとして言う：bot は「安定して速い」場で勝ち、エージェントは「世界が変わる」場で勝つ。Eris に regime ショックや新イベントを入れて LLMエージェント vs ルールbot を比較すれば検証できる
- 論点②（多様性とトークン経済）:
  - 幅広く戦略を探すメタ能力が高いが、普通にやるとトークン消費が大きい
  - → 勝ち筋をミラトレして効率化、あるいは特化 ⇒ 結局は戦略が多様化する、という仮説
  - 突き詰めると勝負はデータ取得の効率化とコンテキスト管理 ＝ 計算/情報の効率が競争上の一次資源になる
  - それは実際の AIエージェント開発のボトルネックそのもの。Eris は「エージェント開発の課題が、競争適応度として可視化される実験場」
- どちらも未測定の仮説。p15 の「現実の検証環境」で実際に測れる、という前向きな締め
-->
