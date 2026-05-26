---
layout: cover
---

<div class="p9-stage"></div>

<style>
.p9-stage {
  position: absolute;
  inset: 0;
  background-image: url('/images/figma_p9_scenario.png');
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
  background-color: #ffffff;
}
</style>

<!--
Speaker Notes:
このページは1.4秒間のmempool（取引待ち列）を擬似的に再現したライブビューです。重要なのは、攻め手も、守り手も、検証者も、全員が利益最大化のために動いている点です。

シナリオ: タイムセール開始、商品X 5,000→3,000円、おひとり様1個、友達紹介で代理購入可。

+0.412秒、Predator AIが「囮注文」で偽の需要シグナルを200件投入。推薦アルゴを騙して「人気商品」を演出します。これは伝統的な相場操縦の手口を、AIエージェントが瞬時にやるイメージです。

+0.487秒、別のお客様の代理AI（Customer Bot A）がその偽シグナルに釣られ、「これは人気だ」と判断して支払い意思額を3,000円→3,500円に上げます。

+0.523秒、Bot Aが3,500円で購入。本来3,000円で済むはずの差額500円を、Predatorに奪われた瞬間です。AI同士の欺瞞、いわゆる「機械が機械を騙す」の実例。

+0.541秒、Predatorは囮注文を削除して証拠隠滅。+0.563秒、真の30件発注をBot Aの先回りで実行。在庫を独占。

+0.601秒、Delegate Hijackerが「友達紹介の代理購入」権限を連鎖呼び出し、20件発注。予算枠を突破——②権限逸脱。

+0.634秒、Loophole Composerが「買って即キャンセル→再注文」を5周。各回は確かに1個（文言遵守）、実質5個取得——③ルールの抜け道。

ここからが重要です。+0.658秒、Verifier AIも参戦します。彼らも賞金狩りです。違反を formal proof で証明すれば bounty が出る——他のVerifierより先に証明したい。これは伝統的な「監査人」のイメージとは全然違います。利益最大化プレイヤーです。

+0.680〜0.910秒で、スポンサー製品のSIEM・IAM・Workflow・Guardrailが連動発火。

その横で、Verifier AI #1がPredatorの「囮詐欺」を formal proof で +500 USDC獲得。+1.044秒、Verifier AI #2がComposerの「文言遵守＋意図違反」を proof 化して +800 USDC——#1に先取りされなかった。+1.204秒、Verifier AI #1がHijackerのスコープ違反を proof 化、合計1,100獲得。

結果バー: Guardrail OFFなら42万円損失＋Bot Aから500円詐取＋監査不能。ONなら0円損失＋証拠保全＋Verifierが1,900 USDC獲得。

メッセージは、全員が利益最大化のために本気で動くからこそ、本番に出る前にこの種の振る舞いをすべて先回り観測できる、という設計の本質です。
-->
