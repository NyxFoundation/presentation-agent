/*
 * storm/engine.js — the two storm metaphors, hand-coded in Three.js.
 *
 *   house   a cosy house whose key is trivially copied, with thieves
 *           creeping in from every route        (嵐①② — 鍵 / 攻撃)
 *   bridge  a normal-looking, working suspension bridge that quietly
 *           sways — it looks fine, but it is fragile — with the wealth
 *           on it piled onto one side            (嵐③④ — 正しさ / 偏り)
 *
 * Embedded as panels from public/storm/index.html?v=<variant>.
 */
import * as THREE from 'three'
import { OrbitControls } from 'three/addons/controls/OrbitControls.js'
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js'
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js'
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js'
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js'

const SETTINGS = {
  house: {
    sky: { top: 0x46699e, mid: 0xa6bcd2, hor: 0xe4d9c4, sun: 0xffe9cf },
    sunPos: [16, 17, 13], sunColor: 0xfff0d8, sunInt: 2.4,
    ambient: 0x4a5060, ambientInt: 0.5, hemiSky: 0xc4d2e4, hemiGround: 0x3c382c, hemiInt: 0.6,
    fog: 0xdfe4e4, fogNear: 55, fogFar: 150, exposure: 1.0,
    camera: [16.5, 11, 19.5], target: [0, 3, -0.5],
    bloom: { strength: 0.22, radius: 0.5, threshold: 0.85 },
  },
  bridge: {
    sky: { top: 0x3b7ac4, mid: 0x91bbe4, hor: 0xe1ecf2, sun: 0xfff3da },
    sunPos: [22, 24, 14], sunColor: 0xfff2da, sunInt: 3.0,
    ambient: 0x4c5a70, ambientInt: 0.62, hemiSky: 0xbed8f5, hemiGround: 0x33302a, hemiInt: 0.72,
    fog: 0xd2dfeb, fogNear: 46, fogFar: 150, exposure: 1.05,
    camera: [27, 15, 32], target: [0, 6.5, 0],
    bloom: { strength: 0.36, radius: 0.5, threshold: 0.74 },
  },
}

function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6d2b79f5) | 0
    let t = Math.imul(a ^ (a >>> 15), 1 | a)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}
const mat = (color, o = {}) => new THREE.MeshStandardMaterial({
  color, roughness: o.roughness ?? 0.8, metalness: o.metalness ?? 0.05,
  emissive: o.emissive ?? 0x000000, emissiveIntensity: o.emissiveIntensity ?? 1,
  transparent: o.transparent ?? false, opacity: o.opacity ?? 1,
})
const box = (w, h, d, m) => new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m)
const cyl = (rt, rb, h, m, seg = 20) => new THREE.Mesh(new THREE.CylinderGeometry(rt, rb, h, seg), m)
const sph = (r, m) => new THREE.Mesh(new THREE.SphereGeometry(r, 24, 16), m)

const _UP = new THREE.Vector3(0, 1, 0)
const _d = new THREE.Vector3()
function spanCyl(mesh, ax, ay, az, bx, by, bz) {
  _d.set(bx - ax, by - ay, bz - az)
  const len = _d.length() || 0.0001
  mesh.position.set((ax + bx) / 2, (ay + by) / 2, (az + bz) / 2)
  mesh.scale.y = len
  mesh.quaternion.setFromUnitVectors(_UP, _d.normalize())
}

// ==========================================================================
export function startStorm(canvas, variant) {
  const S = SETTINGS[variant] || SETTINGS.house
  const rng = mulberry32(variant === 'bridge' ? 0x7c8133 : 0x4f2a91)
  const rr = (a, b) => a + (b - a) * rng()

  let W = window.innerWidth || 640
  let H = window.innerHeight || 360

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true })
  renderer.setSize(W, H, false)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  renderer.shadowMap.enabled = true
  renderer.shadowMap.type = THREE.PCFSoftShadowMap
  renderer.toneMapping = THREE.ACESFilmicToneMapping
  renderer.toneMappingExposure = S.exposure
  renderer.outputColorSpace = THREE.SRGBColorSpace

  const scene = new THREE.Scene()
  scene.fog = new THREE.Fog(S.fog, S.fogNear, S.fogFar)

  const camera = new THREE.PerspectiveCamera(38, W / H, 0.3, 600)
  camera.position.set(...S.camera)

  // ---- sky + image-based light --------------------------------------------
  function skyMat() {
    return new THREE.ShaderMaterial({
      side: THREE.BackSide, depthWrite: false, fog: false,
      uniforms: {
        cTop: { value: new THREE.Color(S.sky.top) },
        cMid: { value: new THREE.Color(S.sky.mid) },
        cHor: { value: new THREE.Color(S.sky.hor) },
        cSun: { value: new THREE.Color(S.sky.sun) },
        sunDir: { value: new THREE.Vector3(...S.sunPos).normalize() },
      },
      vertexShader: `varying vec3 vD;
        void main(){ vD = position; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }`,
      fragmentShader: `
        uniform vec3 cTop,cMid,cHor,cSun,sunDir; varying vec3 vD;
        void main(){
          vec3 d = normalize(vD); float y = d.y;
          vec3 col = mix(cHor, cMid, smoothstep(-0.05, 0.3, y));
          col = mix(col, cTop, smoothstep(0.22, 0.82, y));
          float s = max(dot(d, normalize(sunDir)), 0.0);
          col += cSun * pow(s, 6.0) * 0.7 + cSun * pow(s, 120.0) * 1.3;
          gl_FragColor = vec4(col, 1.0);
        }`,
    })
  }
  scene.add(new THREE.Mesh(new THREE.SphereGeometry(320, 32, 20), skyMat()))
  const pmrem = new THREE.PMREMGenerator(renderer)
  const envScene = new THREE.Scene()
  envScene.add(new THREE.Mesh(new THREE.SphereGeometry(30, 20, 12), skyMat()))
  scene.environment = pmrem.fromScene(envScene, 0.45).texture

  // ---- lighting ------------------------------------------------------------
  scene.add(new THREE.AmbientLight(S.ambient, S.ambientInt))
  scene.add(new THREE.HemisphereLight(S.hemiSky, S.hemiGround, S.hemiInt))
  const sun = new THREE.DirectionalLight(S.sunColor, S.sunInt)
  sun.position.set(...S.sunPos)
  sun.castShadow = true
  sun.shadow.mapSize.set(2048, 2048)
  sun.shadow.camera.near = 1
  sun.shadow.camera.far = 140
  const sb = variant === 'bridge' ? 34 : 18
  sun.shadow.camera.left = -sb; sun.shadow.camera.right = sb
  sun.shadow.camera.top = sb; sun.shadow.camera.bottom = -sb
  sun.shadow.bias = -0.0006
  sun.shadow.normalBias = 0.03
  scene.add(sun)

  const updaters = []
  if (variant === 'bridge') buildBridge(scene, rng, rr, updaters)
  else buildHouse(scene, rng, rr, updaters)

  // ---- controls ------------------------------------------------------------
  const controls = new OrbitControls(camera, renderer.domElement)
  controls.enableDamping = true
  controls.dampingFactor = 0.07
  controls.target.set(...S.target)
  controls.minDistance = variant === 'bridge' ? 22 : 13
  controls.maxDistance = variant === 'bridge' ? 70 : 40
  controls.minPolarAngle = 0.25
  controls.maxPolarAngle = 1.42
  controls.autoRotate = true
  controls.autoRotateSpeed = 0.5
  controls.update()

  // ---- post ----------------------------------------------------------------
  const composer = new EffectComposer(renderer)
  composer.addPass(new RenderPass(scene, camera))
  composer.addPass(new UnrealBloomPass(
    new THREE.Vector2(W, H), S.bloom.strength, S.bloom.radius, S.bloom.threshold))
  composer.addPass(new OutputPass())
  composer.setSize(W, H)

  function resize() {
    W = window.innerWidth; H = window.innerHeight
    camera.aspect = W / H
    camera.updateProjectionMatrix()
    renderer.setSize(W, H, false)
    composer.setSize(W, H)
  }
  window.addEventListener('resize', resize)

  let raf = 0, prev = performance.now()
  function tick() {
    raf = requestAnimationFrame(tick)
    const now = performance.now()
    const dt = Math.min((now - prev) / 1000, 0.05)
    prev = now
    const t = now / 1000
    controls.update()
    for (const u of updaters) u(t, dt)
    composer.render()
  }
  tick()

  return {
    dispose() {
      cancelAnimationFrame(raf)
      window.removeEventListener('resize', resize)
      controls.dispose()
      renderer.dispose()
    },
  }
}

// ============================================================ HOUSE =========
function buildHouse(scene, rng, rr, updaters) {
  // --- ground: grass + a path to the door ---
  const grass = new THREE.Mesh(new THREE.CircleGeometry(26, 48), mat(0x6f8246, { roughness: 1 }))
  grass.rotation.x = -Math.PI / 2
  grass.receiveShadow = true
  scene.add(grass)
  const plot = box(15, 0.1, 15, mat(0x76874e, { roughness: 1 }))
  plot.position.y = 0.05
  plot.receiveShadow = true
  scene.add(plot)
  const path = box(2.2, 0.12, 5.6, mat(0xc9b48c, { roughness: 0.95 }))
  path.position.set(0, 0.12, 5.4)
  path.receiveShadow = true
  scene.add(path)

  // --- house body ---
  const house = new THREE.Group()
  scene.add(house)
  const wallMat = mat(0xd9c6a4, { roughness: 0.85 })
  const body = box(6.4, 3.6, 5.4, wallMat)
  body.position.y = 1.85
  body.castShadow = true; body.receiveShadow = true
  house.add(body)

  // pitched roof — one solid prism: clean ridge, wall-coloured gables
  const roofMat = mat(0x9c4f3b, { roughness: 0.78 })
  const roofShape = new THREE.Shape()
  roofShape.moveTo(-3.62, 0)
  roofShape.lineTo(3.62, 0)
  roofShape.lineTo(0, 2.05)
  roofShape.closePath()
  const roofDepth = 6.2
  const roofGeo = new THREE.ExtrudeGeometry(roofShape, { depth: roofDepth, bevelEnabled: false })
  roofGeo.translate(0, 0, -roofDepth / 2)
  const roof = new THREE.Mesh(roofGeo, [wallMat, roofMat])
  roof.position.y = 3.65
  roof.castShadow = true; roof.receiveShadow = true
  house.add(roof)
  const chimney = box(0.72, 1.7, 0.72, mat(0x8a5847, { roughness: 0.9 }))
  chimney.position.set(1.7, 5.0, -1.0)
  chimney.castShadow = true
  house.add(chimney)

  // door + lock
  const door = box(1.4, 2.55, 0.18, mat(0x5f4128, { roughness: 0.7 }))
  door.position.set(0, 1.28, 2.78)
  door.castShadow = true
  house.add(door)
  const knob = sph(0.12, mat(0xd8b24a, { metalness: 0.9, roughness: 0.3 }))
  knob.position.set(0.48, 1.3, 2.9)
  house.add(knob)

  // windows — warm, lit (someone is home; evening tension)
  const glassMat = mat(0x4a3a22, { emissive: 0xffce7a, emissiveIntensity: 0.55, roughness: 0.4 })
  const frameMat = mat(0xf2ead8, { roughness: 0.7 })
  function window2(x, y, z, ry) {
    const g = new THREE.Group()
    g.position.set(x, y, z); g.rotation.y = ry
    const f = box(1.34, 1.34, 0.14, frameMat); g.add(f)
    const gl = box(1.04, 1.04, 0.1, glassMat); gl.position.z = 0.04; g.add(gl)
    const bar1 = box(0.08, 1.04, 0.12, frameMat); bar1.position.z = 0.05; g.add(bar1)
    const bar2 = box(1.04, 0.08, 0.12, frameMat); bar2.position.z = 0.05; g.add(bar2)
    house.add(g)
  }
  window2(-2.1, 2.15, 2.72, 0)
  window2(2.1, 2.15, 2.72, 0)
  window2(-3.22, 2.15, -0.6, -Math.PI / 2)
  window2(3.22, 2.15, 0.8, Math.PI / 2)
  window2(0, 2.15, -2.72, Math.PI)

  // --- low fence with an open gate (it is not really secured) ---
  const fenceMat = mat(0xb9a888, { roughness: 0.9 })
  const FN = 7.1
  function post(x, z) {
    const p = box(0.22, 1.4, 0.22, fenceMat)
    p.position.set(x, 0.7, z); p.castShadow = true
    scene.add(p)
  }
  function rail(x, z, len, horiz) {
    for (const y of [0.55, 1.05]) {
      const r = box(horiz ? len : 0.1, 0.1, horiz ? 0.1 : len, fenceMat)
      r.position.set(x, y, z)
      scene.add(r)
    }
  }
  for (let i = -FN; i <= FN; i += 1.7) {
    post(i, -FN); post(i, FN)
    post(-FN, i); post(FN, i)
  }
  rail(0, -FN, FN * 2, true)
  rail(-FN, 0, FN * 2, false); rail(FN, 0, FN * 2, false)
  rail(-FN / 2 - 0.7, FN, FN - 1.4, true) // front rails leave a gap for the gate
  rail(FN / 2 + 0.7, FN, FN - 1.4, true)
  // the gate itself — swung wide open
  const gate = new THREE.Group()
  gate.position.set(-1.4, 0, FN)
  const gpost = box(0.16, 1.2, 0.16, fenceMat)
  for (const gy of [0.5, 0.95]) {
    const gr = box(2.6, 0.09, 0.09, fenceMat); gr.position.set(1.3, gy, 0); gate.add(gr)
  }
  for (let gx = 0; gx <= 2.6; gx += 0.65) {
    const gp = box(0.09, 1.1, 0.09, fenceMat); gp.position.set(gx, 0.7, 0); gate.add(gp)
  }
  void gpost
  gate.rotation.y = -1.15
  scene.add(gate)

  // --- the key, and the copies that keep peeling off it ---
  function makeKey(goldMat) {
    const k = new THREE.Group()
    const bow = new THREE.Mesh(new THREE.TorusGeometry(0.34, 0.11, 12, 26), goldMat)
    bow.rotation.y = Math.PI / 2
    bow.position.x = -0.62
    k.add(bow)
    const shaft = cyl(0.085, 0.085, 1.15, goldMat, 14)
    shaft.rotation.z = Math.PI / 2
    k.add(shaft)
    for (const tx of [0.34, 0.52]) {
      const tooth = box(0.12, 0.26, 0.12, goldMat)
      tooth.position.set(tx, -0.2, 0)
      k.add(tooth)
    }
    return k
  }
  const goldMat = mat(0xe7b53e, { metalness: 0.95, roughness: 0.26, emissive: 0xc8861a, emissiveIntensity: 0.45 })
  const hero = makeKey(goldMat)
  const heroPos = new THREE.Vector3(2.7, 3.3, 4.1)
  hero.position.copy(heroPos)
  hero.castShadow = true
  scene.add(hero)

  const copies = []
  for (let i = 0; i < 5; i++) {
    const cm = mat(0xe7b53e, {
      metalness: 0.9, roughness: 0.3, emissive: 0xc8861a, emissiveIntensity: 0.5,
      transparent: true, opacity: 0.5,
    })
    const k = makeKey(cm)
    const ang = (i / 5) * Math.PI * 2 + 0.4
    k.userData = {
      mat: cm,
      dir: new THREE.Vector3(Math.cos(ang) * 1.3, rr(-0.2, 0.7), Math.sin(ang) * 1.3).normalize(),
      phase: i / 5,
    }
    scene.add(k)
    copies.push(k)
  }

  // --- thieves creeping in from every route ---
  const thieves = []
  const darkMat = mat(0x282830, { roughness: 0.85 })
  const angs = [Math.PI * 0.5, Math.PI * 0.85, Math.PI * 1.15, Math.PI * 1.55, Math.PI * 1.9]
  for (let i = 0; i < angs.length; i++) {
    const th = new THREE.Group()
    const bodyM = new THREE.Mesh(new THREE.CapsuleGeometry(0.32, 0.86, 6, 14), darkMat)
    bodyM.position.y = 0.83; bodyM.castShadow = true
    th.add(bodyM)
    const head = sph(0.27, darkMat); head.position.y = 1.56; head.castShadow = true
    th.add(head)
    const brim = cyl(0.44, 0.44, 0.06, darkMat, 16); brim.position.y = 1.74
    th.add(brim)
    const crown = cyl(0.27, 0.29, 0.32, darkMat, 16); crown.position.y = 1.92
    th.add(crown)
    const sack = sph(0.34, darkMat); sack.position.set(0.42, 1.2, -0.16); sack.scale.set(1, 0.85, 1)
    sack.castShadow = true
    th.add(sack)
    th.userData = { ang: angs[i], speed: rr(0.05, 0.085), phase: rng() }
    scene.add(th)
    thieves.push(th)
  }

  updaters.push((t) => {
    hero.position.y = heroPos.y + Math.sin(t * 1.6) * 0.12
    hero.rotation.y = t * 0.5
    for (const k of copies) {
      const p = ((t * 0.32 + k.userData.phase) % 1)
      k.position.copy(heroPos).addScaledVector(k.userData.dir, 0.4 + p * 3.4)
      k.rotation.y = t * 0.5 + k.userData.phase * 6
      k.rotation.z = p * 1.4
      k.userData.mat.opacity = Math.max(0, 0.6 * (1 - p) - 0.05)
      const s = 1 - p * 0.35
      k.scale.setScalar(s)
    }
    for (const th of thieves) {
      const p = ((t * th.userData.speed + th.userData.phase) % 1)
      const r = 9.2 - p * 4.9
      const a = th.userData.ang
      th.position.set(Math.cos(a) * r, Math.abs(Math.sin(t * 7 + th.userData.phase * 9)) * 0.07, Math.sin(a) * r)
      th.rotation.y = -a + Math.PI / 2
    }
  })
}

// ============================================================ BRIDGE ========
function buildBridge(scene, rng, rr, updaters) {
  // --- water + two banks, a gap spanned by the bridge ---
  const water = new THREE.Mesh(new THREE.PlaneGeometry(220, 160),
    new THREE.MeshStandardMaterial({
      color: 0x35699a, roughness: 0.12, metalness: 0.6,
      envMapIntensity: 1.4, emissive: 0x10314f, emissiveIntensity: 0.3,
    }))
  water.rotation.x = -Math.PI / 2
  water.receiveShadow = true
  scene.add(water)

  const bankMat = mat(0x5d6f3f, { roughness: 1 })
  const cliffMat = mat(0x6b6256, { roughness: 1 })
  for (const side of [-1, 1]) {
    const bank = box(26, 4.7, 40, bankMat)
    bank.position.set(side * 28, 2.35, 0)
    bank.castShadow = true; bank.receiveShadow = true
    scene.add(bank)
    const cliff = box(4, 4.7, 40, cliffMat)
    cliff.position.set(side * 15.2, 2.35, 0)
    cliff.castShadow = true; cliff.receiveShadow = true
    scene.add(cliff)
  }

  const DECK_Y = 5.0
  const TOWER_X = 9
  const TOWER_TOP = 13.6
  const cableMat = mat(0x95a0ad, { metalness: 0.7, roughness: 0.4 })
  const steelMat = mat(0x8f99a6, { metalness: 0.55, roughness: 0.5 })
  const deckMat = mat(0x6a7079, { roughness: 0.82 })

  // --- two towers (slim — an early hint that this is under-built) ---
  for (const side of [-1, 1]) {
    const tower = new THREE.Group()
    tower.position.x = side * TOWER_X
    for (const z of [-2.6, 2.6]) {
      const leg = box(0.62, TOWER_TOP, 0.62, steelMat)
      leg.position.set(0, TOWER_TOP / 2, z)
      leg.castShadow = true
      tower.add(leg)
    }
    for (const y of [3.6, DECK_Y + 0.4, 9.0, TOWER_TOP - 0.4]) {
      const brace = box(0.42, 0.42, 5.2, steelMat)
      brace.position.set(0, y, 0)
      brace.castShadow = true
      tower.add(brace)
    }
    // hairline cracks on the right tower's leg — looks fine, but it is not
    if (side === 1) {
      for (let c = 0; c < 5; c++) {
        const crack = box(0.07, rr(0.5, 1.3), 0.66, mat(0x1c1c22, { roughness: 1 }))
        crack.position.set(0.30, rr(2, 9), 2.6)
        crack.rotation.z = rr(-0.5, 0.5)
        tower.add(crack)
      }
    }
    tower.userData = { side }
    scene.add(tower)
    updaters.push((t) => { tower.rotation.z = Math.sin(t * 0.9 + side) * 0.012 })
  }

  // --- deck: many short segments so it can visibly flex ---
  const deck = new THREE.Group()
  scene.add(deck)
  const segs = []
  const SEG_N = 30, SEG_W = 1.0
  const X0 = -15
  for (let i = 0; i < SEG_N; i++) {
    const x = X0 + i * SEG_W + SEG_W / 2
    const seg = new THREE.Group()
    seg.position.set(x, DECK_Y, 0)
    const slab = box(SEG_W + 0.04, 0.34, 6.0, deckMat)
    slab.castShadow = true; slab.receiveShadow = true
    seg.add(slab)
    for (const z of [-2.9, 2.9]) {
      const curb = box(SEG_W + 0.04, 0.4, 0.22, steelMat)
      curb.position.set(0, 0.36, z)
      seg.add(curb)
    }
    seg.userData = { x, base: DECK_Y }
    deck.add(seg)
    segs.push(seg)
  }

  // --- main cables + hangers ---
  // cable height across the main span (a parabola between the towers)
  const yMid = 7.6
  const cableY = (x) => {
    if (Math.abs(x) <= TOWER_X) return yMid + (TOWER_TOP - yMid) * (x / TOWER_X) ** 2
    // side spans run straight from tower top down to the deck anchor
    const t = (Math.abs(x) - TOWER_X) / (15 - TOWER_X)
    return TOWER_TOP + (DECK_Y + 0.4 - TOWER_TOP) * t
  }
  for (const z of [-2.7, 2.7]) {
    const pts = []
    for (let x = -15; x <= 15.001; x += 0.6) pts.push(new THREE.Vector3(x, cableY(x), z))
    const curve = new THREE.CatmullRomCurve3(pts)
    const tube = new THREE.Mesh(new THREE.TubeGeometry(curve, 64, 0.13, 8, false), cableMat)
    tube.castShadow = true
    scene.add(tube)
  }
  // hangers — thin verticals, updated each frame so they track the flex
  const hangers = []
  for (const z of [-2.7, 2.7]) {
    for (let x = -TOWER_X + 1.0; x <= TOWER_X - 0.9; x += 1.5) {
      const h = cyl(0.045, 0.045, 1, cableMat, 6)
      h.userData = { x, z, topY: cableY(x) }
      scene.add(h)
      hangers.push(h)
    }
  }

  // --- the value on the bridge — almost all of it piled on one side ---
  const coinMat = mat(0xe7b53e, { metalness: 0.95, roughness: 0.28, emissive: 0xc8861a, emissiveIntensity: 0.4 })
  function coinStack(seg, ox, oz, n) {
    const stack = new THREE.Group()
    stack.position.set(ox, 0.215, oz)
    for (let c = 0; c < n; c++) {
      const coin = cyl(0.44, 0.44, 0.09, coinMat, 22)
      coin.position.y = c * 0.095
      coin.rotation.y = rng() * 3
      coin.castShadow = true
      stack.add(coin)
    }
    seg.add(stack)
  }
  const segAt = (x) => segs[Math.max(0, Math.min(SEG_N - 1, Math.round((x - X0 - SEG_W / 2) / SEG_W)))]
  // a heavy hoard crowded onto the right third of the deck
  for (let k = 0; k < 11; k++) {
    const x = rr(3.5, 12.5)
    coinStack(segAt(x), 0, rr(-1.9, 1.9), Math.round(rr(6, 15)))
  }
  // ...and almost nothing on the rest of it
  coinStack(segAt(-8.5), 0, -1.2, 2)
  coinStack(segAt(-3), 0, 1.4, 1)

  // --- flex: it carries traffic, it looks fine — and it never stops moving ---
  updaters.push((t) => {
    for (let i = 0; i < segs.length; i++) {
      const seg = segs[i]
      const wave = Math.sin(t * 1.5 + i * 0.42) * 0.17 + Math.sin(t * 0.7 + i * 0.18) * 0.07
      seg.position.y = seg.userData.base + wave
      seg.rotation.x = Math.sin(t * 1.3 + i * 0.42) * 0.035 // a slow torsional roll
    }
    for (const h of hangers) {
      const seg = segAt(h.userData.x)
      const wave = Math.sin(t * 1.5 + (segs.indexOf(seg)) * 0.42) * 0.17
        + Math.sin(t * 0.7 + segs.indexOf(seg) * 0.18) * 0.07
      spanCyl(h, h.userData.x, h.userData.topY, h.userData.z,
        h.userData.x, DECK_Y + 0.18 + wave, h.userData.z)
    }
  })
}
