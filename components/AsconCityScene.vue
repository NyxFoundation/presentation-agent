<script setup lang="ts">
import { useLoop } from '@tresjs/core'
import { OrbitControls } from '@tresjs/cientos'
import * as THREE from 'three'
import { ref } from 'vue'

const PI = Math.PI
const DoubleSide = THREE.DoubleSide

function makeLabelSprite(text: string, opts: { bg: string; fg?: string; width?: number }) {
  const canvas = document.createElement('canvas')
  canvas.width = 512
  canvas.height = 128
  const ctx = canvas.getContext('2d')!
  ctx.fillStyle = opts.bg
  ctx.fillRect(0, 0, 512, 128)
  ctx.strokeStyle = '#ffffff'
  ctx.lineWidth = 4
  ctx.strokeRect(2, 2, 508, 124)
  ctx.fillStyle = opts.fg ?? '#ffffff'
  ctx.font = 'bold 64px "ui-monospace", "Menlo", monospace'
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'
  ctx.fillText(text, 256, 70)
  const texture = new THREE.CanvasTexture(canvas)
  texture.minFilter = THREE.LinearFilter
  texture.magFilter = THREE.LinearFilter
  texture.needsUpdate = true
  const material = new THREE.SpriteMaterial({ map: texture, transparent: true })
  const sprite = new THREE.Sprite(material)
  const w = opts.width ?? 3
  sprite.scale.set(w, w * 0.25, 1)
  return sprite
}

function makeBadgeTexture(letter: string, color: string) {
  const canvas = document.createElement('canvas')
  canvas.width = 128
  canvas.height = 128
  const ctx = canvas.getContext('2d')!
  ctx.clearRect(0, 0, 128, 128)
  ctx.shadowColor = color
  ctx.shadowBlur = 18
  ctx.beginPath()
  ctx.arc(64, 64, 50, 0, Math.PI * 2)
  ctx.fillStyle = '#0a0e1a'
  ctx.fill()
  ctx.shadowBlur = 0
  ctx.lineWidth = 6
  ctx.strokeStyle = color
  ctx.stroke()
  ctx.fillStyle = color
  ctx.font = 'bold 70px "ui-monospace", "Menlo", monospace'
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'
  ctx.fillText(letter, 64, 70)
  const texture = new THREE.CanvasTexture(canvas)
  texture.minFilter = THREE.LinearFilter
  texture.magFilter = THREE.LinearFilter
  texture.needsUpdate = true
  return texture
}

function makeBubbleTexture(text: string, accent: string) {
  const w = 384, h = 176
  const canvas = document.createElement('canvas')
  canvas.width = w
  canvas.height = h
  const ctx = canvas.getContext('2d')!
  ctx.clearRect(0, 0, w, h)
  ctx.shadowColor = accent
  ctx.shadowBlur = 22
  const r = 18
  const bh = h - 36
  ctx.beginPath()
  ctx.moveTo(r, 6)
  ctx.lineTo(w - r, 6)
  ctx.quadraticCurveTo(w - 2, 6, w - 2, r + 6)
  ctx.lineTo(w - 2, bh - r)
  ctx.quadraticCurveTo(w - 2, bh, w - r - 2, bh)
  ctx.lineTo(110, bh)
  ctx.lineTo(80, h - 6)
  ctx.lineTo(60, bh)
  ctx.lineTo(r, bh)
  ctx.quadraticCurveTo(2, bh, 2, bh - r)
  ctx.lineTo(2, r + 6)
  ctx.quadraticCurveTo(2, 6, r, 6)
  ctx.closePath()
  ctx.fillStyle = '#0a0e1a'
  ctx.fill()
  ctx.shadowBlur = 0
  ctx.lineWidth = 5
  ctx.strokeStyle = accent
  ctx.stroke()
  ctx.fillStyle = accent
  ctx.font = 'bold 56px "ui-monospace", "Menlo", monospace'
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'
  ctx.fillText(text, w / 2, bh / 2 + 4)
  const texture = new THREE.CanvasTexture(canvas)
  texture.minFilter = THREE.LinearFilter
  texture.magFilter = THREE.LinearFilter
  texture.needsUpdate = true
  return texture
}

function makePlatformGridTexture() {
  const W = 1300, H = 450
  const canvas = document.createElement('canvas')
  canvas.width = W
  canvas.height = H
  const ctx = canvas.getContext('2d')!
  ctx.fillStyle = '#080c1a'
  ctx.fillRect(0, 0, W, H)
  ctx.strokeStyle = '#0ea5e9'
  ctx.lineWidth = 1
  ctx.globalAlpha = 0.4
  const step = 50
  for (let x = 0; x <= W; x += step) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke()
  }
  for (let y = 0; y <= H; y += step) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke()
  }
  ctx.strokeStyle = '#22d3ee'
  ctx.lineWidth = 2
  ctx.globalAlpha = 0.85
  for (let x = 0; x <= W; x += step * 4) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke()
  }
  for (let y = 0; y <= H; y += step * 4) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke()
  }
  ctx.fillStyle = '#ec4899'
  ctx.globalAlpha = 0.95
  for (let i = 0; i < 28; i++) {
    const x = Math.random() * W
    const y = Math.random() * H
    ctx.beginPath()
    ctx.arc(x, y, 2.2, 0, Math.PI * 2)
    ctx.fill()
  }
  const texture = new THREE.CanvasTexture(canvas)
  texture.minFilter = THREE.LinearFilter
  texture.magFilter = THREE.LinearFilter
  texture.needsUpdate = true
  return texture
}

const labels = {
  uniswap: makeLabelSprite('UNISWAP', { bg: '#ff1493' }),
  aave: makeLabelSprite('AAVE', { bg: '#a855f7' }),
  maker: makeLabelSprite('MAKERDAO', { bg: '#06b6d4' }),
  rwa: makeLabelSprite('RWA FARM', { bg: '#84cc16' }),
  deploy: makeLabelSprite('+ DEPLOY HERE', { bg: '#fbbf24', fg: '#000000' }),
}
labels.uniswap.position.set(0, 4.4, 0)
labels.aave.position.set(0, 4.6, 0)
labels.maker.position.set(0, 4.4, 0)
labels.rwa.position.set(0, 4.4, 0)
labels.deploy.position.set(0, 2.0, 0)

const badgeTextures = {
  T: makeBadgeTexture('T', '#22ee99'),
  H: makeBadgeTexture('H', '#ff4d4d'),
  V: makeBadgeTexture('V', '#5c91ff'),
}

const traderBubbleTexs = ['BUY $ETH', 'ARB!', 'SWAP →', 'MEV +20%'].map(t => makeBubbleTexture(t, '#22ee99'))
const hackerBubbleTexs = ['REENTRANCY?', 'ORACLE HIT', 'FLASH LOAN'].map(t => makeBubbleTexture(t, '#ff4d4d'))
const droneBubbleTexs = ['LEAN ✓', 'PROOF OK', 'INV CHECK'].map(t => makeBubbleTexture(t, '#5c91ff'))

const platformGridTexture = makePlatformGridTexture()

const aaveColumnPositions = [-1.0, -0.35, 0.3, 0.95]

type V3 = [number, number, number]

const traderBaseX = [-7.5, -3, 1.5, 6.5]
const traderPositions = ref<V3[]>(traderBaseX.map((x) => [x, 0.55, 1.8]))
const traderBubbleScale = ref<number[]>(traderBaseX.map(() => 0))

const hackerBaseX = [-10.5, -2.2, 7.5]
const hackerTargets: V3[] = [[-9, 1.6, 0.6], [0, 1.4, 0.6], [9, 0.7, 0.6]]
const hackerPositions = ref<V3[]>(hackerBaseX.map((x) => [x, 0.55, -1.8]))
const hackerBubbleScale = ref<number[]>(hackerBaseX.map(() => 0))
const hackerAttackOpacity = ref<number[]>(hackerBaseX.map(() => 0))
const hackerAttackPos = ref<V3[]>(hackerBaseX.map(() => [0, 0, 0]))
const hackerAttackRot = ref<V3[]>(hackerBaseX.map(() => [0, 0, 0]))
const hackerAttackLength = ref<number[]>(hackerBaseX.map(() => 1))
const hackerImpactScale = ref<number[]>(hackerBaseX.map(() => 0))

const droneBaseX = [-8, 0, 6]
const droneTargets: V3[] = [[-9, 0.05, 0], [0, 0.05, 0], [4.8, 0.05, 0]]
const dronePositions = ref<V3[]>(droneBaseX.map((x) => [x, 5, 0]))
const droneRotations = ref<V3[]>(droneBaseX.map(() => [0, 0, 0]))
const droneScanOpacity = ref<number[]>(droneBaseX.map(() => 0))
const droneScanPos = ref<V3[]>(droneBaseX.map(() => [0, 0, 0]))
const droneScanRot = ref<V3[]>(droneBaseX.map(() => [0, 0, 0]))
const droneScanLength = ref<number[]>(droneBaseX.map(() => 1))
const droneBubbleScale = ref<number[]>(droneBaseX.map(() => 0))

const smokePositions = ref<V3[]>([0, 1, 2].map(() => [1, 4.5, -0.6]))
const smokeOpacity = ref<number[]>([0.7, 0.5, 0.3])
const smokeScale = ref<number[]>([1, 1, 1])

const _quat = new THREE.Quaternion()
const _euler = new THREE.Euler()
const _yAxis = new THREE.Vector3(0, 1, 0)
const _dir = new THREE.Vector3()
function alignedCylinder(from: V3, to: V3) {
  const dx = to[0] - from[0]
  const dy = to[1] - from[1]
  const dz = to[2] - from[2]
  const length = Math.max(0.001, Math.sqrt(dx * dx + dy * dy + dz * dz))
  const mid: V3 = [(from[0] + to[0]) / 2, (from[1] + to[1]) / 2, (from[2] + to[2]) / 2]
  _dir.set(dx / length, dy / length, dz / length)
  _quat.setFromUnitVectors(_yAxis, _dir)
  _euler.setFromQuaternion(_quat)
  return { pos: mid, rot: [_euler.x, _euler.y, _euler.z] as V3, length }
}

const { onBeforeRender } = useLoop()
onBeforeRender(({ elapsed }) => {
  dronePositions.value = droneBaseX.map((x, i) => [
    x,
    5 + Math.sin(elapsed * 1.2 + i * 1.6) * 0.35,
    0,
  ])
  droneRotations.value = droneBaseX.map((_, i) => [0, elapsed * 0.5 + i, 0])

  traderPositions.value = traderBaseX.map((x, i) => [
    x + Math.sin(elapsed * 0.5 + i) * 1.2,
    0.55 + Math.abs(Math.sin(elapsed * 4 + i * 2)) * 0.06,
    1.8,
  ])

  hackerPositions.value = hackerBaseX.map((x, i) => [
    x + Math.sin(elapsed * 0.3 + i) * 0.5,
    0.55,
    -1.8,
  ])

  smokePositions.value = [0, 1, 2].map((i) => {
    const t = (elapsed * 0.5 + i * 0.4) % 1
    return [1, 3.2 + t * 1.6, -0.6]
  })
  smokeOpacity.value = [0, 1, 2].map((i) => {
    const t = (elapsed * 0.5 + i * 0.4) % 1
    return (1 - t) * 0.7
  })
  smokeScale.value = [0, 1, 2].map((i) => {
    const t = (elapsed * 0.5 + i * 0.4) % 1
    return 0.5 + t * 1.2
  })

  // Trader speech bubbles cycle in/out
  traderBubbleScale.value = traderBaseX.map((_, i) => {
    const cycle = 5
    const t = (elapsed + i * 1.3) % cycle
    if (t < 1.7) return Math.sin((t / 1.7) * Math.PI) * 1.15
    return 0
  })

  // Hacker bubble + attack zap — bubble first, attack burst right after
  const hackerCycle = 4.2
  hackerBubbleScale.value = hackerBaseX.map((_, i) => {
    const t = (elapsed + i * 1.4) % hackerCycle
    if (t < 1.4) return Math.sin((t / 1.4) * Math.PI) * 1.05
    return 0
  })
  hackerAttackOpacity.value = hackerBaseX.map((_, i) => {
    const t = (elapsed + i * 1.4) % hackerCycle
    if (t > 1.3 && t < 2.5) return Math.sin(((t - 1.3) / 1.2) * Math.PI) * 0.9
    return 0
  })
  hackerImpactScale.value = hackerBaseX.map((_, i) => {
    const t = (elapsed + i * 1.4) % hackerCycle
    if (t > 1.6 && t < 2.6) return Math.sin(((t - 1.6) / 1.0) * Math.PI) * 0.7
    return 0
  })
  hackerBaseX.forEach((_, i) => {
    const cyl = alignedCylinder(hackerPositions.value[i], hackerTargets[i])
    hackerAttackPos.value[i] = cyl.pos
    hackerAttackRot.value[i] = cyl.rot
    hackerAttackLength.value[i] = cyl.length
  })
  hackerAttackPos.value = [...hackerAttackPos.value]
  hackerAttackRot.value = [...hackerAttackRot.value]
  hackerAttackLength.value = [...hackerAttackLength.value]

  // Drone scan beams
  const droneCycle = 5.4
  droneScanOpacity.value = droneBaseX.map((_, i) => {
    const t = (elapsed + i * 1.7) % droneCycle
    if (t < 2.2) return Math.sin((t / 2.2) * Math.PI) * 0.4
    return 0
  })
  droneBubbleScale.value = droneBaseX.map((_, i) => {
    const t = (elapsed + i * 1.7) % droneCycle
    if (t < 2) return Math.sin((t / 2) * Math.PI) * 1.05
    return 0
  })
  droneBaseX.forEach((_, i) => {
    const cyl = alignedCylinder(dronePositions.value[i], droneTargets[i])
    droneScanPos.value[i] = cyl.pos
    droneScanRot.value[i] = cyl.rot
    droneScanLength.value[i] = cyl.length
  })
  droneScanPos.value = [...droneScanPos.value]
  droneScanRot.value = [...droneScanRot.value]
  droneScanLength.value = [...droneScanLength.value]
})
</script>

<template>
  <TresPerspectiveCamera :position="[18, 13, 22]" :fov="46" :look-at="[0, 1.2, 0]" />
  <OrbitControls
    :auto-rotate="false"
    :enable-damping="false"
    :enable-pan="false"
    :min-distance="14"
    :max-distance="40"
    :min-polar-angle="0.3"
    :max-polar-angle="1.35"
    :target="[0, 1.2, 0]"
  />

  <TresFog :args="['#06081a', 24, 70]" />

  <TresAmbientLight :intensity="0.45" color="#3a4a6a" />
  <TresDirectionalLight :position="[10, 18, 12]" :intensity="0.9" color="#dde6ff" />
  <TresHemisphereLight :args="['#1a2540', '#080510', 0.4]" />
  <TresPointLight :position="[-12, 5, 6]" color="#22d3ee" :intensity="120" :distance="20" :decay="2" />
  <TresPointLight :position="[12, 5, -5]" color="#ec4899" :intensity="120" :distance="20" :decay="2" />
  <TresPointLight :position="[0, 9, 0]" color="#a855f7" :intensity="60" :distance="14" :decay="2" />

  <!-- Platform base -->
  <TresMesh :position="[0, -0.3, 0]">
    <TresBoxGeometry :args="[26, 0.6, 9]" />
    <TresMeshStandardMaterial color="#08090d" :metalness="0.6" :roughness="0.4" />
  </TresMesh>
  <!-- Platform top with cyber grid -->
  <TresMesh :position="[0, 0.012, 0]" :rotation="[-PI / 2, 0, 0]">
    <TresPlaneGeometry :args="[25.8, 8.8]" />
    <TresMeshBasicMaterial :map="platformGridTexture" />
  </TresMesh>
  <!-- Neon edge frame -->
  <TresMesh :position="[0, 0.06, 4.4]">
    <TresBoxGeometry :args="[25.8, 0.06, 0.08]" />
    <TresMeshBasicMaterial color="#22d3ee" />
  </TresMesh>
  <TresMesh :position="[0, 0.06, -4.4]">
    <TresBoxGeometry :args="[25.8, 0.06, 0.08]" />
    <TresMeshBasicMaterial color="#22d3ee" />
  </TresMesh>
  <TresMesh :position="[12.9, 0.06, 0]">
    <TresBoxGeometry :args="[0.08, 0.06, 8.8]" />
    <TresMeshBasicMaterial color="#ec4899" />
  </TresMesh>
  <TresMesh :position="[-12.9, 0.06, 0]">
    <TresBoxGeometry :args="[0.08, 0.06, 8.8]" />
    <TresMeshBasicMaterial color="#ec4899" />
  </TresMesh>

  <!-- UNISWAP -->
  <TresGroup :position="[-9, 0, 0]">
    <TresMesh :position="[0, 1.1, 0]">
      <TresBoxGeometry :args="[2.6, 2.2, 2.6]" />
      <TresMeshStandardMaterial color="#1a0e18" :emissive="'#ff1493'" :emissive-intensity="0.18" :metalness="0.3" :roughness="0.4" />
    </TresMesh>
    <TresMesh :position="[0, 2.85, 0]" :rotation="[0, PI / 4, 0]">
      <TresConeGeometry :args="[1.95, 1.4, 4]" />
      <TresMeshStandardMaterial color="#ff1493" :emissive="'#ff1493'" :emissive-intensity="0.9" />
    </TresMesh>
    <TresMesh :position="[0, 3.85, 0]">
      <TresConeGeometry :args="[0.1, 0.5, 12]" />
      <TresMeshStandardMaterial color="#ff5fb0" :emissive="'#ff1493'" :emissive-intensity="1.4" />
    </TresMesh>
    <TresMesh :position="[0, 0.45, 1.35]">
      <TresBoxGeometry :args="[2.7, 0.12, 0.4]" />
      <TresMeshStandardMaterial color="#ff1493" :emissive="'#ff1493'" :emissive-intensity="0.8" />
    </TresMesh>
    <TresMesh :position="[0, 0.7, 1.31]">
      <TresBoxGeometry :args="[0.6, 1.1, 0.05]" />
      <TresMeshStandardMaterial color="#0a0510" />
    </TresMesh>
    <TresMesh :position="[-0.85, 1.5, 1.31]">
      <TresBoxGeometry :args="[0.6, 0.6, 0.05]" />
      <TresMeshStandardMaterial color="#22d3ee" :emissive="'#22d3ee'" :emissive-intensity="0.7" />
    </TresMesh>
    <TresMesh :position="[0.85, 1.5, 1.31]">
      <TresBoxGeometry :args="[0.6, 0.6, 0.05]" />
      <TresMeshStandardMaterial color="#22d3ee" :emissive="'#22d3ee'" :emissive-intensity="0.7" />
    </TresMesh>
    <primitive :object="labels.uniswap" />
  </TresGroup>

  <!-- AAVE -->
  <TresGroup :position="[-4.5, 0, 0]">
    <TresMesh :position="[0, 1.25, 0]">
      <TresBoxGeometry :args="[3, 2.5, 2.5]" />
      <TresMeshStandardMaterial color="#160e2a" :emissive="'#a855f7'" :emissive-intensity="0.18" :metalness="0.3" :roughness="0.4" />
    </TresMesh>
    <TresMesh :position="[0, 2.8, 0]">
      <TresConeGeometry :args="[1.8, 0.8, 3]" />
      <TresMeshStandardMaterial color="#a855f7" :emissive="'#a855f7'" :emissive-intensity="0.9" />
    </TresMesh>
    <TresMesh
      v-for="(cx, i) in aaveColumnPositions"
      :key="`col-${i}`"
      :position="[cx, 1.2, 1.27]"
    >
      <TresCylinderGeometry :args="[0.13, 0.13, 2.4, 12]" />
      <TresMeshStandardMaterial color="#e8e3f2" :emissive="'#a855f7'" :emissive-intensity="0.45" />
    </TresMesh>
    <TresMesh :position="[0, 0.05, 1.3]">
      <TresBoxGeometry :args="[3.2, 0.1, 0.4]" />
      <TresMeshStandardMaterial color="#a855f7" :emissive="'#a855f7'" :emissive-intensity="0.6" />
    </TresMesh>
    <primitive :object="labels.aave" />
  </TresGroup>

  <!-- MAKERDAO -->
  <TresGroup :position="[0, 0, 0]">
    <TresMesh :position="[0, 1, 0]">
      <TresBoxGeometry :args="[3, 2, 2.4]" />
      <TresMeshStandardMaterial color="#0a1a22" :emissive="'#06b6d4'" :emissive-intensity="0.2" :metalness="0.3" :roughness="0.4" />
    </TresMesh>
    <TresMesh :position="[0, 2.05, 0]">
      <TresBoxGeometry :args="[3.05, 0.1, 2.45]" />
      <TresMeshStandardMaterial color="#06b6d4" :emissive="'#06b6d4'" :emissive-intensity="0.8" />
    </TresMesh>
    <TresMesh :position="[1, 3.1, -0.6]">
      <TresCylinderGeometry :args="[0.22, 0.22, 2.2, 16]" />
      <TresMeshStandardMaterial color="#1a1a22" />
    </TresMesh>
    <TresMesh :position="[1, 4.21, -0.6]">
      <TresCylinderGeometry :args="[0.27, 0.27, 0.08, 16]" />
      <TresMeshStandardMaterial color="#374151" />
    </TresMesh>
    <TresMesh
      v-for="(p, i) in smokePositions"
      :key="`smoke-${i}`"
      :position="p"
      :scale="smokeScale[i]"
    >
      <TresSphereGeometry :args="[0.25, 12, 12]" />
      <TresMeshBasicMaterial color="#cbd5e1" :transparent="true" :opacity="smokeOpacity[i]" />
    </TresMesh>
    <TresMesh :position="[0, 0.7, 1.21]">
      <TresBoxGeometry :args="[1.6, 1.2, 0.05]" />
      <TresMeshStandardMaterial color="#06b6d4" :emissive="'#06b6d4'" :emissive-intensity="0.55" />
    </TresMesh>
    <primitive :object="labels.maker" />
  </TresGroup>

  <!-- RWA FARM -->
  <TresGroup :position="[4.8, 0, 0]">
    <TresMesh :position="[0, 0.02, 1.8]" :rotation="[-PI / 2, 0, 0]">
      <TresPlaneGeometry :args="[4, 1.6]" />
      <TresMeshStandardMaterial color="#0a2010" :emissive="'#84cc16'" :emissive-intensity="0.3" :roughness="0.9" />
    </TresMesh>
    <TresMesh
      v-for="i in 6"
      :key="`crop-${i}`"
      :position="[-1.6 + i * 0.55, 0.12, 1.8]"
    >
      <TresBoxGeometry :args="[0.04, 0.2, 1.5]" />
      <TresMeshStandardMaterial color="#84cc16" :emissive="'#84cc16'" :emissive-intensity="0.6" />
    </TresMesh>

    <TresGroup :position="[-1.6, 0, 0]">
      <TresMesh :position="[0, 1.4, 0]">
        <TresCylinderGeometry :args="[0.55, 0.55, 2.8, 18]" />
        <TresMeshStandardMaterial color="#403828" :emissive="'#fbbf24'" :emissive-intensity="0.22" />
      </TresMesh>
      <TresMesh :position="[0, 0.6, 0]">
        <TresCylinderGeometry :args="[0.56, 0.56, 0.06, 18]" />
        <TresMeshStandardMaterial color="#fbbf24" :emissive="'#fbbf24'" :emissive-intensity="0.7" />
      </TresMesh>
      <TresMesh :position="[0, 1.4, 0]">
        <TresCylinderGeometry :args="[0.56, 0.56, 0.06, 18]" />
        <TresMeshStandardMaterial color="#fbbf24" :emissive="'#fbbf24'" :emissive-intensity="0.7" />
      </TresMesh>
      <TresMesh :position="[0, 2.2, 0]">
        <TresCylinderGeometry :args="[0.56, 0.56, 0.06, 18]" />
        <TresMeshStandardMaterial color="#fbbf24" :emissive="'#fbbf24'" :emissive-intensity="0.7" />
      </TresMesh>
      <TresMesh :position="[0, 2.8, 0]">
        <TresSphereGeometry :args="[0.55, 18, 12, 0, PI * 2, 0, PI / 2]" />
        <TresMeshStandardMaterial color="#605040" />
      </TresMesh>
    </TresGroup>

    <TresGroup :position="[0.5, 0, 0]">
      <TresMesh :position="[0, 0.95, 0]">
        <TresBoxGeometry :args="[2, 1.9, 2.2]" />
        <TresMeshStandardMaterial color="#260a0a" :emissive="'#ef4444'" :emissive-intensity="0.35" />
      </TresMesh>
      <TresMesh :position="[0, 2.25, 0]">
        <TresConeGeometry :args="[1.2, 0.9, 4]" />
        <TresMeshStandardMaterial color="#5a1a18" :emissive="'#ef4444'" :emissive-intensity="0.25" />
      </TresMesh>
      <TresMesh :position="[0, 0.55, 1.11]">
        <TresBoxGeometry :args="[0.7, 1.0, 0.05]" />
        <TresMeshStandardMaterial color="#1a0a0a" />
      </TresMesh>
    </TresGroup>

    <primitive :object="labels.rwa" />
  </TresGroup>

  <!-- EMPTY PLOT -->
  <TresGroup :position="[9, 0, 0]">
    <TresMesh :position="[0, 0.6, 0]">
      <TresBoxGeometry :args="[2.6, 1.2, 2.4]" />
      <TresMeshBasicMaterial color="#fbbf24" :wireframe="true" :transparent="true" :opacity="0.75" />
    </TresMesh>
    <TresMesh :position="[0, 0.5, 0.6]">
      <TresBoxGeometry :args="[0.06, 1, 0.06]" />
      <TresMeshStandardMaterial color="#fbbf24" :emissive="'#fbbf24'" :emissive-intensity="0.6" />
    </TresMesh>
    <primitive :object="labels.deploy" />
  </TresGroup>

  <!-- TRADERS (T badge + speech bubble) -->
  <TresGroup
    v-for="(p, i) in traderPositions"
    :key="`trader-${i}`"
    :position="p"
  >
    <TresMesh :position="[0, 0.5, 0]">
      <TresCapsuleGeometry :args="[0.25, 0.55, 6, 12]" />
      <TresMeshStandardMaterial color="#22ee99" :emissive="'#22ee99'" :emissive-intensity="0.5" />
    </TresMesh>
    <TresMesh :position="[0, 1.05, 0]">
      <TresSphereGeometry :args="[0.18, 16, 16]" />
      <TresMeshStandardMaterial color="#f4d2a8" />
    </TresMesh>
    <TresMesh :position="[0.32, 0.45, 0]">
      <TresBoxGeometry :args="[0.18, 0.14, 0.1]" />
      <TresMeshStandardMaterial color="#fbbf24" :emissive="'#fbbf24'" :emissive-intensity="0.5" />
    </TresMesh>
    <TresSprite :position="[0, 1.85, 0]" :scale="[0.7, 0.7, 1]">
      <TresSpriteMaterial :map="badgeTextures.T" :transparent="true" :depth-test="false" />
    </TresSprite>
    <TresSprite
      :position="[0.5, 2.6, 0]"
      :scale="[traderBubbleScale[i] * 1.7, traderBubbleScale[i] * 0.78, 1]"
    >
      <TresSpriteMaterial :map="traderBubbleTexs[i]" :transparent="true" :depth-test="false" />
    </TresSprite>
  </TresGroup>

  <!-- HACKERS (H badge + speech bubble + impact at building) -->
  <TresGroup
    v-for="(p, i) in hackerPositions"
    :key="`hacker-${i}`"
    :position="p"
  >
    <TresMesh :position="[0, 0.5, 0]">
      <TresCapsuleGeometry :args="[0.25, 0.55, 6, 12]" />
      <TresMeshStandardMaterial color="#ff4d4d" :emissive="'#ff4d4d'" :emissive-intensity="0.5" />
    </TresMesh>
    <TresMesh :position="[0, 1.0, 0]">
      <TresConeGeometry :args="[0.28, 0.5, 12]" />
      <TresMeshStandardMaterial color="#8b1a1a" :emissive="'#ff4d4d'" :emissive-intensity="0.4" />
    </TresMesh>
    <TresMesh :position="[0, 0.95, 0.18]">
      <TresSphereGeometry :args="[0.13, 12, 12]" />
      <TresMeshBasicMaterial color="#1a0a0a" />
    </TresMesh>
    <TresSprite :position="[0, 1.85, 0]" :scale="[0.7, 0.7, 1]">
      <TresSpriteMaterial :map="badgeTextures.H" :transparent="true" :depth-test="false" />
    </TresSprite>
    <TresSprite
      :position="[0.5, 2.6, 0]"
      :scale="[hackerBubbleScale[i] * 1.85, hackerBubbleScale[i] * 0.85, 1]"
    >
      <TresSpriteMaterial :map="hackerBubbleTexs[i]" :transparent="true" :depth-test="false" />
    </TresSprite>
  </TresGroup>

  <!-- HACKER ATTACK ZAPS (world space) -->
  <TresMesh
    v-for="(_, i) in hackerBaseX"
    :key="`atk-${i}`"
    :position="hackerAttackPos[i]"
    :rotation="hackerAttackRot[i]"
    :scale="[1, hackerAttackLength[i], 1]"
  >
    <TresCylinderGeometry :args="[0.05, 0.05, 1, 6]" />
    <TresMeshBasicMaterial color="#ff4d4d" :transparent="true" :opacity="hackerAttackOpacity[i]" />
  </TresMesh>
  <!-- Impact flash on the building -->
  <TresMesh
    v-for="(t, i) in hackerTargets"
    :key="`impact-${i}`"
    :position="t"
    :scale="hackerImpactScale[i]"
  >
    <TresSphereGeometry :args="[0.45, 14, 14]" />
    <TresMeshBasicMaterial color="#ffaaaa" :transparent="true" :opacity="0.7" />
  </TresMesh>

  <!-- DRONES (V badge + bubble) -->
  <TresGroup
    v-for="(p, i) in dronePositions"
    :key="`drone-${i}`"
    :position="p"
    :rotation="droneRotations[i]"
  >
    <TresMesh>
      <TresOctahedronGeometry :args="[0.4, 0]" />
      <TresMeshStandardMaterial color="#5c91ff" :emissive="'#5c91ff'" :emissive-intensity="0.7" :metalness="0.4" :roughness="0.4" />
    </TresMesh>
    <TresMesh :position="[0.6, 0, 0]">
      <TresCylinderGeometry :args="[0.04, 0.04, 0.5, 8]" />
      <TresMeshStandardMaterial color="#1a2a4a" />
    </TresMesh>
    <TresMesh :position="[-0.6, 0, 0]">
      <TresCylinderGeometry :args="[0.04, 0.04, 0.5, 8]" />
      <TresMeshStandardMaterial color="#1a2a4a" />
    </TresMesh>
    <TresMesh :position="[0, 0, 0.6]">
      <TresCylinderGeometry :args="[0.04, 0.04, 0.5, 8]" />
      <TresMeshStandardMaterial color="#1a2a4a" />
    </TresMesh>
    <TresMesh :position="[0, 0, -0.6]">
      <TresCylinderGeometry :args="[0.04, 0.04, 0.5, 8]" />
      <TresMeshStandardMaterial color="#1a2a4a" />
    </TresMesh>
    <TresMesh :position="[0.6, 0.08, 0]" :rotation="[PI / 2, 0, 0]">
      <TresCylinderGeometry :args="[0.32, 0.32, 0.02, 24]" />
      <TresMeshStandardMaterial color="#aab8e0" :transparent="true" :opacity="0.5" />
    </TresMesh>
    <TresMesh :position="[-0.6, 0.08, 0]" :rotation="[PI / 2, 0, 0]">
      <TresCylinderGeometry :args="[0.32, 0.32, 0.02, 24]" />
      <TresMeshStandardMaterial color="#aab8e0" :transparent="true" :opacity="0.5" />
    </TresMesh>
    <TresMesh :position="[0, 0.08, 0.6]" :rotation="[PI / 2, 0, 0]">
      <TresCylinderGeometry :args="[0.32, 0.32, 0.02, 24]" />
      <TresMeshStandardMaterial color="#aab8e0" :transparent="true" :opacity="0.5" />
    </TresMesh>
    <TresMesh :position="[0, 0.08, -0.6]" :rotation="[PI / 2, 0, 0]">
      <TresCylinderGeometry :args="[0.32, 0.32, 0.02, 24]" />
      <TresMeshStandardMaterial color="#aab8e0" :transparent="true" :opacity="0.5" />
    </TresMesh>
    <TresSprite :position="[0, 1.1, 0]" :scale="[0.7, 0.7, 1]">
      <TresSpriteMaterial :map="badgeTextures.V" :transparent="true" :depth-test="false" />
    </TresSprite>
    <TresSprite
      :position="[0.5, 1.85, 0]"
      :scale="[droneBubbleScale[i] * 1.7, droneBubbleScale[i] * 0.78, 1]"
    >
      <TresSpriteMaterial :map="droneBubbleTexs[i]" :transparent="true" :depth-test="false" />
    </TresSprite>
  </TresGroup>

  <!-- DRONE SCAN BEAMS (world space) -->
  <TresMesh
    v-for="(_, i) in droneBaseX"
    :key="`scan-${i}`"
    :position="droneScanPos[i]"
    :rotation="droneScanRot[i]"
    :scale="[1, droneScanLength[i], 1]"
  >
    <TresCylinderGeometry :args="[0.45, 0.05, 1, 14, 1, true]" />
    <TresMeshBasicMaterial color="#5c91ff" :transparent="true" :opacity="droneScanOpacity[i]" :side="DoubleSide" />
  </TresMesh>
</template>
