<script setup lang="ts">
// 時間軸 2 段構成:
//  Row 1 (2010-2024 歴史):   上 = commitment / 下 = proving system
//  Row 2 (2025-2026 最新):  上 = commitment side trends / 下 = proving side trends
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

// ===== Row 1: 2010-2024 歴史 =====
const row1: Milestone[] = [
  // commitment side (above timeline)
  { id: 'kzg',       side: 'commit', year: '2010', x: 200,  label: 'KZG',        sub: 'pairing / setup',  era: 'classic' },
  { id: 'fri',       side: 'commit', year: '2017', x: 360,  label: 'FRI',        sub: 'hash-based',       era: 'hash' },
  { id: 'brakedown', side: 'commit', year: '2023', x: 520,  label: 'Brakedown',  sub: 'linear-time',      era: 'hash' },
  { id: 'basefold',  side: 'commit', year: '2024', x: 680,  label: 'BaseFold',   sub: 'multilinear FRI',  era: 'modern' },
  { id: 'binius',    side: 'commit', year: '2024', x: 840,  label: 'Binius',     sub: 'small-field',      era: 'modern' },
  { id: 'whir',      side: 'commit', year: '2024', x: 1000, label: 'WHIR',       sub: 'fast verifier',    era: 'modern' },

  // proving side (below timeline)
  { id: 'groth16',   side: 'prove',  year: '2016', x: 200,  label: 'Groth16',    sub: 'pairing SNARK',    era: 'classic' },
  { id: 'stark',     side: 'prove',  year: '2018', x: 335,  label: 'STARK',      sub: 'hash-based',       era: 'hash' },
  { id: 'plonk',     side: 'prove',  year: '2019', x: 470,  label: 'PLONK',      sub: 'universal',        era: 'hash' },
  { id: 'halo2',     side: 'prove',  year: '2020', x: 605,  label: 'Halo2',      sub: 'accumulation',     era: 'hash' },
  { id: 'nova',      side: 'prove',  year: '2022', x: 740,  label: 'Nova',       sub: 'folding / IVC',    era: 'fold' },
  { id: 'jolt',      side: 'prove',  year: '2024', x: 870,  label: 'Jolt',       sub: 'sumcheck+Lasso',   era: 'modern' },
  { id: 'neut',      side: 'prove',  year: '2024', x: 1000, label: 'NeutronNova',sub: 'Mova ↓ overhead',  era: 'modern' },
]

const row1Commit = row1.filter(m => m.side === 'commit')
const row1Prove  = row1.filter(m => m.side === 'prove')

// ===== Row 2: 2025-2026 最新トレンド =====
type Trend = {
  side: Side;
  x: number;
  width: number;
  title: string;
  examples: string;
  note: string;
  hue: 'cyan' | 'amber' | 'purple' | 'green';
}

const row2: Trend[] = [
  // commitment side (above timeline)
  { side: 'commit', x: 200,  width: 380, title: 'small-field / 2 進 tower',
    examples: 'Binius / FRI-Binius / FRIVail',
    note: '32-bit 以下の小 field で乗算高速化', hue: 'cyan' },
  { side: 'commit', x: 620,  width: 420, title: 'client-side proving (commitment 側)',
    examples: 'Longfellow / Ligero MPC-in-the-head',
    note: 'mobile / wallet で軽量 prover', hue: 'amber' },

  // proving side (below timeline)
  { side: 'prove',  x: 200,  width: 380, title: 'Production STARK',
    examples: 'Stwo / Circle STARK (Starknet mainnet)',
    note: 'M31 prime field、Stwo が 125× 速い (2025)', hue: 'purple' },
  { side: 'prove',  x: 620,  width: 420, title: 'post-quantum folding',
    examples: 'LatticeFold+ (CRYPTO 2025) / LatticeFold',
    note: 'lattice ベース、量子耐性 IVC', hue: 'green' },
]

const row2Commit = row2.filter(t => t.side === 'commit')
const row2Prove  = row2.filter(t => t.side === 'prove')
</script>

<template>
  <div class="cf-root">
    <!-- Caption -->
    <div class="cf-cap">
      <div class="cf-cap-title">commitment × proving system  ─  時間軸 2 段</div>
      <div class="cf-cap-sub">上段は 2010-2024 の系譜、下段は 2025-2026 最新トレンド ─ 各段の x 軸の上 = commitment、下 = proving system</div>
    </div>

    <!-- Main SVG: 2 stacked rows -->
    <svg class="cf-svg" viewBox="0 0 1200 410" preserveAspectRatio="xMidYMid meet">
      <defs>
        <marker id="cf-ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0,0 L 10,5 L 0,10 z" fill="#94a3b8"/>
        </marker>
      </defs>

      <!-- =====================================================
           ROW 1: 2010-2024 歴史
           ===================================================== -->
      <text x="30" y="20" class="cf-row-header">▸ 2010 → 2024  歴史</text>

      <!-- Side labels (top: commitment, bottom: proving) -->
      <text x="30" y="65" class="cf-side-label cf-side-commit">commitment</text>
      <text x="30" y="160" class="cf-side-label cf-side-prove">proving system</text>

      <!-- Commit cards (above timeline) -->
      <g v-for="m in row1Commit" :key="m.id" :class="['cf-node', `cf-era-${m.era}`]">
        <line :x1="m.x" y1="100" :x2="m.x" y2="80" class="cf-stub"/>
        <rect :x="m.x - 65" y="28" width="130" height="52" rx="7" class="cf-card-bg"/>
        <text :x="m.x" y="48" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="64" text-anchor="middle" class="cf-card-sub">{{ m.sub }}</text>
      </g>

      <!-- Row 1 timeline -->
      <line x1="150" y1="100" x2="1150" y2="100" class="cf-track-line"/>
      <line x1="1115" y1="100" x2="1148" y2="100" class="cf-arrow-end" marker-end="url(#cf-ar)"/>

      <!-- Year markers on timeline -->
      <g class="cf-years">
        <text x="200" y="118" text-anchor="middle" class="cf-year">2010</text>
        <text x="360" y="118" text-anchor="middle" class="cf-year">2017</text>
        <text x="520" y="118" text-anchor="middle" class="cf-year">2023</text>
        <text x="840" y="118" text-anchor="middle" class="cf-year">2024</text>
      </g>

      <!-- Prove cards (below timeline) -->
      <g v-for="m in row1Prove" :key="m.id" :class="['cf-node', `cf-era-${m.era}`]">
        <line :x1="m.x" y1="100" :x2="m.x" y2="120" class="cf-stub"/>
        <rect :x="m.x - 60" y="125" width="120" height="52" rx="7" class="cf-card-bg"/>
        <text :x="m.x" y="145" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="161" text-anchor="middle" class="cf-card-sub-sm">{{ m.sub }}</text>
      </g>

      <!-- Separator between rows -->
      <line x1="0" y1="200" x2="1200" y2="200" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="3 3"/>

      <!-- =====================================================
           ROW 2: 2025-2026 最新トレンド (zoomed)
           ===================================================== -->
      <text x="30" y="218" class="cf-row-header cf-row-header-latest">▸ 2025 → 2026  最新トレンド</text>

      <text x="30" y="263" class="cf-side-label cf-side-commit">commitment</text>
      <text x="30" y="360" class="cf-side-label cf-side-prove">proving system</text>

      <!-- Commit side trends (above timeline) -->
      <g v-for="t in row2Commit" :key="t.title" :class="['cf-trend', `cf-trend-${t.hue}`]">
        <line :x1="t.x + t.width / 2" y1="290" :x2="t.x + t.width / 2" y2="280" class="cf-stub"/>
        <rect :x="t.x" y="232" :width="t.width" height="50" rx="8" class="cf-trend-bg"/>
        <text :x="t.x + 18" y="251" class="cf-trend-title">▶ {{ t.title }}</text>
        <text :x="t.x + 18" y="270" class="cf-trend-examples">{{ t.examples }}</text>
        <text :x="t.x + t.width - 12" y="278" text-anchor="end" class="cf-trend-note">{{ t.note }}</text>
      </g>

      <!-- Row 2 timeline (zoomed 2025-2026) -->
      <line x1="150" y1="290" x2="1150" y2="290" class="cf-track-line cf-track-line-latest"/>
      <line x1="1115" y1="290" x2="1148" y2="290" class="cf-arrow-end cf-arrow-end-latest" marker-end="url(#cf-ar)"/>

      <!-- Year markers -->
      <g class="cf-years">
        <text x="200" y="308" text-anchor="middle" class="cf-year cf-year-latest">2025</text>
        <text x="1050" y="308" text-anchor="middle" class="cf-year cf-year-latest">2026</text>
      </g>

      <!-- Prove side trends (below timeline) -->
      <g v-for="t in row2Prove" :key="t.title" :class="['cf-trend', `cf-trend-${t.hue}`]">
        <line :x1="t.x + t.width / 2" y1="290" :x2="t.x + t.width / 2" y2="318" class="cf-stub"/>
        <rect :x="t.x" y="320" :width="t.width" height="50" rx="8" class="cf-trend-bg"/>
        <text :x="t.x + 18" y="339" class="cf-trend-title">▶ {{ t.title }}</text>
        <text :x="t.x + 18" y="358" class="cf-trend-examples">{{ t.examples }}</text>
        <text :x="t.x + t.width - 12" y="366" text-anchor="end" class="cf-trend-note">{{ t.note }}</text>
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

/* Side labels (commitment vs proving system) */
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
  font-size: 11px;
  fill: #94a3b8;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.04em;
}
.cf-year-latest { fill: #c2410c; font-weight: 800; }

/* Row 1 milestone cards */
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

.cf-card-title {
  font-size: 14px;
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

/* Row 2 trend cards */
.cf-trend-bg {
  fill: white;
  stroke-width: 2;
  filter: drop-shadow(0 2px 5px rgba(0,0,0,0.07));
}
.cf-trend-cyan   .cf-trend-bg { fill: #ecfeff; stroke: #06b6d4; }
.cf-trend-amber  .cf-trend-bg { fill: #fffbeb; stroke: #d97706; }
.cf-trend-purple .cf-trend-bg { fill: #f5f3ff; stroke: #8b5cf6; }
.cf-trend-green  .cf-trend-bg { fill: #f0fdf4; stroke: #10b981; }

.cf-trend-title {
  font-size: 13px;
  font-weight: 800;
  fill: #1f2937;
  font-family: 'BIZ UDPMincho', serif;
}
.cf-trend-cyan   .cf-trend-title { fill: #155e75; }
.cf-trend-amber  .cf-trend-title { fill: #92400e; }
.cf-trend-purple .cf-trend-title { fill: #5b21b6; }
.cf-trend-green  .cf-trend-title { fill: #065f46; }

.cf-trend-examples {
  font-size: 12px;
  font-weight: 700;
  fill: #1f2937;
  font-family: 'JetBrains Mono', monospace;
}
.cf-trend-note {
  font-size: 10.5px;
  fill: #4b5563;
  font-family: 'BIZ UDPMincho', serif;
  font-weight: 600;
  font-style: italic;
}
</style>
