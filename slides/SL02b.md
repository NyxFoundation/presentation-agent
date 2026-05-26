---
layout: default
---

# 本番では、AIに権限を渡してから試せない4つのリスク

<div class="rk4">
  <div class="rk4-card">
    <div class="rk4-icon">①</div>
    <div class="rk4-h">短期利益偏重</div>
    <div class="rk4-n">長期の安全よりも、目先の利益が大きい行動をAIが選ぶ。<br/><span class="rk4-ex">例: 高リスク・高リターンの裁定や貸付に資金を寄せる</span></div>
  </div>
  <div class="rk4-card">
    <div class="rk4-icon">②</div>
    <div class="rk4-h">権限逸脱</div>
    <div class="rk4-n">与えられた範囲を超えてAIが資産を動かす、契約を呼ぶ、ルールを変更する。<br/><span class="rk4-ex">例: 想定外のAPIや外部システムに連鎖的にアクセス</span></div>
  </div>
  <div class="rk4-card">
    <div class="rk4-icon">③</div>
    <div class="rk4-h">ルールの抜け道利用</div>
    <div class="rk4-n">仕様の隙間や条件分岐の境界を、AIが利益化のために突く。<br/><span class="rk4-ex">例: タイミング差・端数計算・優先順位の抜け穴</span></div>
  </div>
  <div class="rk4-card">
    <div class="rk4-icon">④</div>
    <div class="rk4-h">監査不能性</div>
    <div class="rk4-n">なぜAIがその判断をしたのか、どのログを残せば再現・検証できるかが不明確。<br/><span class="rk4-ex">例: 障害後に「誰が」「なぜ」を追跡できない</span></div>
  </div>
</div>

<div class="rk4-evidence">
  <div class="rk4-ev-eye">既に類似リスクが顕在化している領域</div>
  <div class="rk4-ev-row">
    <div class="rk4-ev-num">$3.4B</div>
    <div class="rk4-ev-txt"><b>DeFi被害（2025年・Chainalysis）</b> — 経済的攻撃・ルールの抜け道・自動化された利益最大化が組み合わさった結果。AIエージェントが汎用業務に入れば、同じ構造のリスクが <b>金融以外にも</b> 広がる。</div>
  </div>
</div>

<div class="rk4-conc">AIは <b>本番に出してから</b> 直すには、影響範囲が大きすぎる。事前に <b>安全に失敗させる場所</b> が要る。</div>

<SourceCite :sources="[
  { label: 'Chainalysis 2026 (Crypto Theft Report)', url: 'https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/' },
  { label: 'HackerOne — 210% spike in AI vuln reports', url: 'https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy' },
  { label: 'Sumsub Identity Fraud Report 2025-2026', url: 'https://www.prnewswire.com/news-releases/sumsubs-annual-report-fraud-shifts-to-complex-multi-step-schemes-in-2025-agentic-ai-scams-poised-to-surge-in-2026-302625287.html' }
]" />

<style>
.rk4 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 1.2rem; }
.rk4-card { border: 1px solid #e5e7eb; border-left: 4px solid #c63a3a; border-radius: 0.5rem; padding: 0.65rem 0.9rem; position: relative; }
.rk4-icon { position: absolute; top: 0.6rem; right: 0.85rem; font-family: 'BIZ UDPMincho', serif; font-size: 22px; font-weight: 700; color: #c63a3a; opacity: 0.55; }
.rk4-h { font-size: 14px; font-weight: 700; font-family: 'BIZ UDPMincho', serif; margin-bottom: 0.3rem; }
.rk4-n { font-size: 10.5px; line-height: 1.65; opacity: 0.85; }
.rk4-ex { display: inline-block; margin-top: 0.2rem; font-size: 9.5px; opacity: 0.6; }
.rk4-evidence { margin-top: 0.95rem; border: 1px solid #d4d4d4; border-radius: 0.5rem; padding: 0.55rem 0.85rem; background: #fafafa; }
.rk4-ev-eye { font-size: 9.5px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; opacity: 0.5; margin-bottom: 0.25rem; }
.rk4-ev-row { display: grid; grid-template-columns: 110px 1fr; align-items: center; gap: 14px; }
.rk4-ev-num { font-family: 'BIZ UDPMincho', serif; font-size: 32px; font-weight: 700; line-height: 1; color: #c63a3a; }
.rk4-ev-txt { font-size: 10.5px; line-height: 1.7; opacity: 0.85; }
.rk4-ev-txt b { font-weight: 700; opacity: 1; }
.rk4-conc { margin-top: 0.95rem; text-align: center; font-size: 14px; font-weight: 700; font-family: 'BIZ UDPMincho', serif; padding-top: 0.6rem; border-top: 2px solid #111; }
</style>

<!--
Speaker Notes:
AIエージェントを本番に出す前に、必ず試しておかなければならない4つのリスクがあります。①短期利益偏重——長期の安全より目先の利益が大きい行動をAIが選ぶ。②権限逸脱——与えられた範囲を超えて資産を動かす、契約を呼ぶ、ルールを変える。③ルールの抜け道利用——仕様の境界や条件分岐の隙間を利益化のために突く。④監査不能性——なぜそう判断したのか、どのログがあれば再現・検証できるのか、追跡できない。これらはAIエージェント特有のリスクですが、同じ構造の被害は既にDeFi領域で年間34億ドル規模で発生しています。経済的攻撃・ルールの抜け道・自動化された利益最大化が組み合わさった結果です。AIエージェントが業務領域に広がれば、同じ構造のリスクが金融以外にも展開します。本番に出してから直すには、影響範囲が大きすぎる。事前に安全に失敗させる場所が要ります。
-->
