<script setup lang="ts">
// 2-track timeline: commitment schemes + proving systems.
// Latest milestones from 2024-2025 academic publications and zkVM usage.
type Track = 'commit' | 'prove'
type ColorType = 'classic' | 'hash' | 'modern'

type Milestone = {
  id: string;
  track: Track;
  year: string;
  x: number;
  label: string;
  sub: string;
  type: ColorType;
}

const milestones: Milestone[] = [
  // ===== Commitment track =====
  { id: 'kzg',       track: 'commit', year: '2010', x: 175, label: 'KZG',        sub: 'pairing / trusted setup', type: 'classic' },
  { id: 'fri',       track: 'commit', year: '2017', x: 340, label: 'FRI',        sub: 'hash-based',              type: 'hash'    },
  { id: 'brakedown', track: 'commit', year: '2023', x: 505, label: 'Brakedown',  sub: 'linear-time',             type: 'hash'    },
  { id: 'basefold',  track: 'commit', year: '2024', x: 670, label: 'BaseFold',   sub: 'multilinear / field-agnostic', type: 'modern' },
  { id: 'binius',    track: 'commit', year: '2024', x: 835, label: 'Binius',     sub: 'small-field (binary)',    type: 'modern'  },
  { id: 'whir',      track: 'commit', year: '2024', x: 1000, label: 'WHIR',      sub: 'fast verifier (RS prox.)', type: 'modern' },

  // ===== Proving system track =====
  { id: 'groth16',   track: 'prove',  year: '2016', x: 175, label: 'Groth16',     sub: 'pairing SNARK',          type: 'classic' },
  { id: 'stark',     track: 'prove',  year: '2018', x: 340, label: 'STARK',       sub: 'hash-based, no setup',   type: 'hash'    },
  { id: 'plonk',     track: 'prove',  year: '2019', x: 470, label: 'PLONK',       sub: 'universal SNARK',        type: 'hash'    },
  { id: 'halo2',     track: 'prove',  year: '2020', x: 600, label: 'Halo2',       sub: 'accumulation / recursion', type: 'hash'  },
  { id: 'nova',      track: 'prove',  year: '2022', x: 730, label: 'Nova',        sub: 'folding scheme (IVC)',   type: 'hash'    },
  { id: 'jolt',      track: 'prove',  year: '2024', x: 870, label: 'Jolt',        sub: 'sumcheck + Lasso lookups', type: 'modern' },
  { id: 'hypernova', track: 'prove',  year: '2024', x: 1020, label: 'HyperNova',  sub: '+ ProtoStar / CycleFold', type: 'modern' },
]

const commitTrack = milestones.filter(m => m.track === 'commit')
const proveTrack  = milestones.filter(m => m.track === 'prove')

// zkVMs and what they combine (current state)
const zkvms = [
  { name: 'Jolt',  recipe: 'Sumcheck + Lasso',     extra: '(+ Binius / Zeromorph)',  hue: 'amber'  },
  { name: 'SP1',   recipe: 'Plonky3 + FRI',        extra: 'Succinct Labs',           hue: 'green'  },
  { name: 'RISC0', recipe: 'STARK + FRI',          extra: 'RISC Zero',               hue: 'blue'   },
  { name: 'Nexus', recipe: 'HyperNova + CycleFold', extra: 'Nexus Labs',             hue: 'purple' },
]
</script>

<template>
  <div class="cf-root">
    <!-- Caption -->
    <div class="cf-cap">
      <div class="cf-cap-title">commitment schemes と proving systems の進化</div>
      <div class="cf-cap-sub">10 年で pairing/setup-heavy → hash-based, sumcheck-based, small-field へ ─ 現代 zkVM はこれらの組み合わせ</div>
    </div>

    <!-- Main SVG: 2 timelines + zkVM strip -->
    <svg class="cf-svg" viewBox="0 0 1200 420" preserveAspectRatio="xMidYMid meet">
      <defs>
        <marker id="cf-ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0,0 L 10,5 L 0,10 z" fill="#94a3b8"/>
        </marker>
      </defs>

      <!-- Track 1 label: commitment -->
      <g class="cf-track-pill cf-track-pill-commit">
        <rect x="18" y="78" width="120" height="22" rx="11" fill="#fef3c7" stroke="#fcd34d" stroke-width="1.5"/>
        <text x="78" y="94" text-anchor="middle" class="cf-track-label">commitment</text>
      </g>

      <!-- Timeline 1 -->
      <line x1="150" y1="89" x2="1150" y2="89" class="cf-track-line"/>
      <line x1="1110" y1="89" x2="1145" y2="89" class="cf-arrow-end" marker-end="url(#cf-ar)"/>

      <!-- Commitment cards (above line) -->
      <g v-for="m in commitTrack" :key="m.id" :class="['cf-node', `cf-type-${m.type}`]">
        <line :x1="m.x" y1="89" :x2="m.x" y2="68" class="cf-stub"/>
        <rect :x="m.x - 72" y="14" width="144" height="54" rx="8" class="cf-card-bg"/>
        <text :x="m.x" y="36" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="55" text-anchor="middle" class="cf-card-sub">{{ m.sub }}</text>
        <text :x="m.x" y="110" text-anchor="middle" class="cf-year">{{ m.year }}</text>
      </g>

      <!-- Track 2 label: proving system -->
      <g class="cf-track-pill cf-track-pill-prove">
        <rect x="18" y="195" width="120" height="22" rx="11" fill="#ede9fe" stroke="#c4b5fd" stroke-width="1.5"/>
        <text x="78" y="211" text-anchor="middle" class="cf-track-label cf-track-label-prove">proving system</text>
      </g>

      <!-- Timeline 2 -->
      <line x1="150" y1="206" x2="1150" y2="206" class="cf-track-line"/>
      <line x1="1110" y1="206" x2="1145" y2="206" class="cf-arrow-end" marker-end="url(#cf-ar)"/>

      <!-- Proving system cards (below line) -->
      <g v-for="m in proveTrack" :key="m.id" :class="['cf-node', `cf-type-${m.type}`]">
        <text :x="m.x" y="195" text-anchor="middle" class="cf-year">{{ m.year }}</text>
        <line :x1="m.x" y1="206" :x2="m.x" y2="227" class="cf-stub"/>
        <rect :x="m.x - 65" y="232" width="130" height="54" rx="8" class="cf-card-bg"/>
        <text :x="m.x" y="254" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="273" text-anchor="middle" class="cf-card-sub">{{ m.sub }}</text>
      </g>

      <!-- zkVM combinations strip (bottom) -->
      <text x="78" y="320" class="cf-zkvm-label">現代 zkVMs ＝ 組み合わせ</text>

      <g v-for="(v, i) in zkvms" :key="v.name" :class="['cf-zkvm', `cf-zkvm-${v.hue}`]">
        <rect :x="170 + i * 250" y="332" width="230" height="74" rx="8" class="cf-zkvm-bg"/>
        <text :x="170 + i * 250 + 18" y="357" class="cf-zkvm-name">{{ v.name }}</text>
        <text :x="170 + i * 250 + 18" y="378" class="cf-zkvm-recipe">= {{ v.recipe }}</text>
        <text :x="170 + i * 250 + 18" y="395" class="cf-zkvm-extra">{{ v.extra }}</text>
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
/* color by type/era */
.cf-type-classic .cf-card-bg { fill: #fef2f2; stroke: #f87171; }
.cf-type-hash    .cf-card-bg { fill: #f0fdf4; stroke: #86efac; }
.cf-type-modern  .cf-card-bg { fill: #ecfeff; stroke: #67e8f9; }

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

.cf-year {
  font-size: 11px;
  fill: #94a3b8;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.04em;
}

/* zkVM strip */
.cf-zkvm-label {
  font-size: 13px;
  font-weight: 800;
  fill: #4338ca;
  font-family: 'BIZ UDPMincho', serif;
}
.cf-zkvm-bg {
  fill: white;
  stroke-width: 2;
  filter: drop-shadow(0 2px 5px rgba(0,0,0,0.06));
}
.cf-zkvm-amber  .cf-zkvm-bg { fill: #fffbeb; stroke: #fcd34d; }
.cf-zkvm-green  .cf-zkvm-bg { fill: #f0fdf4; stroke: #86efac; }
.cf-zkvm-blue   .cf-zkvm-bg { fill: #eff6ff; stroke: #93c5fd; }
.cf-zkvm-purple .cf-zkvm-bg { fill: #f5f3ff; stroke: #c4b5fd; }

.cf-zkvm-name {
  font-size: 18px;
  font-weight: 900;
  fill: #1f2937;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.02em;
}
.cf-zkvm-amber  .cf-zkvm-name { fill: #b45309; }
.cf-zkvm-green  .cf-zkvm-name { fill: #047857; }
.cf-zkvm-blue   .cf-zkvm-name { fill: #1d4ed8; }
.cf-zkvm-purple .cf-zkvm-name { fill: #6d28d9; }

.cf-zkvm-recipe {
  font-size: 12.5px;
  font-weight: 700;
  fill: #1f2937;
  font-family: 'JetBrains Mono', monospace;
}
.cf-zkvm-extra {
  font-size: 11px;
  fill: #6b7280;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 600;
  font-style: italic;
}
</style>
