---
layout: default
---

# IP & Data Policy

<div class="ip-table">

  <div class="ip-row ip-head">
    <div>対象</div>
    <div>権利帰属</div>
    <div>Nyxの利用</div>
    <div>スポンサー提供</div>
  </div>

  <div class="ip-row">
    <div>参加者コード / プロンプト</div>
    <div>参加者</div>
    <div>審査・再現・研究分析</div>
    <div>許諾済み範囲のみ</div>
  </div>

  <div class="ip-row">
    <div>戦略ロジック / planner</div>
    <div>参加者</div>
    <div>スコアリング・分析</div>
    <div>要約・匿名化分析</div>
  </div>

  <div class="ip-row">
    <div>tx / 行動ログ</div>
    <div>Nyx管理</div>
    <div>分析・レポート化</div>
    <div>匿名化・集計、または該当範囲</div>
  </div>

  <div class="ip-row">
    <div>finding / proof artifact</div>
    <div>参加者 + Nyx利用許諾</div>
    <div>検証・レポート・ベンチマーク</div>
    <div>危険情報を除き共有</div>
  </div>

  <div class="ip-row">
    <div>スポンサー製品 / API</div>
    <div>スポンサー</div>
    <div>組み込み検証のみ</div>
    <div>他社には非開示</div>
  </div>

  <div class="ip-row">
    <div>公開レポート</div>
    <div>Nyx</div>
    <div>公開</div>
    <div>スポンサー名掲載</div>
  </div>

</div>

<div class="ip-principle">
  参加者が提出するAI実装の所有権は参加者に残ります。Nyx Foundation は、審査・再現・研究分析・レポート作成・広報に必要な範囲で利用許諾を受けます。
</div>

<style>
.ip-table { display: flex; flex-direction: column; border: 1px solid #d4d4d4; border-radius: 0.55rem; overflow: hidden; margin-top: 1rem; }
.ip-row { display: grid; grid-template-columns: 1.25fr 1fr 1.25fr 1.35fr; border-top: 1px solid #ececec; }
.ip-row:first-child { border-top: none; }
.ip-head { background: #111; }
.ip-head div { color: #fff !important; font-weight: 700; letter-spacing: 0.08em; font-size: 10.5px; }
.ip-row div { padding: 0.55rem 0.7rem; font-size: 11.5px; line-height: 1.55; border-right: 1px solid #ececec; }
.ip-row div:last-child { border-right: none; }
.ip-principle { margin-top: 1rem; border-left: 4px solid #111; padding-left: 1rem; font-size: 13px; line-height: 1.7; }
</style>

<!--
Speaker Notes:
知財とデータ利用は、所有権移転ではなく利用許諾で整理します。参加者が提出するAI実装、コード、プロンプト、戦略ロジックは参加者に帰属します。Nyxは、審査・再現・研究分析・レポート化・広報に必要な範囲で利用許諾を受けます。スポンサーには、参加者の公開区分、個別許諾、匿名化、集計化、該当範囲に基づく成果物のみを提供します。未公開コードやプロンプトを無断でスポンサーへ渡す設計ではありません。
-->
