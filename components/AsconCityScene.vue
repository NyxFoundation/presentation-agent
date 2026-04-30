<script setup lang="ts">
import { useLoop } from '@tresjs/core'
import { OrbitControls } from '@tresjs/cientos'
import * as THREE from 'three'
import { ref } from 'vue'

const PI = Math.PI

function makeLabelSprite(text: string, opts: { bg: string; fg?: string; width?: number }) {
  const canvas = document.createElement('canvas')
  canvas.width = 512
  canvas.height = 128
  const ctx = canvas.getContext('2d')!
  ctx.fillStyle = opts.bg
  ctx.fillRect(0, 0, 512, 128)
  ctx.strokeStyle = '#000'
  ctx.lineWidth = 6
  ctx.strokeRect(3, 3, 506, 122)
  ctx.fillStyle = opts.fg ?? '#fff'
  ctx.font = 'bold 64px "ui-sans-serif", "system-ui", sans-serif'
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
  ctx.beginPath()
  ctx.arc(64, 64, 54, 0, Math.PI * 2)
  ctx.fillStyle = '#ffffff'
  ctx.fill()
  ctx.lineWidth = 8
  ctx.strokeStyle = color
  ctx.stroke()
  ctx.fillStyle = color
  ctx.font = 'bold 78px "ui-sans-serif", "system-ui", sans-serif'
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'
  ctx.fillText(letter, 64, 70)
  const texture = new THREE.CanvasTexture(canvas)
  texture.minFilter = THREE.LinearFilter
  texture.magFilter = THREE.LinearFilter
  texture.needsUpdate = true
  return texture
}

const labels = {
  uniswap: makeLabelSprite('UNISWAP', { bg: '#ff5e8a' }),
  aave: makeLabelSprite('AAVE', { bg: '#7c6cae' }),
  maker: makeLabelSprite('MAKERDAO', { bg: '#1aab9b' }),
  rwa: makeLabelSprite('RWA FARM', { bg: '#3d6824' }),
  deploy: makeLabelSprite('+ DEPLOY HERE', { bg: '#fbbf24', fg: '#000' }),
}
labels.uniswap.position.set(-9, 4.4, 0)
labels.aave.position.set(-4.5, 4.6, 0)
labels.maker.position.set(0, 4.4, 0)
labels.rwa.position.set(4.8, 4.4, 0)
labels.deploy.position.set(9, 2.0, 0)

const badgeTextures = {
  T: makeBadgeTexture('T', '#1f8a64'),
  H: makeBadgeTexture('H', '#c63a3a'),
  V: makeBadgeTexture('V', '#3a5fc6'),
}

const aaveColumnPositions = [-1.0, -0.35, 0.3, 0.95]

type V3 = [number, number, number]

const traderBaseX = [-7.5, -3, 1.5, 6.5]
const traderPositions = ref<V3[]>(traderBaseX.map((x) => [x, 0.55, 1.8]))

const hackerBaseX = [-10.5, -2.2, 7.5]
const hackerPositions = ref<V3[]>(hackerBaseX.map((x) => [x, 0.55, -1.8]))

const droneBaseX = [-8, 0, 6]
const dronePositions = ref<V3[]>(droneBaseX.map((x) => [x, 5, 0]))
const droneRotations = ref<V3[]>(droneBaseX.map(() => [0, 0, 0]))

const smokeBaseY = [4.65, 5.15, 5.65]
const smokePositions = ref<V3[]>(smokeBaseY.map((y) => [1, y, -0.6]))
const smokeOpacity = ref<number[]>([0.7, 0.5, 0.3])
const smokeScale = ref<number[]>([1, 1, 1])

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

  <TresAmbientLight :intensity="1.1" />
  <TresDirectionalLight :position="[10, 18, 12]" :intensity="1.6" />
  <TresHemisphereLight :args="['#cdd9e8', '#2a2a35', 0.5]" />

  <!-- L2 Platform -->
  <TresMesh :position="[0, -0.3, 0]">
    <TresBoxGeometry :args="[26, 0.6, 9]" />
    <TresMeshStandardMaterial color="#15171a" :metalness="0.3" :roughness="0.7" />
  </TresMesh>
  <TresMesh :position="[0, 0.001, 0]">
    <TresBoxGeometry :args="[25.8, 0.02, 8.8]" />
    <TresMeshStandardMaterial color="#2a2d33" :metalness="0.4" :roughness="0.5" />
  </TresMesh>

  <!-- UNISWAP -->
  <TresGroup :position="[-9, 0, 0]">
    <TresMesh :position="[0, 1.1, 0]">
      <TresBoxGeometry :args="[2.6, 2.2, 2.6]" />
      <TresMeshStandardMaterial color="#ffffff" />
    </TresMesh>
    <TresMesh :position="[0, 2.85, 0]" :rotation="[0, PI / 4, 0]">
      <TresConeGeometry :args="[1.95, 1.4, 4]" />
      <TresMeshStandardMaterial color="#ff5e8a" />
    </TresMesh>
    <TresMesh :position="[0, 3.85, 0]">
      <TresConeGeometry :args="[0.1, 0.5, 12]" />
      <TresMeshStandardMaterial color="#ff5e8a" />
    </TresMesh>
    <TresMesh :position="[0, 0.45, 1.35]">
      <TresBoxGeometry :args="[2.7, 0.12, 0.4]" />
      <TresMeshStandardMaterial color="#ff5e8a" />
    </TresMesh>
    <TresMesh :position="[0, 0.7, 1.31]">
      <TresBoxGeometry :args="[0.6, 1.1, 0.05]" />
      <TresMeshStandardMaterial color="#3a2533" />
    </TresMesh>
    <TresMesh :position="[-0.85, 1.5, 1.31]">
      <TresBoxGeometry :args="[0.6, 0.6, 0.05]" />
      <TresMeshStandardMaterial color="#bcd6e8" />
    </TresMesh>
    <TresMesh :position="[0.85, 1.5, 1.31]">
      <TresBoxGeometry :args="[0.6, 0.6, 0.05]" />
      <TresMeshStandardMaterial color="#bcd6e8" />
    </TresMesh>
    <primitive :object="labels.uniswap" />
  </TresGroup>

  <!-- AAVE -->
  <TresGroup :position="[-4.5, 0, 0]">
    <TresMesh :position="[0, 1.25, 0]">
      <TresBoxGeometry :args="[3, 2.5, 2.5]" />
      <TresMeshStandardMaterial color="#ffffff" />
    </TresMesh>
    <TresMesh :position="[0, 2.8, 0]">
      <TresConeGeometry :args="[1.8, 0.8, 3]" />
      <TresMeshStandardMaterial color="#7c6cae" />
    </TresMesh>
    <TresMesh
      v-for="(cx, i) in aaveColumnPositions"
      :key="`col-${i}`"
      :position="[cx, 1.2, 1.27]"
    >
      <TresCylinderGeometry :args="[0.13, 0.13, 2.4, 12]" />
      <TresMeshStandardMaterial color="#e8e3f2" />
    </TresMesh>
    <TresMesh :position="[0, 0.05, 1.3]">
      <TresBoxGeometry :args="[3.2, 0.1, 0.4]" />
      <TresMeshStandardMaterial color="#cdc4e0" />
    </TresMesh>
    <primitive :object="labels.aave" />
  </TresGroup>

  <!-- MAKERDAO -->
  <TresGroup :position="[0, 0, 0]">
    <TresMesh :position="[0, 1, 0]">
      <TresBoxGeometry :args="[3, 2, 2.4]" />
      <TresMeshStandardMaterial color="#e5e7eb" />
    </TresMesh>
    <TresMesh :position="[0, 2.05, 0]">
      <TresBoxGeometry :args="[3.05, 0.1, 2.45]" />
      <TresMeshStandardMaterial color="#4b5563" />
    </TresMesh>
    <TresMesh :position="[1, 3.1, -0.6]">
      <TresCylinderGeometry :args="[0.22, 0.22, 2.2, 16]" />
      <TresMeshStandardMaterial color="#6b7280" />
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
      <TresMeshStandardMaterial color="#374151" />
    </TresMesh>
    <primitive :object="labels.maker" />
  </TresGroup>

  <!-- RWA FARM -->
  <TresGroup :position="[4.8, 0, 0]">
    <TresMesh :position="[0, 0.02, 1.8]" :rotation="[-PI / 2, 0, 0]">
      <TresPlaneGeometry :args="[4, 1.6]" />
      <TresMeshStandardMaterial color="#7ba858" :roughness="0.9" />
    </TresMesh>
    <TresMesh
      v-for="i in 6"
      :key="`crop-${i}`"
      :position="[-1.6 + i * 0.55, 0.12, 1.8]"
    >
      <TresBoxGeometry :args="[0.04, 0.2, 1.5]" />
      <TresMeshStandardMaterial color="#3d6824" />
    </TresMesh>

    <TresGroup :position="[-1.6, 0, 0]">
      <TresMesh :position="[0, 1.4, 0]">
        <TresCylinderGeometry :args="[0.55, 0.55, 2.8, 18]" />
        <TresMeshStandardMaterial color="#d8c8a0" />
      </TresMesh>
      <TresMesh :position="[0, 0.6, 0]">
        <TresCylinderGeometry :args="[0.56, 0.56, 0.06, 18]" />
        <TresMeshStandardMaterial color="#000" />
      </TresMesh>
      <TresMesh :position="[0, 1.4, 0]">
        <TresCylinderGeometry :args="[0.56, 0.56, 0.06, 18]" />
        <TresMeshStandardMaterial color="#000" />
      </TresMesh>
      <TresMesh :position="[0, 2.2, 0]">
        <TresCylinderGeometry :args="[0.56, 0.56, 0.06, 18]" />
        <TresMeshStandardMaterial color="#000" />
      </TresMesh>
      <TresMesh :position="[0, 2.8, 0]">
        <TresSphereGeometry :args="[0.55, 18, 12, 0, PI * 2, 0, PI / 2]" />
        <TresMeshStandardMaterial color="#a89570" />
      </TresMesh>
    </TresGroup>

    <TresGroup :position="[0.5, 0, 0]">
      <TresMesh :position="[0, 0.95, 0]">
        <TresBoxGeometry :args="[2, 1.9, 2.2]" />
        <TresMeshStandardMaterial color="#c84d44" />
      </TresMesh>
      <TresMesh :position="[0, 2.25, 0]">
        <TresConeGeometry :args="[1.2, 0.9, 4]" />
        <TresMeshStandardMaterial color="#5a2421" />
      </TresMesh>
      <TresMesh :position="[0, 0.55, 1.11]">
        <TresBoxGeometry :args="[0.7, 1.0, 0.05]" />
        <TresMeshStandardMaterial color="#3a2222" />
      </TresMesh>
    </TresGroup>

    <primitive :object="labels.rwa" />
  </TresGroup>

  <!-- EMPTY PLOT -->
  <TresGroup :position="[9, 0, 0]">
    <TresMesh :position="[0, 0.6, 0]">
      <TresBoxGeometry :args="[2.6, 1.2, 2.4]" />
      <TresMeshBasicMaterial color="#475569" :wireframe="true" :transparent="true" :opacity="0.55" />
    </TresMesh>
    <TresMesh :position="[0, 0.5, 0.6]">
      <TresBoxGeometry :args="[0.06, 1, 0.06]" />
      <TresMeshStandardMaterial color="#92400e" />
    </TresMesh>
    <primitive :object="labels.deploy" />
  </TresGroup>

  <!-- TRADERS (T badge) -->
  <TresGroup
    v-for="(p, i) in traderPositions"
    :key="`trader-${i}`"
    :position="p"
  >
    <TresMesh :position="[0, 0.5, 0]">
      <TresCapsuleGeometry :args="[0.25, 0.55, 6, 12]" />
      <TresMeshStandardMaterial color="#1f8a64" />
    </TresMesh>
    <TresMesh :position="[0, 1.05, 0]">
      <TresSphereGeometry :args="[0.18, 16, 16]" />
      <TresMeshStandardMaterial color="#f4d2a8" />
    </TresMesh>
    <TresMesh :position="[0.32, 0.45, 0]">
      <TresBoxGeometry :args="[0.18, 0.14, 0.1]" />
      <TresMeshStandardMaterial color="#d4a017" />
    </TresMesh>
    <TresSprite :position="[0, 1.85, 0]" :scale="[0.7, 0.7, 1]">
      <TresSpriteMaterial :map="badgeTextures.T" :transparent="true" :depth-test="false" />
    </TresSprite>
  </TresGroup>

  <!-- HACKERS (H badge) -->
  <TresGroup
    v-for="(p, i) in hackerPositions"
    :key="`hacker-${i}`"
    :position="p"
  >
    <TresMesh :position="[0, 0.5, 0]">
      <TresCapsuleGeometry :args="[0.25, 0.55, 6, 12]" />
      <TresMeshStandardMaterial color="#c63a3a" />
    </TresMesh>
    <TresMesh :position="[0, 1.0, 0]">
      <TresConeGeometry :args="[0.28, 0.5, 12]" />
      <TresMeshStandardMaterial color="#8b1a1a" />
    </TresMesh>
    <TresMesh :position="[0, 0.95, 0.18]">
      <TresSphereGeometry :args="[0.13, 12, 12]" />
      <TresMeshBasicMaterial color="#1a0a0a" />
    </TresMesh>
    <TresSprite :position="[0, 1.85, 0]" :scale="[0.7, 0.7, 1]">
      <TresSpriteMaterial :map="badgeTextures.H" :transparent="true" :depth-test="false" />
    </TresSprite>
  </TresGroup>

  <!-- DRONES (V badge) -->
  <TresGroup
    v-for="(p, i) in dronePositions"
    :key="`drone-${i}`"
    :position="p"
    :rotation="droneRotations[i]"
  >
    <TresMesh>
      <TresOctahedronGeometry :args="[0.4, 0]" />
      <TresMeshStandardMaterial color="#3a5fc6" :metalness="0.4" :roughness="0.4" />
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
  </TresGroup>
</template>
