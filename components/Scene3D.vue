<!--
  Scene3D — interactive live 3D for Slidev slides.

  Renders a visually-3d `MachineSceneDescriptor` JSON with Three.js + orbit
  controls, so a slide can carry a real, draggable 3D model. Generate scenes
  with `make scene` (see scripts/scene-generate.mjs) into public/scenes/.

  Usage in a slide:
      <Scene3D src="/scenes/cpu.json" />
      <Scene3D src="/scenes/cpu.json" height="500px" autorotate />

  Props:
    src        URL of a scene JSON under public/ (e.g. "/scenes/cpu.json")
    scene      inline descriptor object (alternative to src)
    height     CSS height of the viewer (default 430px)
    background CSS/hex background color (default #0d1117)
    autorotate slowly spin the model when the user is not dragging
-->
<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js'

const props = defineProps({
  src: { type: String, default: '' },
  scene: { type: Object, default: null },
  height: { type: String, default: '430px' },
  background: { type: String, default: '#0d1117' },
  autorotate: { type: Boolean, default: false },
})

const container = ref(null)
const status = ref('loading')

let renderer, scene3, camera, controls, raf, ro

// --- material mapping (ported from visually-3d Viewer) ----------------------
function materialColor(material, shape) {
  const m = (material || '').toLowerCase()
  if (m.includes('glass') || m.includes('display')) return 0x46b7ff
  if (m.includes('carbon')) return 0x1c2128
  if (m.includes('brass')) return 0xd4a657
  if (m.includes('copper')) return 0xb87333
  if (m.includes('fiberglass')) return 0xe8e8ea
  if (m.includes('concrete')) return 0x6e737b
  if (m.includes('white')) return 0xf0f0f2
  if (m.includes('rubber') || m.includes('black')) return 0x2b2f38
  if (m.includes('anodized')) return 0x3a3d44
  if (m.includes('steel') || m.includes('aluminum') || m.includes('metal') || m.includes('forged'))
    return 0x9ca3af
  return shape === 'complex' ? 0xa855f7 : 0x8b949e
}
function materialPhysical(material) {
  const m = (material || '').toLowerCase()
  if (m.includes('rubber')) return { metalness: 0.0, roughness: 0.95 }
  if (m.includes('glass') || m.includes('display')) return { metalness: 0.15, roughness: 0.15 }
  if (m.includes('carbon')) return { metalness: 0.35, roughness: 0.55 }
  if (m.includes('brass') || m.includes('copper')) return { metalness: 0.9, roughness: 0.35 }
  if (m.includes('brushed')) return { metalness: 0.8, roughness: 0.45 }
  if (m.includes('anodized') || m.includes('aluminum')) return { metalness: 0.7, roughness: 0.4 }
  if (m.includes('steel') || m.includes('forged')) return { metalness: 0.85, roughness: 0.35 }
  if (m.includes('fiberglass')) return { metalness: 0.05, roughness: 0.6 }
  if (m.includes('concrete')) return { metalness: 0.0, roughness: 0.95 }
  if (m.includes('composite')) return { metalness: 0.1, roughness: 0.65 }
  return { metalness: 0.5, roughness: 0.45 }
}

// --- geometry per primitive -------------------------------------------------
function buildGeometry(shape, size) {
  const s = Array.isArray(size) ? size : []
  if (shape === 'cylinder') {
    const [a = 0.5, b = 1, c] = s
    const [rTop, rBot, h] = c !== undefined ? [a, b, c] : [a, a, b]
    return new THREE.CylinderGeometry(rTop, rBot, h, 32)
  }
  if (shape === 'sphere') return new THREE.SphereGeometry(s[0] ?? 0.5, 32, 20)
  if (shape === 'cone') return new THREE.ConeGeometry(s[0] ?? 0.5, s[1] ?? 1, 32)
  if (shape === 'torus') return new THREE.TorusGeometry(s[0] ?? 0.5, s[1] ?? 0.15, 20, 48)
  if (shape === 'capsule') return new THREE.CapsuleGeometry(s[0] ?? 0.3, s[1] ?? 1, 8, 24)
  // box and complex
  const [w = 1, h = 1, d = 1] = s.length >= 3 ? s : [1, 1, 1]
  return new THREE.BoxGeometry(w, h, d)
}

function build(descriptor) {
  const group = new THREE.Group()
  const centers = new Map()
  for (const part of descriptor.parts || []) {
    if (!part || !Array.isArray(part.position)) continue
    const phys = materialPhysical(part.material)
    const mat = new THREE.MeshStandardMaterial({
      color: materialColor(part.material, part.shape),
      metalness: phys.metalness,
      roughness: phys.roughness,
    })
    const mesh = new THREE.Mesh(buildGeometry(part.shape, part.size), mat)
    mesh.castShadow = true
    mesh.receiveShadow = true
    mesh.position.set(part.position[0] || 0, part.position[1] || 0, part.position[2] || 0)
    if (Array.isArray(part.rotation)) {
      mesh.rotation.set(part.rotation[0] || 0, part.rotation[1] || 0, part.rotation[2] || 0)
    }
    group.add(mesh)
    centers.set(part.id, mesh.position.clone())
  }
  // faint connection lines
  const pts = []
  for (const part of descriptor.parts || []) {
    const from = centers.get(part.id)
    if (!from) continue
    for (const to of part.connections || []) {
      const dst = centers.get(to)
      if (dst) { pts.push(from, dst) }
    }
  }
  if (pts.length) {
    const lg = new THREE.BufferGeometry().setFromPoints(pts)
    group.add(new THREE.LineSegments(
      lg,
      new THREE.LineBasicMaterial({ color: 0x4b5563, transparent: true, opacity: 0.4 }),
    ))
  }
  return group
}

function init(descriptor) {
  const el = container.value
  const w = el.clientWidth || 800
  const h = el.clientHeight || 430

  scene3 = new THREE.Scene()
  scene3.background = new THREE.Color(props.background)

  const group = build(descriptor)
  scene3.add(group)

  // fit camera to scene bounds
  const box = new THREE.Box3().setFromObject(group)
  const sphere = box.getBoundingSphere(new THREE.Sphere())
  const center = sphere.center
  const radius = Math.max(sphere.radius, 0.5)

  camera = new THREE.PerspectiveCamera(45, w / h, radius / 100, radius * 100)
  const cam = descriptor.metadata && descriptor.metadata.thumbnail_camera
  if (Array.isArray(cam) && cam.length === 3) {
    camera.position.set(cam[0], cam[1], cam[2])
  } else {
    const d = radius * 1.7
    camera.position.set(center.x + d, center.y + d * 0.7, center.z + d)
  }

  // lighting — soft ambient + a shadow-casting key light
  scene3.add(new THREE.AmbientLight(0xffffff, 0.28))
  scene3.add(new THREE.HemisphereLight(0xbcd3ff, 0x141619, 0.45))
  const key = new THREE.DirectionalLight(0xffffff, 2.6)
  key.position.set(center.x + radius * 1.6, center.y + radius * 2.4, center.z + radius * 1.2)
  key.target.position.copy(center)
  key.castShadow = true
  key.shadow.mapSize.set(2048, 2048)
  key.shadow.camera.near = radius * 0.1
  key.shadow.camera.far = radius * 14
  const sh = radius * 2
  key.shadow.camera.left = -sh
  key.shadow.camera.right = sh
  key.shadow.camera.top = sh
  key.shadow.camera.bottom = -sh
  key.shadow.bias = -0.0006
  key.shadow.radius = 5
  scene3.add(key)
  scene3.add(key.target)
  const fill = new THREE.DirectionalLight(0xa9c3ff, 0.5)
  fill.position.set(center.x - radius * 2, center.y + radius, center.z - radius * 1.6)
  scene3.add(fill)

  // a shadow-catching ground so the model is grounded, not floating
  const ground = new THREE.Mesh(
    new THREE.PlaneGeometry(radius * 40, radius * 40),
    new THREE.ShadowMaterial({ opacity: 0.3 }),
  )
  ground.rotation.x = -Math.PI / 2
  ground.position.set(center.x, box.min.y - radius * 0.01, center.z)
  ground.receiveShadow = true
  scene3.add(ground)

  renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' })
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  renderer.shadowMap.enabled = true
  renderer.shadowMap.type = THREE.PCFSoftShadowMap
  renderer.toneMapping = THREE.ACESFilmicToneMapping
  renderer.toneMappingExposure = 1.05
  // setSize(..., false): do NOT let three write inline px width/height onto the
  // canvas — CSS keeps it at 100% of the container so it can never overflow a
  // grid/flex cell and break the slide layout.
  renderer.setSize(w, h, false)
  el.appendChild(renderer.domElement)

  // image-based lighting — gives metal/glass real reflections instead of a
  // flat, cheap-looking shade.
  const pmrem = new THREE.PMREMGenerator(renderer)
  scene3.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture
  scene3.environmentIntensity = 0.5
  pmrem.dispose()

  controls = new OrbitControls(camera, renderer.domElement)
  controls.target.copy(center)
  controls.enableDamping = true
  controls.dampingFactor = 0.08
  controls.minDistance = radius * 0.5
  controls.maxDistance = radius * 8
  controls.autoRotate = props.autorotate
  controls.autoRotateSpeed = 0.8
  controls.update()

  ro = new ResizeObserver(() => {
    const cw = el.clientWidth, ch = el.clientHeight
    if (!cw || !ch) return
    camera.aspect = cw / ch
    camera.updateProjectionMatrix()
    renderer.setSize(cw, ch, false)
  })
  ro.observe(el)

  const tick = () => {
    raf = requestAnimationFrame(tick)
    controls.update()
    renderer.render(scene3, camera)
  }
  tick()
  status.value = 'ready'
}

async function load() {
  let descriptor = props.scene
  if (!descriptor && props.src) {
    const res = await fetch(props.src)
    if (!res.ok) throw new Error(`fetch ${props.src} → ${res.status}`)
    descriptor = await res.json()
  }
  if (!descriptor || !Array.isArray(descriptor.parts)) {
    throw new Error('no valid scene descriptor (need { parts: [...] })')
  }
  init(descriptor)
}

onMounted(() => {
  load().catch((e) => {
    status.value = 'error'
    console.error('[Scene3D]', e)
  })
})

onBeforeUnmount(() => {
  if (raf) cancelAnimationFrame(raf)
  if (ro) ro.disconnect()
  if (controls) controls.dispose()
  if (renderer) {
    renderer.dispose()
    renderer.domElement.remove()
  }
  if (scene3) {
    scene3.traverse((o) => {
      if (o.geometry) o.geometry.dispose()
      if (o.material) (Array.isArray(o.material) ? o.material : [o.material]).forEach((m) => m.dispose())
    })
  }
})
</script>

<template>
  <div ref="container" class="scene3d" :style="{ height }">
    <div v-if="status === 'loading'" class="scene3d__msg">Loading 3D scene…</div>
    <div v-else-if="status === 'error'" class="scene3d__msg">3D scene failed to load</div>
  </div>
</template>

<style scoped>
.scene3d {
  position: relative;
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
  background: #0d1117;
}
.scene3d :deep(canvas) {
  display: block;
  position: absolute;
  inset: 0;
  width: 100% !important;
  height: 100% !important;
  cursor: grab;
}
.scene3d :deep(canvas):active {
  cursor: grabbing;
}
.scene3d__msg {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #8b949e;
  font-size: 0.85rem;
}
</style>
