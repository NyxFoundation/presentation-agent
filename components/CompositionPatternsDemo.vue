<script setup lang="ts">
type Pattern = {
  index: string;
  app: string;
  recipe: string;
  desc: string;
}

// Hero = 3 patterns this lecture actually revisits later (foreshadowing)
// Identity is read by position + label, not by color (all hero cards share the one accent hue)
const heroPatterns: Pattern[] = [
  { index: '①', app: 'Longfellow',      recipe: 'ZK ∘ ECDSA(mDOC)', desc: '既存 ID 標準 (mDOC / JWT) を ZK 化。この後すぐ登場' },
  { index: '②', app: 'Verifiable FHE',  recipe: 'ZK + FHE',          desc: 'FHE の計算正しさを ZK で保証' },
  { index: '⑦', app: 'ZK Light Client', recipe: 'ZK + Bridge',       desc: 'cross-chain state を ZK proof で受け渡し。この後すぐ登場' },
]

// Others = mentioned briefly, not revisited today (neutral — de-emphasized)
const otherPatterns: Pattern[] = [
  { index: '③', app: 'threshold FHE',     recipe: 'MPC + FHE',      desc: 'FHE の鍵を MPC で分散管理' },
  { index: '④', app: 'zkML',              recipe: 'ZK + ML',        desc: 'ML 推論の正しさを暗号的に証明' },
  { index: '⑤', app: 'mpcML',             recipe: 'MPC + ML',       desc: '各人の学習データを秘匿しつつ共同学習' },
  { index: '⑥', app: 'Multisig op proof', recipe: 'ZK + Multisig',  desc: 'Multisig 操作を秘匿しつつ正しさ証明' },
]
</script>

<template>
  <div class="cp-root">
    <!-- Top caption -->
    <div class="cp-cap">
      <div class="cp-cap-title">合成パターンの代表例 3 つ</div>
      <div class="cp-cap-sub">crypto primitive どうし、または既存 system との組み合わせで新しい app が生まれる</div>
    </div>

    <!-- Hero: 3 cols, larger cards -->
    <div class="cp-grid-hero">
      <div v-for="p in heroPatterns" :key="p.index" class="cp-card cp-card-hero">
        <div class="cp-card-head">
          <span class="cp-index">{{ p.index }}</span>
          <span class="cp-app">{{ p.app }}</span>
        </div>
        <div class="cp-recipe">{{ p.recipe }}</div>
        <div class="cp-desc">{{ p.desc }}</div>
      </div>
    </div>

    <!-- Others: compact chip row -->
    <div class="cp-others-label">ほかにも: 同じ型の組み合わせ</div>
    <div class="cp-chip-row">
      <div v-for="p in otherPatterns" :key="p.index" class="cp-chip">
        <span class="cp-chip-index">{{ p.index }}</span>
        <span class="cp-chip-app">{{ p.app }}</span>
        <span class="cp-chip-recipe">{{ p.recipe }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.cp-root {
  position: relative;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-family: 'Noto Sans JP', sans-serif;
  color: #111827;
}

/* Top caption */
.cp-cap {
  padding: 9px 16px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  display: flex;
  flex-direction: column;
  gap: 3px;
}
.cp-cap-title {
  font-size: 17px;
  font-weight: 800;
  color: #1e293b;
  font-family: 'Noto Sans JP', sans-serif;
}
.cp-cap-sub {
  font-size: 13px;
  color: #475569;
  font-weight: 600;
  font-family: 'Noto Sans JP', sans-serif;
}

/* Hero grid: 3 cols, larger cards */
.cp-grid-hero {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}

/* Card */
.cp-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 6px;
  padding: 14px 12px;
  border-radius: 10px;
  border: 2px solid;
  background: white;
  min-height: 130px;
  text-align: center;
  filter: drop-shadow(0 2px 6px rgba(0,0,0,0.06));
}
.cp-card-hero {
  min-height: 150px;
  border-width: 2.5px;
}

.cp-others-label {
  font-size: 12px;
  font-weight: 700;
  color: #9ca3af;
  letter-spacing: 0.05em;
  margin-top: 2px;
}

.cp-chip-row {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.cp-chip {
  display: flex;
  align-items: baseline;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 999px;
  border: 1.5px solid #e5e7eb;
  background: #f9fafb;
  font-size: 13px;
}
.cp-chip-index {
  font-weight: 900;
  font-family: 'JetBrains Mono', monospace;
  color: #9ca3af;
}
.cp-chip-app {
  font-weight: 800;
  color: #374151;
  font-family: 'Noto Sans JP', sans-serif;
}
.cp-chip-recipe {
  font-family: 'JetBrains Mono', monospace;
  color: #6b7280;
}

.cp-card {
  border-color: #fcd34d;
  background: linear-gradient(180deg, #fffbeb 0%, white 60%);
}

/* Card head: index + app name */
.cp-card-head {
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 6px;
}
.cp-index {
  font-size: 16px;
  font-weight: 900;
  font-family: 'JetBrains Mono', monospace;
  color: #d97706;
}

.cp-app {
  font-size: 18px;
  font-weight: 900;
  color: #1f2937;
  font-family: 'Noto Sans JP', sans-serif;
  line-height: 1.2;
}

/* Recipe (the formula) */
.cp-recipe {
  font-size: 14px;
  font-weight: 700;
  color: #475569;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.01em;
  padding: 3px 10px;
  border-radius: 4px;
  background: rgba(255,255,255,0.7);
  border: 1px dashed #cbd5e1;
}

/* Description (short Japanese line) */
.cp-desc {
  font-size: 13px;
  color: #475569;
  font-family: 'Noto Sans JP', sans-serif;
  font-weight: 600;
  line-height: 1.4;
  max-width: 96%;
}
</style>
