---
layout: default
---

<div class="nx-kicker">Next Step ／ Eris</div>
<h1 class="nx-display">次に問うべき、<em>4つの論点</em>。</h1>
<div class="ns-grid"><div class="ns-card"><div class="ns-num">01</div><div class="ns-body"><div class="ns-q">botと何が違うか？</div><div class="ns-e">botは決まったルールで瞬時に動くが、AIは考える分だけ遅く、取引回数も少ない。平常時はこれが不利になる。だが暴落や新手の攻撃といった未知が来ると、botは古いルールを当て続けて崩れ、AIはその場で戦略を組み替える。差は速さでなく、未知への対応力ではないか。</div></div></div><div class="ns-card"><div class="ns-num">02</div><div class="ns-body"><div class="ns-q">戦略の多様化はどう起きるか？</div><div class="ns-e">AIは幅広く戦略を探せるが、探索にはトークン（計算コスト）がかかり、全部は試せない。だから勝ち筋を真似る者と、一点に特化する者に分かれ、戦略は多様化していく。勝敗を分けるのは資本量より、データとコンテキストを効率よく扱う力。良いAIを作る課題が、そのまま市場の勝ち筋になる。</div></div></div><div class="ns-card"><div class="ns-num">03</div><div class="ns-body"><div class="ns-q">守りのAIに、どんな認証・権限を渡すか？</div><div class="ns-e">実験では、競争するAIは自分から守りに入った。守りが安全の源なら、認可は「許す/禁止」を静的に固めるより振る舞いに連動させたい。リスクを抑えている間だけ権限や資本を広げ、失敗tx（revert）が増えたら自動で絞り剥奪する。前提は“守っている事実”をその場で検証できること。身元（KYA）に加え、自制し続けた実績そのものを信頼の根拠にできるか。</div></div></div><div class="ns-card"><div class="ns-num">04</div><div class="ns-body"><div class="ns-q">役割の多様化は、何をもたらすか？</div><div class="ns-e">ここまでは皆が正攻法で稼いでいた。だが役割は増やせる。契約の穴を突くハッカーAI、別の手段で稼ぐAI、価格を大きく動かすαを一度だけ抜けて去るAI。そんな1体が混じったとき、皆の自制は保たれるのか、一気に崩れるのか。個の安全が系全体の安全になるかを測れる。</div></div></div></div>

<style>
.ns-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.85rem 1.25rem; max-width: 896px; margin: 0.85rem auto 0; }
.ns-card { display: flex; gap: 0.8rem; background: #fff; border: 1px solid var(--line); border-left: 3px solid var(--accent); border-radius: 10px; padding: 0.8rem 1.05rem 0.85rem; }
.ns-num { font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--accent); line-height: 1.1; flex-shrink: 0; }
.ns-body { flex: 1; }
.ns-q { font-family: var(--font-jp-serif); font-size: 15.5px; font-weight: 800; color: var(--ink); margin-bottom: 0.32rem; }
.ns-e { font-family: var(--font-jp-serif); font-size: 12.5px; line-height: 1.66; color: var(--ink-dim); }
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
