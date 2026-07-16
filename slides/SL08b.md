---
layout: default
---

# KelpDAO <span class="text-amber-700">事件</span>

<div class="mt-2 flex justify-center">
<img src="/images/kelp_arch_static.png" class="max-h-[440px] w-auto object-contain" />
</div>

<div class="absolute bottom-3 left-6 text-[10px] text-gray-400 leading-tight max-w-3xl">
Sources: Chainalysis "Inside the KelpDAO Bridge Exploit" (Apr 2026, 仮想) ｜ LayerZero Labs "Post-mortem: April 18 Exploit" (Apr 2026, 仮想) ｜ KelpDAO "Response to LayerZero Statement" (Apr 2026, 仮想) ｜ LayerZero V2 OAppConfig docs
</div>

<!--
Speaker Notes:

【事件概要】
116,500 rsETH (~$292M) 流出 ｜ 2026/4/18 ｜ Lazarus / TraderTraitor 帰属。

【重要な前提】
これは 2026 年想定の仮想シナリオです (実在事件ではなく Week 1 教材として設計)。ただし攻撃メカニクスは LayerZero V2 の DVN 構成と RPC infrastructure 依存の現実的な脆弱性パターンに基づきます。コントラクトコードは監査済 (bug なし)、ハードウェア署名・LayerZero ULN302 verify はすべて仕様通りに動いた。攻撃面は DVN が参照する RPC node infrastructure (オフチェーン)。

【概念図の読み方 (静的アーキ図、侵害された瞬間の全体像。枠を一切使わず、アイコン+ラベル+直角の線 (標準的なアーキ図の描き方) だけで状態を伝える設計。生成スクリプト: figures/kelp_arch.py)】
この図は 2026/4/18 に実際に起きたことだけを描いています (対策側の話は p6 で扱う)。エンティティの囲み枠・セクション見出しは一切なし: チェーンの識別はエンティティラベル (Karak L2 Contract / Ethereum Contract)、RPC のチェーンスコープはラベル「Karak RPC #N」に畳み込み、LayerZero の帰属はベンダー境界バンド (下記) が担う。アイコンは形=役割 (シールド=検証者 DVN、サーバースタック=RPC)、色=状態。矢印はすべて直角 (縦・横) で接続する標準的なアーキテクチャ図の描き方。
- 左: User (アイコンのみ) → 矢印の上に「burns rsETH」ラベルが直接乗る → Karak L2 Contract (Karak ロゴをそのままアイコンとして使用)。
- 中央上: `setConfig(requiredDVNCount: 1)` は枠なしのプレーンなコード行 (図全体の boxless トンマナに合わせる)。致命的な値「1」だけを赤+細枠で強調し、その真下から垂直の赤い破線リーダーが DVN #1 のアイコン上辺に着地する (「この config 値が DVN #1 を 1-of-1 にした」という因果を一本の垂直線で示す)。
- 中央: DVN 3 台の検証レイヤー全体を淡い破線の「LayerZero バンド」(左上に LayerZero ロゴ+名前) で囲い、この多重検証機構が LayerZero のブリッジ基盤であることを領域で示す。burns/release の矢印と偽応答トランクがバンドの縁を横切る = メッセージも攻撃もこの LayerZero レイヤーを通過する。DVN #1 (amber・実線シールドアイコン) がメインの流れの上に乗って「active・signs (1-of-1)」を実行する一方、DVN #2/#3 は左右のやや下に破線アウトラインのシールド (ghost) として配置し「未参加」と明示。本来 3 台必要な多重検証のうち 2 台がそもそも不在であることを、凡例ではなく形 (実線 vs 破線ゴースト) と配置だけで伝える。
- 下段: Karak RPC 5 台 (サーバースタックアイコン) を DVN #1 の直下にクラスタ配置 (= DVN #1 の情報源プールであることを空間で示す)。改ざん済みの Karak RPC #1/#2 (赤・実線) だけがトランク (x 中央) の両脇に立ち、2 本の赤い破線が上昇して合流点 (赤い丸) で 1 本にまとまり、「偽の応答」ラベル付きの単一矢印として DVN #1 の下辺に入る。DVN #1 のラベルは白地で線上に座り、線がテキストを貫通しない。Karak RPC #3-5 (オフライン) は破線ゴーストのグレーアイコンのみで、DVN #1 への接続線はなし (そもそも応答していないことを線の不在で示す)。ゴースト DVN #2/#3 は赤い配線の外側にあり、偽の応答が届くのは DVN #1 だけだと読める。
- 右: DVN #1 の署名 (赤い実線矢印、矢印上に「release() 実行」ラベル) が Ethereum Contract (Ethereum ロゴをそのままアイコンとして使用) に到達。Ethereum Contract のラベルは中立色のまま (コントラクトは仕様通り動いた=無傷)。被害はその下の赤い「−116,500 rsETH（$292M）流出」ラベルで示す (被害プロトコルの識別はスライドタイトルの KelpDAO が担う)。ULN302 の検証と rsETH Bridge の release() は 1 つのノードにまとめて表示、ノード下に説明文は置かない (詳細は本ノートで補足)。

DVN 自身もコントラクトも仕様通りに動いている (バグなし) — 唯一の攻撃面は上部の config 値 `requiredDVNCount: 1` であることを、色と形 (グレー破線ゴースト=未参加/オフライン、赤=compromised/攻撃経路、amber実線=かろうじて生きている唯一の経路、中立色=無傷) だけで一目で伝える設計です。

【講義での強調点】
- コードは無傷、すべての contract は監査済で仕様通り動いた
- 攻撃面は deployment config の選択 (`requiredDVNCount: 1`) + RPC infrastructure 依存
- もし 2-of-3 DVN なら 3 つの独立した RPC topology を同時に落とす必要 → 現実的に止まる
- もし ZK light client なら source chain 状態を on-chain で暗号的に verify → RPC の嘘では release が走らない
- 次の p6 (Proof-of-Exploit) で、この事件を具体的に防ぐには何が必要だったかを、この図との差分として見せる
- S1-A 「攻撃面 ⊃ 防御スコープ」の最も触感的な実例
-->
