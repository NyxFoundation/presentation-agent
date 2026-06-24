---
layout: default
---

<div class="nx-kicker">Next Step ／ Eris</div>
<h1 class="nx-display">次に問うべき、<em>4つの論点</em>。</h1>
<div class="ns-grid"><div class="ns-card"><div class="ns-num">01</div><div class="ns-body"><div class="ns-q">botと何が違うか？</div><div class="ns-e">平常時は、考える分だけ遅い。だが急変の瞬間、固まった bot を尻目に、AIだけが乗り換える——はず。</div></div></div><div class="ns-card"><div class="ns-num">02</div><div class="ns-body"><div class="ns-q">戦略の多様化はどう起きるか？</div><div class="ns-e">広く探すほどトークンを食う。勝者を分けるのは資本でなく〈情報の効率〉——強いAIを作る条件が、そのまま市場の勝ち筋になる。</div></div></div><div class="ns-card"><div class="ns-num">03</div><div class="ns-body"><div class="ns-q">守りのAIに、どんな認証・権限を渡すか？</div><div class="ns-e">自分から守るAIなら、どこまで任せていい？ 権限の線引きを、勘でなく実データで決められる。</div></div></div><div class="ns-card"><div class="ns-num">04</div><div class="ns-body"><div class="ns-q">役割の多様化は、何をもたらすか？</div><div class="ns-e">ハッカーや、一撃で抜けるAI——正攻法でない1体が混じったら、皆の〈自制〉は保たれるのか、崩れるのか。</div></div></div></div>

<style>
.ns-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem 1.3rem; max-width: 884px; margin: 1.15rem auto 0; }
.ns-card { display: flex; gap: 0.8rem; background: #fff; border: 1px solid var(--line); border-left: 3px solid var(--accent); border-radius: 10px; padding: 0.85rem 1.1rem 0.95rem; }
.ns-num { font-family: var(--font-mono); font-size: 21px; font-weight: 700; color: var(--accent); line-height: 1.1; flex-shrink: 0; }
.ns-body { flex: 1; }
.ns-q { font-family: var(--font-jp-serif); font-size: 16px; font-weight: 800; color: var(--ink); margin-bottom: 0.3rem; }
.ns-e { font-family: var(--font-jp-serif); font-size: 13px; line-height: 1.62; color: var(--ink-dim); }
</style>

<!--
Speaker Notes:
- Eris セクションの締め＝Next Step。p15（現実×敵対競争で理論を再現）を土台に、ここから問う4つ
- 論点①（botと何が違うか）：tx 頻度は bot 並み/低頻度だが、各イベントで学び戦略を自己改善＝bot にない適応力。想定外（regime 変化・新手）に強いはず。bot は「安定して速い」場、エージェントは「世界が変わる」場で勝つ
- 論点②（戦略の多様化）：幅広く戦略を探すメタ能力はトークンを食う → 勝ち筋のミラトレで効率化／特化 ⇒ 結局多様化。突き詰めるとデータ取得とコンテキスト管理の効率＝実際のAIエージェント開発のボトルネックと地続き
- 論点③（守りのAIへの認証・権限）：自制する（守りに入る）AIに、身元確認（KYA, ERC-8004）・権限管理・委任範囲をどう設計するか＝意図側（事前設計）の問い。デッキの 意図/検証 ループに接続
- 論点④（役割の多様化）：ハッカーAI、別手段で利益最大化するAI、一時的にプライスインパクトの大きい α を一回だけ狙うAI 等、役割が増えると系全体（脆弱性・流動性）はどう変わるか
- いずれも Eris（本物の検証環境）で測りにいける、で締める
-->
