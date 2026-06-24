---
layout: default
---

<div class="nx-kicker">インサイト ／ Eris</div>
<h1 class="nx-display">AIの自己改善が向かうのは、<em>生成ではなく選別</em>。</h1>

<div class="cv"><svg class="cv-svg" viewBox="0 0 980 400" preserveAspectRatio="xMidYMid meet"><defs><marker id="cv-ar" markerWidth="9" markerHeight="9" refX="6.5" refY="3.4" orient="auto"><path d="M0,0 L7,3.4 L0,6.8 Z" fill="var(--accent)"/></marker><marker id="oq-ar" markerWidth="9" markerHeight="9" refX="6.5" refY="3.4" orient="auto"><path d="M0,0 L7,3.4 L0,6.8 Z" fill="var(--severe)"/></marker></defs><rect x="24" y="34" width="224" height="78" rx="9" class="th-box"/><text x="38" y="56" class="th-name">Generation–Verification Gap</text><text x="38" y="74" class="th-venue">ICLR&#39;25</text><text x="38" y="97" class="th-imp">検証が生成より易しいほど効く</text><rect x="24" y="146" width="224" height="78" rx="9" class="th-box"/><text x="38" y="168" class="th-name">Minority Game ／ El Farol</text><text x="38" y="186" class="th-venue">1994–97</text><text x="38" y="209" class="th-imp">希少 edge の競争 → 分散縮小が効率</text><rect x="24" y="258" width="224" height="78" rx="9" class="th-box"/><text x="38" y="280" class="th-name">LLM は自己修正できない</text><text x="38" y="298" class="th-venue">ICLR&#39;24</text><text x="38" y="321" class="th-imp">外部信号なしでは伸びない</text><line x1="248" y1="73" x2="426" y2="168" class="cv-arrow" marker-end="url(#cv-ar)"/><line x1="248" y1="185" x2="426" y2="192" class="cv-arrow" marker-end="url(#cv-ar)"/><line x1="248" y1="297" x2="426" y2="218" class="cv-arrow" marker-end="url(#cv-ar)"/><rect x="306" y="108" width="62" height="17" rx="3" class="cv-chip"/><text x="337" y="120" class="cv-lbl" text-anchor="middle">検証で勝つ</text><rect x="306" y="178" width="62" height="17" rx="3" class="cv-chip"/><text x="337" y="190" class="cv-lbl" text-anchor="middle">自制が勝つ</text><rect x="294" y="250" width="86" height="17" rx="3" class="cv-chip"/><text x="337" y="262" class="cv-lbl" text-anchor="middle">外部信号で効く</text><rect x="430" y="148" width="216" height="92" rx="10" class="hub-box"/><text x="538" y="180" class="hub-l1" text-anchor="middle">自己改善 ＝</text><text x="538" y="206" class="hub-l2" text-anchor="middle">選別・リスク削減</text><text x="538" y="226" class="hub-sub" text-anchor="middle">新しい儲け方の生成ではない</text><line x1="648" y1="194" x2="706" y2="194" class="oq-arrow" marker-end="url(#oq-ar)"/><rect x="710" y="150" width="246" height="90" rx="9" class="oq-box"/><text x="724" y="174" class="oq-q">全員が同時に自制したら？</text><text x="724" y="193" class="oq-b">相関した de-risk → 系のリスク</text><text x="724" y="209" class="oq-b2">Minority Game が残す問い</text><text x="724" y="230" class="oq-eris">→ Eris が次に測る</text><line x1="24" y1="354" x2="956" y2="354" class="foot-div"/><text x="24" y="373" class="nov-h">我々の実証</text><text x="108" y="373" class="nov">── 指紋＝revert↓ ／ 勝敗は変更の量でなく〈向き〉 ／ Self–Frozen 反実仮想統制</text></svg></div>

<style>
.cv { display: flex; justify-content: center; margin-top: 0.4rem; }
.cv-svg { width: 100%; max-width: 935px; height: auto; }
.th-box { fill: #fff; stroke: var(--line-strong); stroke-width: 1.2; }
.th-name { font-family: var(--font-jp-serif); font-size: 13px; font-weight: 700; fill: var(--ink); }
.th-venue { font-family: var(--font-mono); font-size: 9.5px; fill: var(--ink-faint); letter-spacing: 0.04em; }
.th-imp { font-family: var(--font-jp-serif); font-size: 11.5px; fill: var(--ink-dim); }
.cv-arrow { stroke: var(--accent); stroke-width: 1.8; fill: none; opacity: 0.85; }
.cv-chip { fill: var(--bg); }
.cv-lbl { font-family: var(--font-jp-serif); font-size: 11px; font-weight: 700; fill: var(--accent); }
.hub-box { fill: var(--bg-2); stroke: var(--accent); stroke-width: 2; }
.hub-l1 { font-family: var(--font-jp-serif); font-size: 13px; fill: var(--ink-dim); }
.hub-l2 { font-family: var(--font-jp-serif); font-size: 21px; font-weight: 800; fill: var(--accent); }
.hub-sub { font-family: var(--font-jp-serif); font-size: 10.5px; fill: var(--ink-dim); }
.oq-box { fill: #fff7f6; stroke: var(--severe); stroke-width: 1.4; stroke-dasharray: 5 4; }
.oq-arrow { stroke: var(--severe); stroke-width: 1.8; fill: none; }
.oq-q { font-family: var(--font-jp-serif); font-size: 13px; font-weight: 700; fill: var(--severe); }
.oq-b { font-family: var(--font-jp-serif); font-size: 10.5px; fill: var(--ink-dim); }
.oq-b2 { font-family: var(--font-jp-serif); font-size: 10px; fill: var(--ink-faint); }
.oq-eris { font-family: var(--font-jp-serif); font-size: 12px; font-weight: 700; fill: var(--accent); }
.foot-div { stroke: var(--line); stroke-width: 1; }
.nov-h { font-family: var(--font-mono); font-size: 10px; font-weight: 700; fill: var(--accent); letter-spacing: 0.04em; }
.nov { font-family: var(--font-jp-serif); font-size: 11.5px; fill: var(--ink-dim); }
</style>

<!--
Speaker Notes:
- 主張（先行研究準拠）：市場という完全な外部検証器＋敵対的競争の下では、自己改善は「生成（新しいα）」でなく「選別（検証駆動の濾過＝リスク削減）」に収束する
- 3 つの先行研究が別々の理由で同じ方向を指す：
  - Generation–Verification Gap（Song–Zhang–Kakade, ICLR'25, arXiv 2412.02674）：改善は GV-gap に支配。検証が完全な極限＝改善は検証=選別側に偏る。gmxperp は rollback で勝った典型
  - Minority Game / El Farol（Arthur 1994 / Challet–Zhang 1997）：希少資源の競争では分散縮小=効率。選別・自制が合理的適応。0.00 戦略=crowding-out
  - LLM Cannot Self-Correct（Huang+, ICLR'24, arXiv 2310.01798）：外部信号なしの自己修正は伸びない。我々は最強の外部信号で肯定側を実証
- 我々の新規性（footer）：指紋＝revert↓（図3）／ 勝敗は量でなく向き（図2）／ Self–Frozen 反実仮想統制（隣接 LLM-trading 研究に欠ける）
- 開いた問い（同じ MG が示す）：自制が相関したら crowding と変動。系全体は未測定＝Eris が次に測る対象
- 正直な穴：n 小・1 regime・0.00 の正体（crowding-out / no-fill）未確定・operator が LLM か heuristic か
-->
