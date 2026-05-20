---
layout: default
---

# 4つの嵐に、研究で応える

<div class="grid grid-cols-3 gap-3 mt-3">

  <div class="rd-card">
    <div class="rd-storm">嵐 ②</div>
    <div class="rd-logo-box">
      <img src="/images/speca_logo.png" alt="SPECA" />
    </div>
    <div class="rd-name">SPECA</div>
    <div class="rd-desc">AI時代のセキュリティ — AIエージェントが守る監査・脆弱性発見</div>
  </div>

  <div class="rd-card">
    <div class="rd-storm">嵐 ①＋③</div>
    <div class="rd-logo-box">
      <img src="/images/verity_logo.jpg" alt="Verity" />
    </div>
    <div class="rd-name">Verity</div>
    <div class="rd-desc">正しさを数学で証明する形式検証と、耐量子暗号への移行</div>
  </div>

  <div class="rd-card">
    <div class="rd-storm">嵐 ④</div>
    <div class="rd-logo-box rd-defi-mark">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M4 10h5l3-5 3 10 3-5h5"/><path d="M4 17h16" opacity="0.4"/></svg>
      <div class="rd-defi-text">DeFi Analytics</div>
    </div>
    <div class="rd-name">DeFi分析</div>
    <div class="rd-desc">MEV・流動性・分配の偏りを定量し、より公平な市場設計へ</div>
  </div>

</div>

<div class="rd-foundation">
  <div class="rd-found-label">全ての基盤 / 分散システム研究</div>
  <img src="/images/eris_logo.png" alt="Eris" class="rd-found-logo" />
  <div class="rd-found-desc">嵐①〜④すべてが立つ土台 — ノード・コンセンサス・ネットワーク</div>
</div>

<div class="rd-achievements">
  <div class="ach-h">研究開発の実績</div>
  <div class="grid grid-cols-4 gap-2.5">
    <div class="ach"><div class="ach-fig">#1</div><div class="ach-t">Sherlock 監査コンテスト<br/><b>世界1位</b></div></div>
    <div class="ach"><div class="ach-fig">5本+</div><div class="ach-t">国際学会<br/><b>採択</b></div></div>
    <div class="ach"><div class="ach-fig"><img src="/images/partners/ef_horizontal.png" alt="EF" class="ach-ef" /></div><div class="ach-t">イーサリアム財団<br/><b>研究助成金 採択</b></div></div>
    <div class="ach"><div class="ach-fig ach-fig-tx">Cambridge</div><div class="ach-t">EF Retreat 招待<br/><b>ケンブリッジ大で発表</b></div></div>
  </div>
</div>

<style>
.rd-card {
  display: flex; flex-direction: column; align-items: center; text-align: center;
  gap: 0.35rem; padding: 0.75rem 0.7rem 0.85rem;
  border: 1px solid #e5e7eb; border-radius: 0.7rem;
}
.rd-storm { font-size: 9.5px; font-weight: 700; opacity: 0.55; letter-spacing: 0.08em; }
.rd-logo-box {
  height: 54px; width: 100%;
  display: flex; align-items: center; justify-content: center;
  padding: 4px 8px;
}
.rd-logo-box img { max-height: 46px; max-width: 100%; object-fit: contain; }
.rd-defi-mark { gap: 6px; }
.rd-defi-mark svg { width: 28px; height: 28px; color: #111; }
.rd-defi-text { font-size: 12px; font-weight: 700; opacity: 0.7; letter-spacing: 0.06em; }
.rd-name { font-size: 14px; font-weight: 700; font-family: 'BIZ UDPMincho', serif; }
.rd-desc { font-size: 9.5px; opacity: 0.65; line-height: 1.55; }

.rd-foundation {
  margin-top: 0.75rem;
  display: grid; grid-template-columns: auto 1fr auto; align-items: center; gap: 1rem;
  padding: 0.55rem 1rem;
  border: 2px solid #000; border-radius: 0.6rem;
  background: #fafafa;
}
.rd-found-label { font-size: 9.5px; font-weight: 700; opacity: 0.7; letter-spacing: 0.08em; white-space: nowrap; }
.rd-found-logo { height: 30px; max-width: 240px; object-fit: contain; justify-self: center; }
.rd-found-desc { font-size: 9.5px; opacity: 0.65; white-space: nowrap; text-align: right; }

.rd-achievements { margin-top: 0.85rem; }
.ach-h { font-size: 11px; font-weight: 700; opacity: 0.55; letter-spacing: 0.08em; margin-bottom: 0.45rem; }
.ach {
  padding: 0.55rem 0.7rem;
  border: 1px solid #e5e7eb; border-radius: 0.55rem;
  display: grid; grid-template-columns: 70px 1fr; align-items: center; gap: 0.7rem;
}
.ach-fig {
  font-size: 22px; font-weight: 700; font-family: 'BIZ UDPMincho', serif;
  line-height: 1; text-align: center;
}
.ach-fig.ach-fig-tx { font-size: 13px; font-family: 'BIZ UDPMincho', serif; letter-spacing: 0.02em; }
.ach-ef { height: 22px; max-width: 70px; object-fit: contain; display: block; margin: 0 auto; }
.ach-t { font-size: 9.5px; opacity: 0.75; line-height: 1.45; }
.ach-t b { font-weight: 700; opacity: 1; }
</style>

<!--
Speaker Notes:
4つの嵐に対して、Nyx Foundation は4つの研究プロジェクトで応えています。嵐②、AIによる攻撃の自律化には「SPECA」——AIエージェント自身が監査を実行し、脆弱性を先に見つける仕組み。嵐①と③、耐量子移行と「動くのに間違っている」問題には「Verity」——数学で正しさを証明する形式検証と、耐量子暗号への安全な移行を担います。嵐④、お金が偏って流れる問題には「DeFi Analytics」——MEVや流動性、分配の偏りを定量化し、より公平な市場設計の原理を取り出す。そしてこの3つすべてが立つ土台が「Eris」——ノード・コンセンサス・ネットワーク層を扱う分散システム研究です。実績としては、Sherlockのスマートコントラクト監査コンテストで世界1位、国際学会への論文採択が5本以上、イーサリアム財団の研究助成金に採択、そしてイーサリアム財団のリトリートに招待され、ケンブリッジ大学で研究発表を行いました。論文と実装、両方で世界の最前線に立っています。
-->
