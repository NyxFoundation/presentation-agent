<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, computed } from 'vue'

type Pattern = {
  left: string;
  leftColor: string;
  leftBg: string;
  right: string;
  rightColor: string;
  rightBg: string;
  op: string;
  app: string;
  appNote: string;
  formula: string;
  caption: string;
}

const patterns: Pattern[] = [
  {
    left: 'ZK',     leftColor: '#b45309', leftBg: '#fffbeb',
    right: 'ECDSA / SHA-256\n(既存 ID standard)', rightColor: '#475569', rightBg: '#f8fafc',
    op: 'over',
    app: 'Longfellow',
    appNote: 'mDOC / JWT を ZK 化',
    formula: 'ZK ∘ ECDSA(mDOC)',
    caption: '① ZK over 既存暗号 — 既存の身分証を破壊せず ZK 化',
  },
  {
    left: 'ZK',     leftColor: '#b45309', leftBg: '#fffbeb',
    right: 'FHE',   rightColor: '#6d28d9', rightBg: '#f5f3ff',
    op: '⊕',
    app: 'Verifiable FHE',
    appNote: '機密 + 計算正しさ',
    formula: 'π_ZK { server.f(E(x)) }',
    caption: '② ZK + FHE — FHE の盲点「計算正しさ」を ZK で塞ぐ',
  },
  {
    left: 'MPC',    leftColor: '#0e7490', leftBg: '#ecfeff',
    right: 'FHE',   rightColor: '#6d28d9', rightBg: '#f5f3ff',
    op: '⊕',
    app: 'threshold FHE',
    appNote: 'Zama / NIST 提出',
    formula: 'sk = share(sk₁, ..., sk_n)',
    caption: '③ MPC + FHE — 鍵を MPC で分散して FHE で計算秘匿',
  },
  {
    left: 'ZK',     leftColor: '#b45309', leftBg: '#fffbeb',
    right: 'ML',    rightColor: '#be185d', rightBg: '#fdf2f8',
    op: '⊕',
    app: 'zkML',
    appNote: 'EZKL / ezkl-poc',
    formula: 'π { model(x) = y }',
    caption: '④ ZK + ML — 推論の正しさを暗号的に証明',
  },
  {
    left: 'MPC',    leftColor: '#0e7490', leftBg: '#ecfeff',
    right: 'ML',    rightColor: '#be185d', rightBg: '#fdf2f8',
    op: '⊕',
    app: 'mpcML',
    appNote: '連邦学習 / federated learning',
    formula: 'update(w) ← share(grad_i)',
    caption: '⑤ MPC + ML — 各人の学習データを秘匿しつつ共同学習',
  },
  {
    left: 'ZK',     leftColor: '#b45309', leftBg: '#fffbeb',
    right: 'Multisig', rightColor: '#1d4ed8', rightBg: '#eff6ff',
    op: '⊕',
    app: 'Multisig op proof',
    appNote: 'Nyx Foundation',
    formula: 'π { multisig(op) signed }',
    caption: '⑥ ZK + Multisig — 操作秘匿 + 認証',
  },
  {
    left: 'ZK',     leftColor: '#b45309', leftBg: '#fffbeb',
    right: 'Bridge', rightColor: '#15803d', rightBg: '#f0fdf4',
    op: '⊕',
    app: 'ZK Light Client',
    appNote: 'Polyhedra / Succinct',
    formula: 'π { source.state @ block_n }',
    caption: '⑦ ZK + Bridge — cross-chain message + state proof',
  },
]

const totalPhases = patterns.length

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
const phaseDurations = patterns.map(() => 3800)
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

const current = computed(() => patterns[phase.value])
</script>

<template>
  <div class="cp-root">
    <!-- Caption strip -->
    <div class="cp-cap">
      <transition name="cp-fade" mode="out-in">
        <div :key="phase" class="cp-cap-inner">
          <code class="cp-code">{{ current.formula }}</code>
          <div class="cp-note">{{ current.caption }}</div>
        </div>
      </transition>
    </div>

    <!-- Phase dots indicator (subtle, no controls) -->
    <div class="cp-dots">
      <span v-for="(p, i) in patterns" :key="i"
            class="cp-dot" :class="{ 'is-on': i === phase, 'is-past': i < phase }"/>
    </div>

    <!-- Main SVG -->
    <svg class="cp-svg" viewBox="0 0 1200 340" preserveAspectRatio="xMidYMid meet">
      <defs>
        <marker id="cp-ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0,0 L 10,5 L 0,10 z" fill="#475569"/>
        </marker>
      </defs>

      <!-- Left primitive -->
      <transition name="cp-pop" mode="out-in">
        <g :key="`L-${phase}`" class="cp-prim-g">
          <rect x="80" y="115" width="240" height="110" rx="12"
                :fill="current.leftBg" :stroke="current.leftColor" stroke-width="2.5"
                class="cp-prim-bg"/>
          <text x="200" y="170" text-anchor="middle" class="cp-prim-label"
                :style="{ fill: current.leftColor }">{{ current.left }}</text>
          <text x="200" y="200" text-anchor="middle" class="cp-prim-sub">primitive</text>
        </g>
      </transition>

      <!-- Operator (center) -->
      <transition name="cp-pop" mode="out-in">
        <g :key="`op-${phase}`" class="cp-op-g">
          <circle cx="490" cy="170" r="38" fill="white" stroke="#475569" stroke-width="2.5"/>
          <text x="490" y="180" text-anchor="middle" class="cp-op-text">{{ current.op }}</text>
        </g>
      </transition>

      <!-- Right primitive -->
      <transition name="cp-pop" mode="out-in">
        <g :key="`R-${phase}`" class="cp-prim-g">
          <rect x="580" y="115" width="240" height="110" rx="12"
                :fill="current.rightBg" :stroke="current.rightColor" stroke-width="2.5"
                class="cp-prim-bg"/>
          <text x="700" y="160" text-anchor="middle" class="cp-prim-label"
                :style="{ fill: current.rightColor }"
                v-if="!current.right.includes('\n')">{{ current.right }}</text>
          <g v-else>
            <text x="700" y="160" text-anchor="middle" class="cp-prim-label"
                  :style="{ fill: current.rightColor }">{{ current.right.split('\n')[0] }}</text>
            <text x="700" y="185" text-anchor="middle" class="cp-prim-sub-emph"
                  :style="{ fill: current.rightColor }">{{ current.right.split('\n')[1] }}</text>
          </g>
          <text x="700" y="208" text-anchor="middle" class="cp-prim-sub"
                v-if="!current.right.includes('\n')">primitive / standard</text>
        </g>
      </transition>

      <!-- Arrow → app -->
      <g class="cp-arrow-g">
        <line x1="830" y1="170" x2="900" y2="170" class="cp-out-wire" marker-end="url(#cp-ar)"/>
      </g>

      <!-- App box (right) -->
      <transition name="cp-pop" mode="out-in">
        <g :key="`app-${phase}`" class="cp-app-g">
          <rect x="910" y="115" width="240" height="110" rx="12"
                fill="#fef3c7" stroke="#d97706" stroke-width="3"
                class="cp-app-bg"/>
          <text x="1030" y="156" text-anchor="middle" class="cp-app-title">{{ current.app }}</text>
          <text x="1030" y="183" text-anchor="middle" class="cp-app-sub">{{ current.appNote }}</text>
          <text x="1030" y="208" text-anchor="middle" class="cp-app-tag">application</text>
        </g>
      </transition>

      <!-- Pattern index header -->
      <text x="600" y="40" text-anchor="middle" class="cp-pattern-hdr">合成パターン</text>
      <text x="600" y="65" text-anchor="middle" class="cp-pattern-idx">{{ phase + 1 }} / {{ totalPhases }}</text>

      <!-- Layer labels under boxes -->
      <text x="200" y="260" text-anchor="middle" class="cp-layer">primitive</text>
      <text x="700" y="260" text-anchor="middle" class="cp-layer">primitive / standard</text>
      <text x="1030" y="260" text-anchor="middle" class="cp-layer">application</text>
    </svg>
  </div>
</template>

<style scoped>
.cp-root {
  position: relative;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-family: 'Noto Sans JP', sans-serif;
  color: #111827;
}

.cp-cap {
  padding: 9px 16px;
  background: #eef2ff;
  border: 1px solid #c7d2fe;
  border-radius: 0.5rem;
  min-height: 52px;
  display: flex;
  align-items: center;
}
.cp-cap-inner {
  display: flex;
  flex-direction: column;
  gap: 3px;
  width: 100%;
}
.cp-code {
  font-family: 'JetBrains Mono', monospace;
  font-size: 18px;
  color: #1e1b4b;
  font-weight: 700;
}
.cp-note {
  font-size: 15px;
  color: #4338ca;
  font-weight: 700;
}

.cp-dots {
  display: flex;
  justify-content: center;
  gap: 6px;
  padding: 0;
}
.cp-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #e5e7eb;
  transition: all 0.4s;
}
.cp-dot.is-on   { background: #d97706; transform: scale(1.4); box-shadow: 0 0 6px rgba(217, 119, 6, 0.5); }
.cp-dot.is-past { background: #fcd34d; }

.cp-svg {
  width: 100%;
  height: auto;
  display: block;
  font-family: 'Noto Sans JP', sans-serif;
}

/* Primitives */
.cp-prim-bg {
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.06));
}
.cp-prim-label {
  font-size: 28px;
  font-weight: 900;
  font-family: 'JetBrains Mono', monospace;
}
.cp-prim-sub {
  font-size: 14px;
  fill: #94a3b8;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 600;
  letter-spacing: 0.05em;
}
.cp-prim-sub-emph {
  font-size: 14px;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
}

/* Operator */
.cp-op-text {
  font-size: 28px;
  font-weight: 900;
  fill: #1f2937;
  font-family: 'JetBrains Mono', monospace;
}

/* Arrow */
.cp-out-wire {
  stroke: #475569;
  stroke-width: 2.5;
  stroke-dasharray: 6 3;
  animation: cp-flow 1.2s linear infinite;
  fill: none;
}
@keyframes cp-flow { to { stroke-dashoffset: -18; } }

/* App */
.cp-app-bg {
  filter: drop-shadow(0 2px 6px rgba(217, 119, 6, 0.25));
}
.cp-app-title {
  font-size: 21px;
  font-weight: 900;
  fill: #78350f;
  font-family: 'BIZ UDPMincho', serif;
}
.cp-app-sub {
  font-size: 14px;
  fill: #92400e;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 600;
}
.cp-app-tag {
  font-size: 13px;
  fill: #d97706;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  letter-spacing: 0.06em;
}

/* Header */
.cp-pattern-hdr {
  font-size: 14px;
  fill: #94a3b8;
  font-weight: 700;
  letter-spacing: 0.12em;
  font-family: 'JetBrains Mono', monospace;
}
.cp-pattern-idx {
  font-size: 19px;
  fill: #d97706;
  font-weight: 900;
  font-family: 'JetBrains Mono', monospace;
}
.cp-layer {
  font-size: 13px;
  fill: #cbd5e1;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.06em;
}

/* Transitions: pop in/out for cycling content */
.cp-pop-enter-active {
  transition: opacity 0.4s ease, transform 0.4s ease;
}
.cp-pop-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.cp-pop-enter-from { opacity: 0; transform: scale(0.92) translateY(6px); }
.cp-pop-leave-to   { opacity: 0; transform: scale(0.96) translateY(-4px); }

.cp-fade-enter-active, .cp-fade-leave-active {
  transition: opacity 0.4s ease, transform 0.4s ease;
}
.cp-fade-enter-from { opacity: 0; transform: translateY(4px); }
.cp-fade-leave-to { opacity: 0; transform: translateY(-4px); }
</style>
