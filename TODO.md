# TODO — ACP26 Week 1 デッキ改修

ページ番号は現行 `slides.md` の include 順 (2026-07-13 時点)。着手前に対応を再確認すること。

## p6 (slides/SL09.md) — Proof-of-Exploit 図の差分化

- [x] p4 (SL08b) の KelpDAO アーキ図からの**技術差分がわかる図**に更新する。
      p4 と同じ actor 配置・同じ設計語彙 (`/arch-diagram` スキル、`figures/kelp_arch.py` ベース) で描き、
      「何が追加されたか」(ZK Verifier / Circuit-Breaker 等) だけが新要素として浮き上がる構成にする。

## p7 (slides/SL10.md) — メッセージの絞り込み + ナラティブ 2 枚追加

- [x] p7 は「AI × システム運用検証」のみに絞る。p4-6 の流れを受けて
      **「サイバーセキュリティの防御範囲を広げるために Programmable Cryptography の社会実装が必要」**
      というメッセージだけにする。
- [x] 次に **Ethereum Scaling のナラティブ**を同じ構図で説明するスライドを追加。(SL10b)
- [x] その次に **既存金融・機関投資家が入っている → プライバシーとコンプラの両立を実現すればさらに使われる**
      というナラティブのスライドを追加。(SL10c)

## p8 (slides/SL12.md) — 静的図化

- [x] 場面ごとのアニメーションをやめて**静的な図**にする (`/arch-diagram` スキル)。(figures/proof_meanings.py)

## p10 (slides/SL15.md) — Programmable Cryptography 図

- [x] 上部のステージごと説明は削除。
- [x] p9 (SL14) のように常にぐるぐる回り続けるが、**どの場面で切り取っても説明できる図**にする。

## p11 (slides/SL16.md) — 削除

- [x] 合成パターンはここでの説明は不要なので**スライドごと削除** (slides.md の include も外す)。

## p12-15 (slides/SL17.md, SL18.md, SL20.md, SL21.md) — ナラティブ化

- [x] p3 (SL07) のように**ナラティブとなる「実用性の変化グラフ」**を表示する構成に変える。
      グラフ上に具体的なプロジェクトのロゴ・名前を入れる (ロゴは `public/logos/` + 実寸逆算 zoom)。
      (figures/trend_{frontier,sumcheck,commit,longfellow}.py + trend_common.py)
- [x] 具体的な技術の説明はここでは省略する。(技術詳細は speaker notes と SL19 に移設)

## p16 (slides/SL22.md) — ZK Bridge の位置づけ変更

- [ ] ZK Bridge は前述の**機関投資家マネーのナラティブ**の文脈で使う (単独技術解説をやめる)。

## p17 (slides/SL23.md) — ライブデモ

- [ ] ライブデモを追加する。

## p18-23 (slides/SL25.md, SL26.md, SL27.md, SL28.md, SL29.md, SL31.md) — 講義向け改善

- [ ] もっと講義用にわかりやすくする。

## p24 (slides/SL32.md) — まとめ

- [ ] もっと簡潔にする。
