<script setup lang="ts">
// 時間軸 2 段構成:
//   Row 1 (2010-2023 歴史):    上 = commitment / 下 = proving system
//   Row 2 (2024-2026 最新):    上 = commitment / 下 = proving system (zoom)
// 全ての milestone が研究単位の個別ブロック。
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

// ===== Row 1: 2010-2023 歴史 (compressed) =====
const row1: Milestone[] = [
  // commitment (above)
  { id: 'kzg',       side: 'commit', year: '2010', x: 230,  label: 'KZG',        sub: 'pairing / setup',  era: 'classic' },
  { id: 'fri',       side: 'commit', year: '2017', x: 540,  label: 'FRI',        sub: 'hash-based',       era: 'hash'    },
  { id: 'brakedown', side: 'commit', year: '2023', x: 980,  label: 'Brakedown',  sub: 'linear-time',      era: 'hash'    },
  // proving (below)
  { id: 'groth16',   side: 'prove',  year: '2016', x: 220,  label: 'Groth16',    sub: 'pairing SNARK',    era: 'classic' },
  { id: 'stark',     side: 'prove',  year: '2018', x: 410,  label: 'STARK',      sub: 'hash-based',       era: 'hash'    },
  { id: 'plonk',     side: 'prove',  year: '2019', x: 580,  label: 'PLONK',      sub: 'universal',        era: 'hash'    },
  { id: 'halo2',     side: 'prove',  year: '2020', x: 750,  label: 'Halo2',      sub: 'accumulation',     era: 'hash'    },
  { id: 'nova',      side: 'prove',  year: '2022', x: 950,  label: 'Nova',       sub: 'folding / IVC',    era: 'fold'    },
]
const row1Commit = row1.filter(m => m.side === 'commit')
const row1Prove  = row1.filter(m => m.side === 'prove')

// ===== Row 2: 2024-2026 最新 (zoomed, per-research blocks) =====
const row2: Milestone[] = [
  // commitment (above)
  { id: 'basefold',  side: 'commit', year: '2024', x: 180,  label: 'BaseFold',   sub: 'multilinear FRI',     era: 'modern' },
  { id: 'binius',    side: 'commit', year: '2024', x: 335,  label: 'Binius',     sub: 'small-field (binary)',era: 'modern' },
  { id: 'whir',      side: 'commit', year: '2024', x: 490,  label: 'WHIR',       sub: 'fast verifier',       era: 'modern' },
  { id: 'fribin',    side: 'commit', year: '2024', x: 645,  label: 'FRI-Binius', sub: 'combo (binary)',      era: 'modern' },
  { id: 'frivail',   side: 'commit', year: '2025', x: 800,  label: 'FRIVail',    sub: 'DAS application',     era: 'latest' },
  { id: 'longfellow',side: 'commit', year: '2024', x: 970,  label: 'Longfellow / Ligero', sub: 'client-side / MPC-in-the-head', era: 'modern' },
  // proving (below)
  { id: 'hypernova', side: 'prove',  year: '2023', x: 180,  label: 'HyperNova',  sub: 'multi-folding',       era: 'fold'   },
  { id: 'protostar', side: 'prove',  year: '2023', x: 320,  label: 'ProtoStar',  sub: 'generic folding',     era: 'fold'   },
  { id: 'cyclefold', side: 'prove',  year: '2024', x: 460,  label: 'CycleFold',  sub: 'cycle of curves',     era: 'modern' },
  { id: 'jolt',      side: 'prove',  year: '2024', x: 600,  label: 'Jolt',       sub: 'sumcheck + Lasso',    era: 'modern' },
  { id: 'neut',      side: 'prove',  year: '2024', x: 740,  label: 'NeutronNova',sub: 'zero-check folding',  era: 'modern' },
  { id: 'mova',      side: 'prove',  year: '2024', x: 870,  label: 'Mova',       sub: 'no error commit',     era: 'modern' },
  { id: 'stwo',      side: 'prove',  year: '2025', x: 1000, label: 'Stwo',       sub: 'Circle STARK / M31',  era: 'latest' },
  { id: 'latfold',   side: 'prove',  year: '2025', x: 1130, label: 'LatticeFold+', sub: 'post-quantum',      era: 'latest' },
]
const row2Commit = row2.filter(m => m.side === 'commit')
const row2Prove  = row2.filter(m => m.side === 'prove')
</script>

<template>
  <div class="cf-root">
    <!-- Caption -->
    <div class="cf-cap">
      <div class="cf-cap-title">commitment × proving system  ─  時間軸 2 段</div>
      <div class="cf-cap-sub">上段: 2010-2023 歴史 ／ 下段: 2024-2026 最新研究 (zoom) ─ 各段の x 軸の上 = commitment、下 = proving system</div>
    </div>

    <!-- Main SVG: 2 stacked time-axis rows -->
    <svg class="cf-svg" viewBox="0 0 1200 410" preserveAspectRatio="xMidYMid meet">
      <defs>
        <marker id="cf-ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0,0 L 10,5 L 0,10 z" fill="#94a3b8"/>
        </marker>
      </defs>

      <!-- =========================================================
           ROW 1: 2010-2023 歴史
           ========================================================= -->
      <text x="30" y="20" class="cf-row-header">▸ 2010 → 2023  歴史</text>

      <text x="40" y="65" class="cf-side-label cf-side-commit">commitment</text>
      <text x="40" y="160" class="cf-side-label cf-side-prove">proving system</text>

      <!-- Commit cards (above) -->
      <g v-for="m in row1Commit" :key="m.id" :class="['cf-node', `cf-era-${m.era}`]">
        <line :x1="m.x" y1="100" :x2="m.x" y2="80" class="cf-stub"/>
        <rect :x="m.x - 70" y="28" width="140" height="52" rx="7" class="cf-card-bg"/>
        <text :x="m.x" y="48" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="64" text-anchor="middle" class="cf-card-sub">{{ m.sub }}</text>
        <text :x="m.x" y="118" text-anchor="middle" class="cf-year">{{ m.year }}</text>
      </g>

      <!-- Row 1 timeline -->
      <line x1="150" y1="100" x2="1150" y2="100" class="cf-track-line"/>
      <line x1="1115" y1="100" x2="1148" y2="100" class="cf-arrow-end" marker-end="url(#cf-ar)"/>

      <!-- Prove cards (below) -->
      <g v-for="m in row1Prove" :key="m.id" :class="['cf-node', `cf-era-${m.era}`]">
        <line :x1="m.x" y1="100" :x2="m.x" y2="125" class="cf-stub"/>
        <rect :x="m.x - 60" y="130" width="120" height="52" rx="7" class="cf-card-bg"/>
        <text :x="m.x" y="150" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="166" text-anchor="middle" class="cf-card-sub-sm">{{ m.sub }}</text>
      </g>

      <!-- Separator between rows -->
      <line x1="0" y1="200" x2="1200" y2="200" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="3 3"/>

      <!-- =========================================================
           ROW 2: 2024-2026 最新 (zoomed, per-research blocks)
           ========================================================= -->
      <text x="30" y="218" class="cf-row-header cf-row-header-latest">▸ 2024 → 2026  最新研究</text>

      <text x="40" y="263" class="cf-side-label cf-side-commit">commitment</text>
      <text x="40" y="365" class="cf-side-label cf-side-prove">proving system</text>

      <!-- Commit cards (above) -->
      <g v-for="m in row2Commit" :key="m.id" :class="['cf-node', `cf-era-${m.era}`]">
        <line :x1="m.x" y1="305" :x2="m.x" y2="285" class="cf-stub"/>
        <rect :x="m.x - 70" y="232" width="140" height="52" rx="7" class="cf-card-bg"/>
        <text :x="m.x" y="252" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="268" text-anchor="middle" class="cf-card-sub-sm">{{ m.sub }}</text>
        <text :x="m.x" y="323" text-anchor="middle" class="cf-year cf-year-latest">{{ m.year }}</text>
      </g>

      <!-- Row 2 timeline (zoomed 2024-2026) -->
      <line x1="150" y1="305" x2="1180" y2="305" class="cf-track-line cf-track-line-latest"/>
      <line x1="1145" y1="305" x2="1178" y2="305" class="cf-arrow-end cf-arrow-end-latest" marker-end="url(#cf-ar)"/>

      <!-- Prove cards (below) -->
      <g v-for="m in row2Prove" :key="m.id" :class="['cf-node', `cf-era-${m.era}`]">
        <line :x1="m.x" y1="305" :x2="m.x" y2="335" class="cf-stub"/>
        <rect :x="m.x - 56" y="338" width="112" height="52" rx="7" class="cf-card-bg"/>
        <text :x="m.x" y="358" text-anchor="middle" class="cf-card-title-sm">{{ m.label }}</text>
        <text :x="m.x" y="374" text-anchor="middle" class="cf-card-sub-xs">{{ m.sub }}</text>
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
  gap: 6px;
  font-family: 'Noto Sans JP', sans-serif;
  color: #111827;
}

.cf-cap {
  padding: 9px 16px;
  background: #eef2ff;
  border: 1px solid #c7d2fe;
  border-radius: 0.5rem;
  display: flex;
  flex-direction: column;
  gap: 3px;
}
.cf-cap-title {
  font-size: 16px;
  font-weight: 800;
  color: #1e1b4b;
  font-family: 'BIZ UDPMincho', serif;
}
.cf-cap-sub {
  font-size: 13px;
  color: #4338ca;
  font-weight: 600;
  font-family: 'BIZ UDPMincho', serif;
}

.cf-svg {
  width: 100%;
  height: auto;
  display: block;
  font-family: 'Noto Sans JP', sans-serif;
}

/* Row headers */
.cf-row-header {
  font-size: 13px;
  font-weight: 800;
  fill: #475569;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.04em;
}
.cf-row-header-latest { fill: #c2410c; }

/* Side labels */
.cf-side-label {
  font-size: 11px;
  font-weight: 800;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.cf-side-commit { fill: #92400e; }
.cf-side-prove  { fill: #5b21b6; }

/* Timelines */
.cf-track-line {
  stroke: #cbd5e1;
  stroke-width: 2;
  stroke-dasharray: 4 3;
}
.cf-track-line-latest {
  stroke: #fb923c;
  stroke-width: 2.5;
}
.cf-arrow-end {
  stroke: #94a3b8;
  stroke-width: 2;
  fill: none;
}
.cf-arrow-end-latest { stroke: #fb923c; stroke-width: 2.5; }

.cf-year {
  font-size: 10px;
  fill: #94a3b8;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.04em;
}
.cf-year-latest { fill: #c2410c; font-weight: 800; }

/* Milestone cards */
.cf-stub {
  stroke: #94a3b8;
  stroke-width: 1.5;
}
.cf-card-bg {
  fill: white;
  stroke-width: 2;
  filter: drop-shadow(0 1px 3px rgba(0,0,0,0.06));
}
.cf-era-classic .cf-card-bg { fill: #fef2f2; stroke: #f87171; }
.cf-era-hash    .cf-card-bg { fill: #f0fdf4; stroke: #86efac; }
.cf-era-fold    .cf-card-bg { fill: #f5f3ff; stroke: #c4b5fd; }
.cf-era-modern  .cf-card-bg { fill: #ecfeff; stroke: #67e8f9; }
.cf-era-latest  .cf-card-bg {
  fill: #fff7ed;
  stroke: #fb923c;
  stroke-width: 2.5;
  filter: drop-shadow(0 0 6px rgba(251, 146, 60, 0.45));
}

.cf-card-title {
  font-size: 13.5px;
  font-weight: 800;
  fill: #1f2937;
  font-family: 'BIZ UDPMincho', serif;
}
.cf-card-title-sm {
  font-size: 12px;
  font-weight: 800;
  fill: #1f2937;
  font-family: 'BIZ UDPMincho', serif;
}
.cf-card-sub {
  font-size: 10.5px;
  fill: #475569;
  font-weight: 600;
  font-family: 'JetBrains Mono', monospace;
}
.cf-card-sub-sm {
  font-size: 10px;
  fill: #475569;
  font-weight: 600;
  font-family: 'JetBrains Mono', monospace;
}
.cf-card-sub-xs {
  font-size: 9.5px;
  fill: #475569;
  font-weight: 600;
  font-family: 'JetBrains Mono', monospace;
}

.cf-era-latest .cf-card-title    { fill: #c2410c; }
.cf-era-latest .cf-card-title-sm { fill: #c2410c; }
</style>
