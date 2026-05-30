<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, computed } from 'vue'

const totalPhases = 6

function getInitialPhase(): { phase: number; play: boolean } {
  if (typeof window === 'undefined') return { phase: 0, play: true }
  const p = new URLSearchParams(window.location.search)
  const raw = p.get('phase') ?? p.get('stage')
  if (raw == null) return { phase: 0, play: true }
  const s = parseInt(raw, 10)
  if (!Number.isNaN(s) && s >= 0 && s < totalPhases) return { phase: s, play: false }
  return { phase: 0, play: true }
}

const initial = getInitialPhase()
const phase = ref(initial.phase)
const phaseDurations = [3500, 4500, 4500, 4500, 5000, 5500]
const isPlaying = ref(initial.play)
let timeoutId: ReturnType<typeof setTimeout> | null = null

function scheduleNext() {
  if (timeoutId) { clearTimeout(timeoutId); timeoutId = null }
  if (!isPlaying.value) return
  timeoutId = setTimeout(advance, phaseDurations[phase.value])
}
function advance() {
  phase.value = (phase.value + 1) % totalPhases
  scheduleNext()
}
onMounted(() => { if (isPlaying.value) scheduleNext() })
onBeforeUnmount(() => { if (timeoutId) clearTimeout(timeoutId) })

const captions = [
  { code: 'commitment: KZG (pairing, trusted setup)  ‖  folding: Halo2 (accumulation)', note: '~2019: pairing-based 全盛、setup ceremony が前提' },
  { code: '+ FRI / Ligero (hash-based)   /   Nova (folding scheme)',                    note: '2017-22: hash-based の系譜と「folding」という新概念が立ち上がる' },
  { code: '+ Brakedown (linear-time, field-agnostic)',                                  note: '2023: linear-time prover、field の自由度' },
  { code: '+ BaseFold (2024)   /   LatticeFold+ (2025)',                                note: '2024-25: hash-based commitment と lattice-based folding が成熟' },
  { code: '+ hash-based folding (2025-26) → IVC / recursion 全層 hash-based',          note: '2025-26: setup-free + post-quantum へ統合' },
  { code: '✓ commitment + folding + 証明系  3 軸すべてが  hash-based / setup-free',     note: '10 年前の SNARK 常識は通用しない' },
]

// timeline: which milestones are visible at each phase
type Milestone = {
  id: string;
  track: 'commit' | 'fold';
  year: string;
  x: number;
  bornAt: number; // phase at which it becomes visible
  label: string;
  sub: string;
  type: 'trusted' | 'hash' | 'lattice';
}

const milestones: Milestone[] = [
  { id: 'kzg',     track: 'commit', year: '~2010', x: 230,  bornAt: 0, label: 'KZG',           sub: 'pairing / trusted setup',   type: 'trusted' },
  { id: 'halo',    track: 'fold',   year: '~2020', x: 230,  bornAt: 0, label: 'Halo2',         sub: 'accumulation',              type: 'trusted' },
  { id: 'fri',     track: 'commit', year: '~2017', x: 410,  bornAt: 1, label: 'FRI / Ligero',  sub: 'hash-based',                type: 'hash' },
  { id: 'nova',    track: 'fold',   year: '~2022', x: 410,  bornAt: 1, label: 'Nova',          sub: 'folding scheme',            type: 'hash' },
  { id: 'brake',   track: 'commit', year: '2023',  x: 600,  bornAt: 2, label: 'Brakedown',     sub: 'linear-time',               type: 'hash' },
  { id: 'base',    track: 'commit', year: '2024',  x: 800,  bornAt: 3, label: 'BaseFold',      sub: 'hash-based',                type: 'hash' },
  { id: 'lat',     track: 'fold',   year: '2025',  x: 800,  bornAt: 3, label: 'LatticeFold+',  sub: 'lattice-based',             type: 'lattice' },
  { id: 'hfold',   track: 'fold',   year: '25-26', x: 1000, bornAt: 4, label: 'hash-based folding', sub: 'IVC / full hash stack', type: 'hash' },
]

function isVisible(m: Milestone) { return phase.value >= m.bornAt }
function isNew(m: Milestone) { return phase.value === m.bornAt && m.bornAt > 0 }

const commitTrack = computed(() => milestones.filter(m => m.track === 'commit'))
const foldTrack   = computed(() => milestones.filter(m => m.track === 'fold'))
</script>

<template>
  <div class="cf-root">
    <!-- Caption strip -->
    <div class="cf-cap">
      <transition name="cf-fade" mode="out-in">
        <div :key="phase" class="cf-cap-inner">
          <code class="cf-code">{{ captions[phase].code }}</code>
          <div class="cf-note">{{ captions[phase].note }}</div>
        </div>
      </transition>
    </div>

    <!-- Main SVG -->
    <svg class="cf-svg" viewBox="0 0 1200 360" preserveAspectRatio="xMidYMid meet">
      <defs>
        <marker id="cf-ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0,0 L 10,5 L 0,10 z" fill="#94a3b8"/>
        </marker>
      </defs>

      <!-- Track labels (compact pills aligned with timelines) -->
      <g class="cf-track-pill cf-track-pill-commit">
        <rect x="20" y="70" width="92" height="22" rx="11" fill="#fef3c7" stroke="#fcd34d" stroke-width="1.5"/>
        <text x="66" y="86" text-anchor="middle" class="cf-track-label">commitment</text>
      </g>

      <g class="cf-track-pill cf-track-pill-fold">
        <rect x="20" y="190" width="92" height="22" rx="11" fill="#ede9fe" stroke="#c4b5fd" stroke-width="1.5"/>
        <text x="66" y="206" text-anchor="middle" class="cf-track-label cf-track-label-fold">folding/IVC</text>
      </g>

      <!-- Timeline horizontal lines -->
      <line x1="120" y1="80" x2="1150" y2="80" class="cf-track-line"/>
      <line x1="120" y1="200" class="cf-track-line" x2="1150" y2="200"/>

      <!-- Commitment milestones -->
      <g v-for="m in commitTrack" :key="m.id" class="cf-node"
         :class="[`cf-type-${m.type}`, { 'is-visible': isVisible(m), 'is-new': isNew(m) }]">
        <line :x1="m.x" y1="80" :x2="m.x" y2="48" class="cf-stub"/>
        <rect :x="m.x - 78" y="20" width="156" height="56" rx="8" class="cf-card-bg"/>
        <text :x="m.x" y="42" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="62" text-anchor="middle" class="cf-card-sub">{{ m.sub }}</text>
        <text :x="m.x" y="100" text-anchor="middle" class="cf-year">{{ m.year }}</text>
      </g>

      <!-- Folding milestones -->
      <g v-for="m in foldTrack" :key="m.id" class="cf-node"
         :class="[`cf-type-${m.type}`, { 'is-visible': isVisible(m), 'is-new': isNew(m) }]">
        <line :x1="m.x" y1="200" :x2="m.x" y2="232" class="cf-stub"/>
        <rect :x="m.x - 78" y="240" width="156" height="56" rx="8" class="cf-card-bg"/>
        <text :x="m.x" y="262" text-anchor="middle" class="cf-card-title">{{ m.label }}</text>
        <text :x="m.x" y="282" text-anchor="middle" class="cf-card-sub">{{ m.sub }}</text>
        <text :x="m.x" y="222" text-anchor="middle" class="cf-year">{{ m.year }}</text>
      </g>

      <!-- direction arrow at end -->
      <line x1="1110" y1="80" x2="1145" y2="80" class="cf-arrow-end" marker-end="url(#cf-ar)"/>
      <line x1="1110" y1="200" x2="1145" y2="200" class="cf-arrow-end" marker-end="url(#cf-ar)"/>

      <!-- Summary band (final phase) -->
      <transition name="cf-fade">
        <g v-if="phase >= 5" class="cf-summary">
          <rect x="120" y="320" width="1030" height="38" rx="6"
                fill="#dcfce7" stroke="#059669" stroke-width="2"
                style="filter: drop-shadow(0 0 8px rgba(5,150,105,0.35));"/>
          <text x="635" y="346" text-anchor="middle" class="cf-summary-text">
            証明系 + commitment + folding  ─  3 軸すべてが  hash-based / setup-free / post-quantum
          </text>
        </g>
      </transition>
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
  min-height: 52px;
  display: flex;
  align-items: center;
}
.cf-cap-inner {
  display: flex;
  flex-direction: column;
  gap: 3px;
  width: 100%;
}
.cf-code {
  font-family: 'JetBrains Mono', monospace;
  font-size: 16px;
  color: #1e1b4b;
  font-weight: 700;
}
.cf-note {
  font-size: 14px;
  color: #4338ca;
  font-weight: 600;
}

.cf-svg {
  width: 100%;
  height: auto;
  display: block;
  font-family: 'Noto Sans JP', sans-serif;
}

/* Track labels (compact pill style) */
.cf-track-label {
  font-size: 12px;
  font-weight: 800;
  fill: #78350f;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.04em;
}
.cf-track-label-fold { fill: #5b21b6; }

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
.cf-node { opacity: 0; transition: opacity 0.6s ease, transform 0.6s ease; }
.cf-node.is-visible { opacity: 1; }
.cf-node.is-new .cf-card-bg {
  filter: drop-shadow(0 0 10px rgba(220, 38, 38, 0.5));
  stroke-width: 3 !important;
}
.cf-stub {
  stroke: #94a3b8;
  stroke-width: 1.8;
}

.cf-card-bg {
  fill: white;
  stroke-width: 2;
  transition: fill 0.5s, stroke 0.5s, stroke-width 0.5s, filter 0.5s;
}
.cf-type-trusted .cf-card-bg { fill: #fef2f2; stroke: #f87171; }
.cf-type-hash .cf-card-bg    { fill: #f0fdf4; stroke: #86efac; }
.cf-type-lattice .cf-card-bg { fill: #ecfeff; stroke: #67e8f9; }

.cf-card-title {
  font-size: 17px;
  font-weight: 800;
  fill: #1f2937;
  font-family: 'BIZ UDPMincho', serif;
}
.cf-card-sub {
  font-size: 12px;
  fill: #475569;
  font-weight: 600;
  font-family: 'JetBrains Mono', monospace;
}

.cf-year {
  font-size: 12px;
  fill: #94a3b8;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.05em;
}

/* Summary */
.cf-summary-text {
  font-size: 16px;
  font-weight: 800;
  fill: #064e3b;
  font-family: 'BIZ UDPMincho', serif;
}

/* Transitions */
.cf-fade-enter-active, .cf-fade-leave-active {
  transition: opacity 0.4s ease, transform 0.4s ease;
}
.cf-fade-enter-from { opacity: 0; transform: translateY(4px); }
.cf-fade-leave-to { opacity: 0; transform: translateY(-4px); }
</style>
