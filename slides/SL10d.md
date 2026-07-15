---
layout: default
---

# 社会的需要 ③ — <span class="text-amber-700">Ethereum 全体がプライバシー前提になる</span>

<div class="mt-2 flex justify-center">
<img src="/images/eth_privacy_arch.png" class="max-h-[450px] w-auto object-contain" />
</div>

<div class="absolute bottom-3 left-6 text-[10px] text-gray-400 leading-tight max-w-3xl">
Sources: Buterin "A maximally simple L1 privacy roadmap" ethereum-magicians (Apr 2025) ｜ EF Blog "The Ethereum Foundation's Commitment to Privacy" / Kohaku (Oct 2025) ｜ PSE → Privacy Stewards of Ethereum roadmap (Sep 2025) ｜ PSE "Ethereum Privacy: Private Information Retrieval" (Jun 2025) ｜ ConsenSys Privacy Notice (Nov 2022) ｜ Shutter Network docs (Gnosis Chain 稼働)
</div>

<!--
Speaker Notes:

【概要 (需要 ③)】
Ethereum 側のもう一つの需要: プライバシー領域の拡大。tx の一生 (wallet → RPC → EL の mempool → CL consensus) をアーキテクチャで描くと、「暗号がどこを守っていたか」が一目で分かる — これまでは User↔RPC の通信路 (TLS) だけ。これからは EF のロードマップ自体が経路全体のプライバシーを前提にしている。

【上段 (これまで) の読み方 — 事実の裏付け】
- User→RPC の緑の線 = TLS。守られているのは「通信の中身を第三者が盗聴できない」ことだけ。
- RPC provider には全部見える: PSE の PIR 研究ノート (2025/6) の一次記述 — eth_getBalance / eth_call / eth_getStorageAt は「照会アドレス・照会のタイミングと頻度・IP とデバイス指紋」を露出し、「RPC endpoint はユーザをプロファイルし deanonymize しうる」。ConsenSys は 2022/11 にプライバシーポリシーで「MetaMask がデフォルト RPC (Infura) を使う場合、IP アドレスと wallet アドレスを収集する」と自認した (収集点が RPC provider であることを事業者自身が認めた事件)。
- EL の mempool は平文で validator に可視 (front-running / censorship の温床)。チェーン上は全公開。
- 下のバー: 緑 (暗号化) は最初の区間だけで、残りは黄色 (可視) — 「どこからどこまで」の答え。

【下段 (これから) の読み方 — すべて実在のプロジェクト】
- Kohaku: EF の privacy-first wallet SDK / リファレンス実装 (2025/10/8 の EF ブログ「Commitment to Privacy」で Privacy Cluster とともに公表、Devconnect ARG 2025/11 で Vitalik がデモ)。Railgun / Privacy Pools 統合、provider 抽象化、post-quantum ERC-4337 account を含む。
- PIR read: 「どのデータを読んだかをサーバに明かさず取得する」暗号技術。Vitalik の L1 privacy roadmap (2025/4) は読み取りプライバシーを「短期は TEE、長期は PIR に置換」と明記。PSE (2025/9 に Privacy Stewards of Ethereum へ改名) の 3 トラックの 1 つが Private Reads。引用スキーム: Spiral / Respire / TreePIR。
- shielded write: Privacy Pools / Railgun をウォレットに統合し、送金をデフォルトで shielded に (Vitalik roadmap の第 1 項目)。
- encrypted mempool: threshold 暗号で tx を包み、ブロック取り込みまで validator にも中身が見えない。Shutter Network の「shutterized」mempool が Gnosis Chain でメインネット稼働中 (Ethereum L1 へはロードマップ文書段階)。
- CL / on-chain: 見えるのは証明とコミットメントだけ — 全公開の台帳からの転換。

【需要としての意味 (聞き手に補完させる)】
「セキュリティ (①) と耐量子 (②) に続いて、Ethereum 本体のロードマップがプライバシー暗号 (PIR / shielded pool / threshold 暗号 / ZK) を標準部品として要求し始めた」— つまり Programmable Cryptography の実装スキルは L1 の中核ロードマップに直結する。

【正確性の注意】
- 「TLS が守るのは通信路だけ」という言い回し自体の単一出典はない (合成命題)。構成事実はそれぞれ一次出典あり: RPC への露出 (PSE)、Infura の収集自認 (ConsenSys)、平文 mempool (Shutter)、チェーン全公開 (Vitalik roadmap の前提)。
- 「RPC-PIR」という固有プロジェクト名は存在しない — PSE の Private Reads トラック + PIR 研究の総称として使う。
- Kohaku は未監査 ("NOT READY FOR PRODUCTION USE")。encrypted mempool の L1 導入は未実装 (Gnosis で稼働)。「前提になりつつあるロードマップ」であって「全部できている」ではない。
-->
