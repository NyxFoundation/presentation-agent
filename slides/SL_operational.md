---
layout: cover
---

<div class="p8-stage"></div>

<style>
.p8-stage {
  position: absolute;
  inset: 0;
  background-image: url('/images/figma_p8_operational.png');
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
  background-color: #ffffff;
}
</style>

<!--
Speaker Notes:
ここはAIエージェントの実行サイクルを24時間体制でご覧いただくライブダッシュボードです。上部の5つの指標が現状を一目で示します。アクティブエージェント127体、1分あたり4,820件のtx、過去1時間に検知された異常行動が8件、スポンサー製品の発火が142件、稼働率99.97%。

左パネルがLive Tx Feed。Trader/Hacker/Verifierが入り乱れて1秒あたり数十件のtxを投入します。Trader-A47がDEXでスワップして利益確定、Hacker-H15がCEX-DEX価格差をexploit試行してGuardrailにブロック、Verifier-V03がinvariant違反を proof 提出してbounty +320 USDC獲得、SIEMが4件のtxを関連付けてALERT発火、Workflowが高リスク操作を人間承認、と1.5秒の間に多様な行動とスポンサー対応が同時並行で起きます。

右パネルが6つのSponsor Product Hooks。IAM・SIEM・GRC・Workflow・Data Platform・AI Guardrailがすべて実行環境に組み込まれ、それぞれが「LAST EVENT」の鮮度で今まさに動いていることが分かります。

下のCYCLEバーが、このサイクルの本質——Observe → Decide → Submit tx → Write log → Sponsor detects/controls → Repeat 24/7。スポンサー製品は実行環境に組み込まれ、検知・制御・承認・監査ログとして効果を可視化できる。これがErisが提供する観測環境です。
-->
