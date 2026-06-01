<script setup lang="ts">
// 2 タイムライン + 「2025 最新トレンド」ストリップ
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
  // ===== Commitment track (7 cards, spacing 145) =====
  { id: 'kzg',       track: 'commit', year: '2010', x: 175,  label: 'KZG',        sub: 'pairing / trusted setup', era: 'classic' },
  { id: 'fri',       track: 'commit', year: '2017', x: 320,  label: 'FRI',        sub: 'hash-based / RS',         era: 'hash'    },
  { id: 'brakedown', track: 'commit', year: '2023', x: 465,  label: 'Brakedown',  sub: 'linear-time prover',      era: 'hash'    },
  { id: 'basefold',  track: 'commit', year: '2024', x: 610,  label: 'BaseFold',   sub: 'multilinear / FA',        era: 'modern'  },
  { id: 'binius',    track: 'commit', year: '2024', x: 755,  label: 'Binius',     sub: 'small-field (binary)',    era: 'modern'  },
  { id: 'whir',      track: 'commit', year: '2024', x: 900,  label: 'WHIR',      sub: 'fast verifier',           era: 'modern'  },
  { id: 'fri-bin',   track: 'commit', year: '2025', x: 1045, label: 'FRI-Binius', sub: 'binary tower (combo)',    era: 'latest'  },

  // ===== Proving system track (7 cards, spacing 145) =====
  { id: 'groth16',   track: 'prove',  year: '2016', x: 175,  label: 'Groth16',    sub: 'pairing SNARK',          era: 'classic' },
  { id: 'starkplonk',track: 'prove',  year: '18-19',x: 320,  label: 'STARK / PLONK', sub: 'hash / universal',    era: 'hash'    },
  { id: 'halo2',     track: 'prove',  year: '2020', x: 465,  label: 'Halo2',      sub: 'accumulation',           era: 'hash'    },
  { id: 'nova',      track: 'prove',  year: '2022', x: 610,  label: 'Nova',       sub: 'folding scheme (IVC)',   era: 'fold'    },
  { id: 'jolt',      track: 'prove',  year: '2024', x: 755,  label: 'Jolt',       sub: 'sumcheck + Lasso',       era: 'modern'  },
  { id: 'neut',      track: 'prove',  year: '2024', x: 900,  label: 'NeutronNova',sub: 'Mova / 軽量 folding',    era: 'modern'  },
  { id: 'stwo',      track: 'prove',  year: '2025', x: 1045, label: 'Stwo',       sub: 'Circle STARK / M31',     era: 'latest'  },
]

const commitTrack = milestones.filter(m => m.track === 'commit')
const proveTrack  = milestones.filter(m => m.track === 'prove')

// 2024-2025 latest trends (categorical)
const trends = [
  {
    title: 'small-field / 2 進 tower',
    detail: 'Binius / FRI-Binius / FRIVail',
    note: '32-bit 以下の小さい field で乗算を高速化',
    hue: 'cyan',
  },
  {
    title: 'client-side proving',
    detail: 'Longfellow / MPC-in-the-head 系',
    note: 'mobile で証明生成 (Ligero 系列の高速化)',
    hue: 'amber',
  },
  {
    title: 'Production STARK',
    detail: 'Stwo / Circle STARK',
    note: 'M31 prime field + Starknet mainnet 稼働 (2025)',
    hue: 'purple',
  },
  {
    title: 'post-quantum folding',
    detail: 'LatticeFold+ (CRYPTO 2025)',
    note: 'lattice ベース、量子耐性 IVC',
    hue: 'green',
  },
]
</script>

<template>
  <div class="cf-root">
    <!-- Caption -->
    <div class="cf-cap">
      <div class="cf-cap-title">commitment schemes と proving systems の 15 年</div>
      <div class="cf-cap-sub">pairing/trusted setup ─ hash-based ─ folding ─ small-field/M31/post-quantum まで</div>
    </div>

    <!-- Main SVG -->
    <svg class="cf-svg" viewBox="0 0 1200 410" preserveAspectRatio="xMidYMid meet">
      <defs>
        <marker id="cf-ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0,0 L 10,5 L 0,10 z" fill="#94a3b8"/>
        </marker>
      </defs>

      <!-- ========= Track 1: Commitment (top) ========= -->
      <g class="cf-track-pill cf-track-pill-commit">
        <rect x="18" y="78" width="125" height="22" rx="11" fill="#fef3c7" stroke="#fcd34d" stroke-width="1.5"/>
        <text x="80" y="94" text-anchor="middle" class="cf-track-label">commitment</text>
      </g>

      <line x1="150" y1="89" x2="1150" y2="89" class="cf-track-line"/>
      <line x1="1115" y1="89" x2="1148" y2="89" class="cf-arrow-end" marker-end="url(#cf-ar)"/>

      <g v-for="m in commitTrack" :key="m.id" :class="['cf-node', `cf-era-${m.era}`]">
        <line :x1="m.x" y1="89" :x2="m.x" y2="68" class="cf-stub"/>
        <rect :x="m.x - 65" y="12" width="130" height="56" rx="8" class="cf-card-bg"/>
        <text :x="m.x" y="32" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="50" text-anchor="middle" class="cf-card-sub">{{ m.sub }}</text>
        <text :x="m.x" y="62" text-anchor="middle" class="cf-card-year">{{ m.year }}</text>
      </g>

      <!-- ========= Track 2: Proving System (middle) ========= -->
      <g class="cf-track-pill cf-track-pill-prove">
        <rect x="18" y="153" width="125" height="22" rx="11" fill="#ede9fe" stroke="#c4b5fd" stroke-width="1.5"/>
        <text x="80" y="169" text-anchor="middle" class="cf-track-label cf-track-label-prove">proving system</text>
      </g>

      <line x1="150" y1="164" x2="1150" y2="164" class="cf-track-line"/>
      <line x1="1115" y1="164" x2="1148" y2="164" class="cf-arrow-end" marker-end="url(#cf-ar)"/>

      <g v-for="m in proveTrack" :key="m.id" :class="['cf-node', `cf-era-${m.era}`]">
        <line :x1="m.x" y1="164" :x2="m.x" y2="185" class="cf-stub"/>
        <rect :x="m.x - 65" y="188" width="130" height="56" rx="8" class="cf-card-bg"/>
        <text :x="m.x" y="208" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="226" text-anchor="middle" class="cf-card-sub">{{ m.sub }}</text>
        <text :x="m.x" y="238" text-anchor="middle" class="cf-card-year">{{ m.year }}</text>
      </g>

      <!-- ========= 2024-2025 最新トレンド ストリップ ========= -->
      <text x="30" y="277" class="cf-trends-header">▶  2024-2025 最新トレンド</text>
      <line x1="220" y1="271" x2="1150" y2="271" stroke="#fb923c" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.7"/>

      <g v-for="(t, i) in trends" :key="t.title" :class="['cf-trend', `cf-trend-${t.hue}`]">
        <rect :x="20 + i * 295" y="285" width="285" height="110" rx="9" class="cf-trend-bg"/>
        <text :x="35 + i * 295" y="307" class="cf-trend-title">{{ t.title }}</text>
        <text :x="35 + i * 295" y="332" class="cf-trend-detail">{{ t.detail }}</text>
        <text :x="35 + i * 295" y="368" class="cf-trend-note">{{ t.note }}</text>
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

/* Timelines */
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
  font-size: 13.5px;
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
.cf-card-year {
  font-size: 10px;
  fill: #94a3b8;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.04em;
}

.cf-era-latest .cf-card-title { fill: #c2410c; }
.cf-era-latest .cf-card-year  { fill: #ea580c; font-weight: 800; }

/* Trends header */
.cf-trends-header {
  font-size: 14px;
  font-weight: 800;
  fill: #c2410c;
  font-family: 'BIZ UDPMincho', serif;
  letter-spacing: 0.04em;
}

/* Trend cards */
.cf-trend-bg {
  fill: white;
  stroke-width: 2;
  filter: drop-shadow(0 2px 5px rgba(0,0,0,0.06));
}
.cf-trend-cyan   .cf-trend-bg { fill: #ecfeff; stroke: #06b6d4; }
.cf-trend-amber  .cf-trend-bg { fill: #fffbeb; stroke: #d97706; }
.cf-trend-purple .cf-trend-bg { fill: #f5f3ff; stroke: #8b5cf6; }
.cf-trend-green  .cf-trend-bg { fill: #f0fdf4; stroke: #10b981; }

.cf-trend-title {
  font-size: 14px;
  font-weight: 800;
  fill: #1f2937;
  font-family: 'JetBrains Mono', monospace;
}
.cf-trend-cyan   .cf-trend-title { fill: #155e75; }
.cf-trend-amber  .cf-trend-title { fill: #92400e; }
.cf-trend-purple .cf-trend-title { fill: #5b21b6; }
.cf-trend-green  .cf-trend-title { fill: #065f46; }

.cf-trend-detail {
  font-size: 13px;
  font-weight: 700;
  fill: #1f2937;
  font-family: 'JetBrains Mono', monospace;
}
.cf-trend-note {
  font-size: 11.5px;
  fill: #4b5563;
  font-family: 'BIZ UDPMincho', serif;
  font-weight: 600;
}
</style>
