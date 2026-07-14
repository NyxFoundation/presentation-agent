---
layout: default
---

# 社会的需要 ③ — <span class="text-amber-700">機関マネー × 規制プライバシー</span>

<div class="mt-10 text-center text-2xl font-bold text-gray-900 leading-relaxed">
既存金融・機関投資家はすでに on-chain に入っている —<br/>
プライバシーとコンプライアンスを<span class="text-amber-700">両立</span>できれば、さらに使われる
</div>

<div class="mt-12 flex items-stretch gap-3">

<div class="flex-1 bg-white rounded-xl border border-gray-200 shadow-sm p-4">
<div class="text-[11px] font-bold tracking-widest text-gray-400 mb-2">事実</div>
<div class="text-3xl font-black text-gray-900 mb-1">$320B</div>
<div class="text-xs text-gray-500 mb-3">Stablecoin 流通額 (2026/4)</div>
<div class="text-sm text-gray-700 leading-relaxed">
<span class="text-amber-500">&#9654;</span> RWA $32B (+200% YoY)、BlackRock BUIDL $2.4B<br/>
<span class="text-amber-500">&#9654;</span> GENIUS Act 施行 (2026/7) — 1:1 担保 + 月次監査を義務化
</div>
</div>

<div class="flex items-center text-gray-300 text-3xl font-black">→</div>

<div class="flex-1 bg-white rounded-xl border border-gray-200 shadow-sm p-4">
<div class="text-[11px] font-bold tracking-widest text-gray-400 mb-2">課題</div>
<div class="text-sm text-gray-700 leading-relaxed">
<span class="text-amber-500">&#9654;</span> <strong class="text-gray-900">全公開</strong>では取引戦略・顧客情報が漏れる<br/><br/>
<span class="text-amber-500">&#9654;</span> <strong class="text-gray-900">全秘密</strong>では監査・規制要件を満たせない<br/><br/>
既存暗号が提供できるのはこの二択だけ
</div>
</div>

<div class="flex items-center text-gray-300 text-3xl font-black">→</div>

<div class="flex-1 bg-amber-50 rounded-xl border border-amber-200 p-4">
<div class="text-[11px] font-bold tracking-widest text-amber-700 mb-2">答え</div>
<div class="text-sm text-gray-700 leading-relaxed">
選択的開示 — <strong class="text-gray-900">証明すべきことだけ</strong>を開示する<br/><br/>
<span class="text-green-500">&#10003;</span> Privacy Pools (規制対応プライバシー)<br/>
<span class="text-green-500">&#10003;</span> Longfellow (mDL の年齢証明)<br/>
<span class="text-green-500">&#10003;</span> zk-KYC / selective disclosure
</div>
</div>

</div>

<div class="absolute bottom-3 left-6 text-[10px] text-gray-400 leading-tight max-w-3xl">
Sources: Bitrue / Cointelegraph "Stablecoin Trends May 2026" ｜ RWA.xyz BUIDL data ｜ GENIUS Act (US, 2025/26) ｜ Buterin et al. "Blockchain Privacy and Regulatory Compliance" eprint 2023/1322 ｜ Google "Longfellow" OSS (Jul 2025)
</div>

<!--
Speaker Notes:

【概要】
社会的需要の 3 枚目。構図は前 2 枚と同一。ナラティブ: 「機関マネーはすでに on-chain に入っている (事実)。だが全公開と全秘密の二択のままでは拡大が止まる (課題)。プライバシーとコンプライアンスの両立を暗号で実現できれば、さらに使われる (答え)」。

【事実カード】
- Stablecoin 流通 $320B (2026/4, Bitrue/Cointelegraph): USDT $190B + USDC $78B。Stripe / Visa / Mastercard / PayPal が決済統合。
- RWA $32B (+200% YoY, RWA.xyz)。BlackRock BUIDL $2.4B、RWA Treasury $11B (Ondo / Franklin / Apollo / KKR が tokenize)。
- GENIUS Act 2026/7/18 施行: Stablecoin 発行者に 1:1 担保 + 月次監査 + 独立監査を義務化。USDC は対応、USDT は非対応 → 機関マネーは GENIUS 対応に流れる。

【課題カード】
機関プレイヤーは「全公開」では取引できない (counterparty に戦略が漏れる) が、「全秘密」では監査・規制を満たせない。既存暗号 (TLS/AES/RSA) はこの二項対立しか提供できない — 暗号化するか、しないか。

【答えカード】
選択的開示 = 「証明すべきことだけを開示し、それ以外は秘匿」。Privacy Pools (Buterin et al. eprint 2023/1322 — 「サンクションリストに載っていない」を ZK 証明)、Longfellow (Google OSS 2025/7 — mDL/mDOC の生年月日を隠したまま >=18 だけ証明、Sparkasse 提携)、zk-KYC / BBS+。ZK Bridge も同じ文脈 — 機関マネーがチェーンをまたぐとき、RPC への信頼ではなく暗号的検証で渡す (S2-C 終盤で再訪)。

【3 つの需要は偶然か必然か (口頭で締める)】
①運用の検証 ②証明の効率 ③選択的開示 — 3 つは別個の現象ではなく、「検証可能な暗号への要請」が異なる経路で噴出したもの。個別解 (Proof-of-Exploit / Jolt / Privacy Pools) は別々に設計されたのではなく、Programmable Cryptography という同じ汎用層の異なる応用。これが「今」社会実装の時期である本質。

【倫理的考察 (口頭 1 分)】
プライバシー保護は合法的取引も非合法な活動も同じく覆い隠す。Tornado Cash の OFAC 制裁 (2022) が実例。Privacy Pools のような「規制対応プライバシー」はこの緊張を解く方向性。Programmable Cryptography は中立的なツール — 「何を可能にするか」と「何を防ぐべきか」を同時に設計する必要がある。
-->
