<script setup lang="ts">
// 時間軸 2 段構成 (キャプションなし、左余白活用、wider cards)
//   Row 1 (2010-2023 歴史):    上 = commitment / 下 = proving system
//   Row 2 (2024-2026 最新):    上 = commitment / 下 = proving system (zoom)
type Era = 'classic' | 'hash' | 'fold' | 'modern' | 'latest'
type Side = 'commit' | 'prove'

type Milestone = {
  id: string;
  side: Side;
  year: string;
  x: number;
  label: string;
  sub: string;
  era: Era;
}

// ===== Row 1: 2010-2023 歴史 (sparse, wider cards) =====
const row1: Milestone[] = [
  // commitment (above) — 3 cards, width 180, generous spacing
  { id: 'kzg',       side: 'commit', year: '2010', x: 250,  label: 'KZG',        sub: 'pairing / setup', era: 'classic' },
  { id: 'fri',       side: 'commit', year: '2017', x: 620,  label: 'FRI',        sub: 'hash-based',      era: 'hash'    },
  { id: 'brakedown', side: 'commit', year: '2023', x: 1010, label: 'Brakedown',  sub: 'linear-time',     era: 'hash'    },
  // proving (below) — 5 cards, width 170
  { id: 'groth16',   side: 'prove',  year: '2016', x: 240,  label: 'Groth16',    sub: 'pairing SNARK',   era: 'classic' },
  { id: 'stark',     side: 'prove',  year: '2018', x: 435,  label: 'STARK',      sub: 'hash-based',      era: 'hash'    },
  { id: 'plonk',     side: 'prove',  year: '2019', x: 625,  label: 'PLONK',      sub: 'universal',       era: 'hash'    },
  { id: 'halo2',     side: 'prove',  year: '2020', x: 820,  label: 'Halo2',      sub: 'accumulation',    era: 'hash'    },
  { id: 'nova',      side: 'prove',  year: '2022', x: 1015, label: 'Nova',       sub: 'folding / IVC',   era: 'fold'    },
]
const row1Commit = row1.filter(m => m.side === 'commit')
const row1Prove  = row1.filter(m => m.side === 'prove')
</script>

<template>
  <div class="cf-root">
    <svg class="cf-svg" viewBox="0 0 1200 300" preserveAspectRatio="xMidYMid meet">
      <defs>
        <marker id="cf-ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0,0 L 10,5 L 0,10 z" fill="#94a3b8"/>
        </marker>
      </defs>

      <!-- =========================================================
           ROW 1: 2010-2023 歴史
           ========================================================= -->
      <text x="20" y="22" class="cf-row-header">▸ 2010 → 2023  歴史</text>

      <text x="20" y="92" class="cf-side-label cf-side-commit">commitment</text>
      <text x="20" y="225" class="cf-side-label cf-side-prove">proving system</text>

      <!-- Commit cards (above, 180 wide) -->
      <g v-for="m in row1Commit" :key="m.id" :class="['cf-node', `cf-era-${m.era}`]">
        <line :x1="m.x" y1="135" :x2="m.x" y2="108" class="cf-stub"/>
        <rect :x="m.x - 90" y="40" width="180" height="68" rx="9" class="cf-card-bg"/>
        <text :x="m.x" y="68" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="92" text-anchor="middle" class="cf-card-sub">{{ m.sub }}</text>
        <text :x="m.x" y="156" text-anchor="middle" class="cf-year">{{ m.year }}</text>
      </g>

      <!-- Row 1 timeline -->
      <line x1="160" y1="135" x2="1175" y2="135" class="cf-track-line"/>
      <line x1="1140" y1="135" x2="1173" y2="135" class="cf-arrow-end" marker-end="url(#cf-ar)"/>

      <!-- Prove cards (below, 170 wide) -->
      <g v-for="m in row1Prove" :key="m.id" :class="['cf-node', `cf-era-${m.era}`]">
        <line :x1="m.x" y1="135" :x2="m.x" y2="168" class="cf-stub"/>
        <rect :x="m.x - 85" y="170" width="170" height="68" rx="9" class="cf-card-bg"/>
        <text :x="m.x" y="198" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="222" text-anchor="middle" class="cf-card-sub">{{ m.sub }}</text>
      </g>

      <!-- Continuation note (2024年以降も進化継続、詳細は配布資料へ) -->
      <g class="cf-continues">
        <rect x="150" y="255" width="900" height="34" rx="8" class="cf-continue-bg"/>
        <text x="600" y="277" text-anchor="middle" class="cf-continue-text">
          2024 年以降も BaseFold・HyperNova・LatticeFold+ 等で高速化が継続中。詳細は配布資料へ
        </text>
      </g>
    </svg>
  </div>
</template>

<style scoped>
.cf-root {
  position: relative;
  width: 100%;
  display: flex;
  flex-direction: column;
  font-family: 'Noto Sans JP', sans-serif;
  color: #111827;
}

.cf-svg {
  width: 100%;
  height: auto;
  display: block;
  font-family: 'Noto Sans JP', sans-serif;
}

/* Row headers */
.cf-row-header {
  font-size: 16px;
  font-weight: 800;
  fill: #475569;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.04em;
}

/* Side labels */
.cf-side-label {
  font-size: 13px;
  font-weight: 800;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.cf-side-commit { fill: #92400e; }
.cf-side-prove  { fill: #475569; }

/* Timelines */
.cf-track-line {
  stroke: #cbd5e1;
  stroke-width: 2.5;
  stroke-dasharray: 5 3;
}
.cf-arrow-end {
  stroke: #94a3b8;
  stroke-width: 2.5;
  fill: none;
}

/* Year markers */
.cf-year {
  font-size: 13px;
  fill: #94a3b8;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.04em;
}

/* Milestone cards */
.cf-stub {
  stroke: #94a3b8;
  stroke-width: 1.8;
}
.cf-card-bg {
  fill: white;
  stroke-width: 2.2;
  filter: drop-shadow(0 1px 3px rgba(0,0,0,0.07));
}
.cf-era-classic .cf-card-bg { fill: #f8fafc; stroke: #cbd5e1; }
.cf-era-hash    .cf-card-bg { fill: #fffbeb; stroke: #fcd34d; }
.cf-era-fold    .cf-card-bg { fill: #f8fafc; stroke: #cbd5e1; }
.cf-era-modern  .cf-card-bg { fill: #f8fafc; stroke: #cbd5e1; }
.cf-era-latest  .cf-card-bg {
  fill: #fffbeb;
  stroke: #d97706;
  stroke-width: 3;
  filter: drop-shadow(0 0 8px rgba(217, 119, 6, 0.4));
}

.cf-card-title {
  font-size: 18px;
  font-weight: 800;
  fill: #1f2937;
  font-family: 'Noto Sans JP', sans-serif;
}
.cf-card-sub {
  font-size: 13px;
  fill: #475569;
  font-weight: 600;
  font-family: 'JetBrains Mono', monospace;
}

.cf-era-latest .cf-card-title    { fill: #b45309; }

.cf-continue-bg {
  fill: #fffbeb;
  stroke: #fcd34d;
  stroke-width: 1.5;
}
.cf-continue-text {
  font-size: 14px;
  font-weight: 700;
  fill: #92400e;
  font-family: 'Noto Sans JP', sans-serif;
}
</style>
