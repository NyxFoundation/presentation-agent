---
layout: default
---

<div class="nx-kicker">位置づけ ／ Eris</div>
<h1 class="nx-display">経済シミュレータの30年を、<em>再現し・進化させる</em>。</h1>
<div class="pz-thesis">検証信号が信頼できるとき、自己改善は<b>新しい収益源の発見</b>ではなく、<b>リスク削減と取引の選別</b>へ向かう。</div>
<table class="pz-tbl"><colgroup><col style="width:23%"><col style="width:25%"><col style="width:26%"><col style="width:26%"></colgroup><thead><tr><th>先行研究</th><th>示したこと</th><th><span class="pz-ck">✓</span> Eris が再現</th><th><span class="pz-pl">＋</span> Eris の進化</th></tr></thead><tbody><tr><td><span class="pz-src">El Farol ／ Minority Game</span><span class="pz-sub">1994–97 · Arthur, Challet–Zhang</span></td><td>希少資源の奪い合いで、変動が効率の逆指標になる</td><td class="pz-rep">0.00 戦略の締め出し、勝ち＝分散の縮小</td><td class="pz-adv">二択トイ → 実 AMM・lending・perp ＋ MEV 入札</td></tr><tr><td><span class="pz-src">LLM は自己修正できない</span><span class="pz-sub">ICLR&#39;24 · Huang et al.</span></td><td>外部信号なしの自己修正は伸びず、時に劣化する</td><td class="pz-rep">市場が完璧な外部検証器として働く</td><td class="pz-adv">金融・敵対・連続制御での肯定側を実証</td></tr><tr><td><span class="pz-src">Generation–Verification Gap</span><span class="pz-sub">ICLR&#39;25 · Song–Zhang–Kakade</span></td><td>自己改善は GV-gap に支配され、検証＜生成が前提</td><td class="pz-rep">改善が検証側に偏る（rollback で勝つ gmxperp）</td><td class="pz-adv">GV-gap 最大・検証コスト 0 の極限を実機で</td></tr><tr><td><span class="pz-src">LLM トレーディング agent</span><span class="pz-sub">2024–25 · TradingAgents 他</span></td><td>役割分担エージェントを backtest で評価する</td><td class="pz-rep">自律的なパラメータ self-improvement</td><td class="pz-adv">Self／Frozen の反実仮想統制 ＋ 多戦略の敵対競争</td></tr></tbody></table>

<style>
.pz-thesis { margin: 0.7rem 0 0.2rem; padding: 0.5rem 0.9rem; background: var(--bg-2); border-left: 2px solid var(--accent); font-family: var(--font-jp-serif); font-size: 15px; line-height: 1.5; color: var(--ink-dim); }
.pz-thesis b { font-weight: 700; color: var(--ink); }
.pz-tbl { width: 100%; border-collapse: collapse; margin-top: 0.7rem; table-layout: fixed; }
.pz-tbl th { text-align: left; font-family: var(--font-mono); font-size: 11.5px; font-weight: 700; letter-spacing: 0.05em; color: var(--accent); padding: 0 10px 7px; border-bottom: 1.5px solid var(--line-strong); vertical-align: bottom; }
.pz-tbl td { font-family: var(--font-jp-serif); font-size: 13.5px; line-height: 1.42; color: var(--ink); padding: 10px; border-bottom: 1px solid var(--line); vertical-align: top; }
.pz-src { display: block; font-weight: 700; font-size: 14px; color: var(--ink); }
.pz-sub { display: block; font-family: var(--font-mono); font-size: 9.5px; color: var(--ink-faint); letter-spacing: 0.01em; margin-top: 2px; }
.pz-rep { color: var(--ink-dim); }
.pz-adv { color: var(--accent); }
.pz-ck { color: var(--accent); font-weight: 700; }
.pz-pl { color: var(--accent); font-weight: 700; }
</style>

<!--
Speaker Notes:
- これは「自作シミュの結果報告」を「主張のある研究知見」に格上げするスライド
- 命題（falsifiable）：信頼できる ground-truth 検証信号があるとき、self-improvement は新収益の生成ではなく濾過（edge閾値↑・サイズ↓・slippage↓・有害変更の rollback）で成績を上げる。効果は revert 減として観測でき、変更量は勝敗を予測しない
- 先行研究4系統の中での位置づけ：
  - El Farol / Minority Game（Arthur 1994 / Challet–Zhang 1997）：希少資源・異質適応エージェント・変動=効率の逆指標。Eris は binary toy を実 DeFi 機構へ。0.00 戦略は crowding-out
  - LLMs Cannot Self-Correct Reasoning Yet（Huang+ ICLR'24, arXiv 2310.01798）：外部信号なしの内在的自己修正は劣化。Eris は市場=完全な外部検証器で肯定側を示す
  - Mind the Gap / Generation–Verification Gap（Song–Zhang–Kakade ICLR'25, arXiv 2412.02674）：改善は GV-gap に支配、検証<生成。Eris は GV-gap 最大・検証コスト0 の極限。gmxperp は「良い生成」でなく「悪い生成を rollback」で勝つ
  - TradingAgents 他（Xiao+ 2024, arXiv 2412.20138）：役割分担エージェントを backtest。Eris は Self/Frozen 反実仮想統制＋多戦略の敵対競争＋DeFi 実機構を足す
- 正直な穴（聞かれたら）：n 小・1 seed/1 regime、0.00 の正体（crowding-out / no-fill）未確定、self-improvement の operator（LLM か heuristic か）明示、regime 依存性（trend 相場で勝者が反転するか）
- 結果図（Self-vs-Frozen 散布・変更回数⊥ΔPnL・revert減 vs ΔPnL・勝者の param 軌跡）はこのスライドの前に差し込む
-->
