<script setup lang="ts">
// 2-track timeline: commitment schemes + proving systems.
// Full evolution 2010 → 2025 with recent academic + production milestones.
type Track = 'commit' | 'prove'
type Era = 'classic' | 'hash' | 'fold' | 'modern' | 'latest'

type Milestone = {
  id: string;
  track: Track;
  year: string;
  x: number;
  label: string;
  sub: string;
  era: Era;
}

const milestones: Milestone[] = [
  // ===== Commitment track =====
  { id: 'kzg',       track: 'commit', year: '2010', x: 175, label: 'KZG',       sub: 'pairing / trusted setup',  era: 'classic' },
  { id: 'fri',       track: 'commit', year: '2017', x: 320, label: 'FRI',       sub: 'hash-based / RS',          era: 'hash'    },
  { id: 'brakedown', track: 'commit', year: '2023', x: 465, label: 'Brakedown', sub: 'linear-time / field-agnostic', era: 'hash' },
  { id: 'basefold',  track: 'commit', year: '2024', x: 610, label: 'BaseFold',  sub: 'multilinear FRI',          era: 'modern'  },
  { id: 'binius',    track: 'commit', year: '2024', x: 755, label: 'Binius',    sub: 'small-field (binary)',     era: 'modern'  },
  { id: 'whir',      track: 'commit', year: '2024', x: 900, label: 'WHIR',      sub: 'super-fast verifier',      era: 'modern'  },
  { id: 'fri-bin',   track: 'commit', year: '2025', x: 1045, label: 'FRI-Binius / FRIVail', sub: 'binary tower + DAS', era: 'latest' },

  // ===== Proving system track =====
  { id: 'groth16',   track: 'prove',  year: '2016', x: 170,  label: 'Groth16',     sub: 'pairing SNARK',            era: 'classic' },
  { id: 'stark',     track: 'prove',  year: '2018', x: 295,  label: 'STARK',       sub: 'hash-based / no setup',    era: 'hash'    },
  { id: 'plonk',     track: 'prove',  year: '2019', x: 420,  label: 'PLONK',       sub: 'universal SNARK',          era: 'hash'    },
  { id: 'halo2',     track: 'prove',  year: '2020', x: 545,  label: 'Halo2',       sub: 'accumulation / recursion', era: 'hash'    },
  { id: 'nova',      track: 'prove',  year: '2022', x: 670,  label: 'Nova',        sub: 'folding scheme (IVC)',     era: 'fold'    },
  { id: 'jolt',      track: 'prove',  year: '2024', x: 800,  label: 'Jolt',        sub: 'sumcheck + Lasso lookup',  era: 'modern'  },
  { id: 'neut',      track: 'prove',  year: '2024', x: 925,  label: 'NeutronNova / Mova', sub: 'folding ↓ overhead', era: 'modern' },
  { id: 'stwo',      track: 'prove',  year: '2025', x: 1050, label: 'Stwo / Circle STARK', sub: 'M31 prime field (Starknet prod)', era: 'latest' },
]

const commitTrack = milestones.filter(m => m.track === 'commit')
const proveTrack  = milestones.filter(m => m.track === 'prove')

// Latest column gets an extra emphasis (LatticeFold+ as post-quantum endpoint)
const extraLatest = [
  { track: 'prove', x: 1050, y: 360, label: 'LatticeFold+ (CRYPTO 2025) — post-quantum lattice folding' },
]
</script>

<template>
  <div class="cf-root">
    <!-- Caption -->
    <div class="cf-cap">
      <div class="cf-cap-title">commitment schemes と proving systems の 15 年</div>
      <div class="cf-cap-sub">pairing / trusted setup から ─ hash-based ─ folding ─ small-field / M31 / post-quantum まで</div>
    </div>

    <!-- Main SVG -->
    <svg class="cf-svg" viewBox="0 0 1200 380" preserveAspectRatio="xMidYMid meet">
      <defs>
        <marker id="cf-ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0,0 L 10,5 L 0,10 z" fill="#94a3b8"/>
        </marker>
      </defs>

      <!-- ============ Track 1: Commitment ============ -->
      <g class="cf-track-pill cf-track-pill-commit">
        <rect x="18" y="98" width="125" height="22" rx="11" fill="#fef3c7" stroke="#fcd34d" stroke-width="1.5"/>
        <text x="80" y="114" text-anchor="middle" class="cf-track-label">commitment</text>
      </g>

      <!-- Timeline 1 -->
      <line x1="150" y1="109" x2="1150" y2="109" class="cf-track-line"/>
      <line x1="1115" y1="109" x2="1148" y2="109" class="cf-arrow-end" marker-end="url(#cf-ar)"/>

      <!-- Commitment cards (above line) -->
      <g v-for="m in commitTrack" :key="m.id" :class="['cf-node', `cf-era-${m.era}`]">
        <line :x1="m.x" y1="109" :x2="m.x" y2="88" class="cf-stub"/>
        <rect :x="m.x - 68" y="14" width="136" height="72" rx="8" class="cf-card-bg"/>
        <text :x="m.x" y="38" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="58" text-anchor="middle" class="cf-card-sub">{{ m.sub }}</text>
        <text :x="m.x" y="76" text-anchor="middle" class="cf-card-year">{{ m.year }}</text>
      </g>

      <!-- Era boundary markers on timeline (subtle) -->
      <g class="cf-era-markers">
        <text x="240" y="135" text-anchor="middle" class="cf-era-tag">classic / pairing</text>
        <text x="540" y="135" text-anchor="middle" class="cf-era-tag">hash-based</text>
        <text x="900" y="135" text-anchor="middle" class="cf-era-tag">modern (2024+)</text>
      </g>

      <!-- ============ Track 2: Proving System ============ -->
      <g class="cf-track-pill cf-track-pill-prove">
        <rect x="18" y="225" width="125" height="22" rx="11" fill="#ede9fe" stroke="#c4b5fd" stroke-width="1.5"/>
        <text x="80" y="241" text-anchor="middle" class="cf-track-label cf-track-label-prove">proving system</text>
      </g>

      <!-- Timeline 2 -->
      <line x1="150" y1="236" x2="1150" y2="236" class="cf-track-line"/>
      <line x1="1115" y1="236" x2="1148" y2="236" class="cf-arrow-end" marker-end="url(#cf-ar)"/>

      <!-- Proving system cards (below line) -->
      <g v-for="m in proveTrack" :key="m.id" :class="['cf-node', `cf-era-${m.era}`]">
        <text :x="m.x" y="226" text-anchor="middle" class="cf-card-year">{{ m.year }}</text>
        <line :x1="m.x" y1="236" :x2="m.x" y2="257" class="cf-stub"/>
        <rect :x="m.x - 58" y="263" width="116" height="68" rx="8" class="cf-card-bg"/>
        <text :x="m.x" y="287" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="310" text-anchor="middle" class="cf-card-sub-small">{{ m.sub }}</text>
      </g>

      <!-- LatticeFold+ as additional latest highlight at bottom-right -->
      <g class="cf-extra-latest">
        <rect x="700" y="346" width="450" height="28" rx="6" fill="#ecfeff" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="3 2"/>
        <text x="925" y="364" text-anchor="middle" class="cf-extra-text">+ LatticeFold+ (CRYPTO 2025) — post-quantum lattice-based folding</text>
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
  gap: 8px;
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

/* Track labels */
.cf-track-label {
  font-size: 12px;
  font-weight: 800;
  fill: #78350f;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.04em;
}
.cf-track-label-prove { fill: #5b21b6; }

/* Track lines */
.cf-track-line {
  stroke: #cbd5e1;
  stroke-width: 2;
  stroke-dasharray: 4 3;
}
.cf-arrow-end {
  stroke: #94a3b8;
  stroke-width: 2;
  fill: none;
}

/* Era markers (between tracks) */
.cf-era-tag {
  font-size: 10px;
  font-weight: 700;
  fill: #94a3b8;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.06em;
}

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
/* era-based coloring */
.cf-era-classic .cf-card-bg { fill: #fef2f2; stroke: #f87171; }
.cf-era-hash    .cf-card-bg { fill: #f0fdf4; stroke: #86efac; }
.cf-era-fold    .cf-card-bg { fill: #f5f3ff; stroke: #c4b5fd; }
.cf-era-modern  .cf-card-bg { fill: #ecfeff; stroke: #67e8f9; }
.cf-era-latest  .cf-card-bg {
  fill: #fff7ed;
  stroke: #fb923c;
  stroke-width: 2.5;
  filter: drop-shadow(0 0 6px rgba(251, 146, 60, 0.4));
}

.cf-card-title {
  font-size: 14px;
  font-weight: 800;
  fill: #1f2937;
  font-family: 'BIZ UDPMincho', serif;
}
.cf-card-sub {
  font-size: 11px;
  fill: #475569;
  font-weight: 600;
  font-family: 'JetBrains Mono', monospace;
}
.cf-card-sub-small {
  font-size: 10px;
  fill: #475569;
  font-weight: 600;
  font-family: 'JetBrains Mono', monospace;
}
.cf-card-year {
  font-size: 11px;
  fill: #94a3b8;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.04em;
}

/* Latest highlights stand out */
.cf-era-latest .cf-card-title { fill: #c2410c; }
.cf-era-latest .cf-card-year  { fill: #ea580c; font-weight: 800; }

/* Extra latest banner */
.cf-extra-text {
  font-size: 12px;
  font-weight: 700;
  fill: #155e75;
  font-family: 'JetBrains Mono', monospace;
}
</style>
