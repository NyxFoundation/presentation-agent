---
layout: default
---

# パターン A を機能要件に落とす — <span class="text-amber-700">RISC Zero × Rust</span>

<div class="mt-2 flex justify-center">
<img src="/images/patternA_arch.png" class="max-h-[470px] w-auto object-contain" />
</div>

<!--
Speaker Notes:

【概要】
前ページの「パターン A = ZK 証明」を、実際に作るなら何を決めるか (機能要件) まで一段掘り下げる 1 枚。「どういう回路を書いて何を証明するか」「どの言語か」「Witness Generation / Proving / Verifying をいつ・どこで・どんな制約でやるか」を、RISC Zero (Rust) を例に pipeline のノードに添字する。

【① 回路記述 (Rust / RISC Zero guest)】
- 言語: Rust。RISC Zero は「Rust で書いた普通のプログラム (guest program) をそのまま zkVM で実行して証明」できる。回路 DSL を新しく覚えなくてよいのが採用理由。
- 証明する命題: env::read() で秘密の攻撃手順 W を受け取り、assert!(exploit(w, C)) で「W を入れるとコントラクト C が壊れる」ことをプログラムの実行で確かめ、env::commit で C のハッシュ (公開値) だけを出力する。W は commit しないので秘密のまま。

【② Witness Generation + Proving】
- RISC Zero では witness 生成と proving は zkVM 実行として一体。脆弱性を発見したその場で 1 回実行する。
- 実行場所: クライアント (Auditor の手元)。マシン制約は置かない — 「時間はかかってよい」という要件なので GPU クラスタは不要。ここが p8 の real-time proving 競争とは要件が違う点 (あちらは L1 ブロックを 12 秒で、こちらは脆弱性発見時に 1 回で良い)。

【③ Groth16 wrap】
- RISC Zero の生の STARK 証明は大きく、on-chain verify が高い。そこで最後に Groth16 に wrap (STARK → SNARK 変換) して証明を小さくする。
- 効果: Verification Cost が一定になる。オンチェーン検証の gas が固定なので、コントラクト側の経済設計が読める。

【④ on-chain Verify】
- Ethereum コントラクトが verify(π)。通れば「脆弱性が存在する」ことが暗号的に確定する。W の中身は出ていない。

【⑤ verify 通過後の分岐】
- 報酬が自動で支払われる: 有効な証明を出した Auditor にバウンティが payout される (証明の検証成功がトリガ)。
- 復号鍵がプロバイダに渡る: W は暗号化して預けてあり、verify 通過を条件に復号鍵がプロトコル (プロバイダ) に渡る → 中身を確認して修正できる。responsible disclosure を暗号で強制する部分。

【講義での強調点】
- 「暗号を選ぶ」の次は「Witness Gen / Proving / Verify のタイミングとコストを設計する」— これが機能要件。要件 (クライアントで 1 回・時間可・検証は一定コスト) が RISC Zero + Groth16 wrap という具体を導く。
- パターン B (MPC) / C (zkML) なら、この pipeline のノードと要件が別物になる — 午後のホワイトボードで各自が描く部分。
-->
