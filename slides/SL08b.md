---
layout: default
---

# KelpDAO × LayerZero $292M — <span class="text-amber-700">1-of-1 DVN</span> の罠

<KelpAttackDemo />

<div class="absolute bottom-3 left-6 text-[10px] text-gray-400 leading-tight max-w-3xl">
Sources: Chainalysis "Inside the KelpDAO Bridge Exploit" (Apr 2026, 仮想) ｜ LayerZero Labs "Post-mortem: April 18 Exploit" (Apr 2026, 仮想) ｜ KelpDAO "Response to LayerZero Statement" (Apr 2026, 仮想) ｜ LayerZero V2 OAppConfig docs
</div>

<!--
Speaker Notes:

【事件概要】
116,500 rsETH (~$292M) 流出 ｜ 2026/4/18 ｜ Lazarus / TraderTraitor 帰属。

【重要な前提】
これは 2026 年想定の仮想シナリオです (実在事件ではなく Week 1 教材として設計)。ただし攻撃メカニクスは LayerZero V2 の DVN 構成と RPC infrastructure 依存の現実的な脆弱性パターンに基づきます。コントラクトコードは監査済 (bug なし)、ハードウェア署名・LayerZero ULN302 verify はすべて仕様通りに動いた。攻撃面は DVN が参照する RPC node infrastructure (オフチェーン)。

【概念図の読み方】
左から右に bridge flow が流れています — User (Karak L2) で rsETH を burn → L0 Endpoint が「dst chain で verify してほしい」というメッセージを送出 → DVN cluster (off-chain multisig) が「source chain でその burn は本当に起きたか?」を検証 → ULN302 (Ethereum dst 側 LZ contract) が DVN の attestation を verify → rsETH Bridge が release。
DVN が source chain 状態を verify するために、Karak L2 の RPC nodes 群に polling します (下向き矢印 = query、上向き矢印 = response)。RPC nodes は Karak L2 チェーン状態のミラーです。

【各 phase の物語】
phase 0 — 本来の姿: 3 DVN multisig が独立に source chain 状態を verify、healthy な polling traffic が流れている。
phase 1 — Kelp の deployment 選択: `requiredDVNCount: 1` を設定 → 3 DVN multisig が "1 票" に縮退。DVN #2, #3 は signing path から外れる (× で fade)。この 1 行の config が攻撃面の本質。
phase 2 — Lazarus は事前に内部 RPC 2 台のバイナリを差し替え。普段は正常応答、特定 query にだけ嘘を返す lazy backdoor。
phase 3 — 攻撃当日: 外部 RPC 3 台を DDoS でダウンさせ、応答できるのは内部 2 台 (改ざん済) だけにする。
phase 4 — 残った 2 RPC が "BURN ✓" の嘘で応答 → DVN は majority-of-responding (2/2 = 100% consensus) と誤判定 → 偽 attestation に署名。DVN 自身は仕様通りに動いている (バグなし)。
phase 5 — rsETH Bridge は 1 DVN signature を OAppConfig 通りに verify し release(0xAttacker, 116,500 rsETH) を実行。116,500 rsETH (~$292M) drain。

【講義での強調点】
- コードは無傷、すべての contract は監査済で仕様通り動いた
- 攻撃面は deployment config の選択 (`requiredDVNCount: 1`) + RPC infrastructure 依存
- もし 2-of-3 DVN なら 3 つの独立した RPC topology を同時に落とす必要 → 現実的に止まる
- もし ZK light client なら source chain 状態を on-chain で暗号的に verify → RPC の嘘では release が走らない
- 午後のホワイトボードで「ZK light client なら防げたか?」を議論する伏線
- S1-A 「攻撃面 ⊃ 防御スコープ」の最も触感的な実例
-->
