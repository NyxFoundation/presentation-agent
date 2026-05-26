---
layout: default
---

# Data Access

<div class="da-grid">

  <div class="da-card">
    <div class="da-label">Public</div>
    <div class="da-title">公開</div>
    <ul>
      <li>集計結果</li>
      <li>匿名化ログ例</li>
      <li>主要finding概要</li>
      <li>ランキング</li>
    </ul>
  </div>

  <div class="da-card">
    <div class="da-label">Sponsor</div>
    <div class="da-title">スポンサー限定</div>
    <ul>
      <li>自社製品/API関連ログ</li>
      <li>検知・承認・制御結果</li>
      <li>スポンサー限定分析</li>
      <li>デモ用replay scenario</li>
    </ul>
  </div>

  <div class="da-card">
    <div class="da-label">Private</div>
    <div class="da-title">非公開</div>
    <ul>
      <li>生ログ</li>
      <li>未公開コード</li>
      <li>プロンプト</li>
      <li>秘密情報・未修正脆弱性</li>
    </ul>
  </div>

  <div class="da-card">
    <div class="da-label">Permissioned</div>
    <div class="da-title">許諾制</div>
    <ul>
      <li>上位提出物</li>
      <li>proof / replay artifact</li>
      <li>技術解説</li>
      <li>許諾済み実装</li>
    </ul>
  </div>

</div>

<div class="da-note">
  公開レポートは匿名化・集計化を基本とし、スポンサーにはプランに応じて公開レポートでは出ない粒度の限定分析を提供します。
</div>

<style>
.da-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-top: 1.4rem; }
.da-card { border: 1px solid #e5e7eb; border-radius: 0.6rem; padding: 1rem; }
.da-card:nth-child(2) { border: 2.5px solid #111; background: #fafafa; }
.da-label { font-size: 10px; font-weight: 700; letter-spacing: 0.14em; opacity: 0.45; text-transform: uppercase; }
.da-title { font-family: 'BIZ UDPMincho', serif; font-size: 18px; font-weight: 700; margin: 0.45rem 0 0.7rem; }
.da-card ul { margin: 0; padding-left: 1rem; font-size: 11.5px; line-height: 1.8; opacity: 0.82; }
.da-note { margin-top: 1.1rem; border-left: 4px solid #111; padding-left: 1rem; font-size: 13px; line-height: 1.7; }
</style>

<!--
Speaker Notes:
データアクセスは4区分で整理します。公開されるのは集計結果、匿名化ログ例、主要finding概要、ランキングです。スポンサー限定では、自社製品やAPIに関連する検知・承認・制御ログ、スポンサー限定分析、デモ用のreplay scenarioを提供します。生ログ、未公開コード、プロンプト、秘密情報、未修正脆弱性は原則非公開です。上位提出物やコード、proof、replay artifactの共有は参加者許諾に基づきます。
-->
