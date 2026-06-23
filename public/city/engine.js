/*
 * city/engine.js — one deterministic city, three skins.
 *
 * A single seeded generator lays out an identical city (streets, river,
 * bridges, ~55 buildings, parks, cars). The `variant` only changes the
 * skin — materials, sky, light, post — so the three slides are visibly
 * the same town seen three ways:
 *
 *   base       a clear-day stylized cityscape (anime-background look)
 *   invisible  the same city as a Matrix-green wireframe silhouette
 *   ethereum   the same city, futuristic — cyan/violet neon glass
 *
 * Used full-bleed from public/city/index.html?v=<variant>.
 */
import * as THREE from 'three'
import { OrbitControls } from 'three/addons/controls/OrbitControls.js'
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js'
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js'
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js'
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js'

// ----------------------------------------------------------------- palettes
const PALETTES = {
  base: {
    sky: { top: 0x2a68bf, mid: 0x7db2e4, hor: 0xe7eff4, sun: 0xfff4dd },
    sunPos: [80, 70, -40], sunColor: 0xfff2da, sunInt: 3.1,
    ambient: 0x4a5c74, ambientInt: 0.6,
    hemiSky: 0xbcd6f4, hemiGround: 0x3a382e, hemiInt: 0.78,
    fog: 0xdbe6ee, fogNear: 115, fogFar: 330, exposure: 1.05,
    ground: 0x2c3340, lot: 0x6d7585, grass: 0x5c8a4a,
    facade: [0xeef1f4, 0xdfe4ea, 0xe7e2d6, 0xd4dae1, 0xc7d2dd],
    fac: { bg: '#c4ccd5', win: '#586d86', lit: '#ffe6b4' },
    windowGlow: 0xffe6b0, windowLit: 0.5, litRatio: 0.11,
    river: 0x3f7fae, riverGlow: 0x14304a,
    edges: null, edgeInt: 0,
    car: 0xfff0c8, carTail: 0xff6b4a, tree: 0x4f8a3e,
    bloom: { strength: 0.42, radius: 0.55, threshold: 0.78 },
    stars: 0, rain: 0, grid: 0,
  },
  invisible: {
    sky: { top: 0x000000, mid: 0x011006, hor: 0x021c0d, sun: 0x000000 },
    sunPos: [80, 64, -46], sunColor: 0x1c5a2c, sunInt: 0.45,
    ambient: 0x021a09, ambientInt: 0.5,
    hemiSky: 0x04340f, hemiGround: 0x000000, hemiInt: 0.4,
    fog: 0x010d05, fogNear: 70, fogFar: 360, exposure: 1.0,
    ground: 0x010402, lot: 0x020c05, grass: 0x041a0a,
    facade: [0x010503, 0x010503, 0x010503, 0x010503, 0x010503],
    fac: { bg: '#010503', win: '#010503', lit: '#39ff84' },
    windowGlow: 0x39ff84, windowLit: 1.5, litRatio: 0.28,
    river: 0x021c0c, riverGlow: 0x0c5224,
    edges: 0x39ff7e, edgeInt: 0.82,
    car: 0x82ffb4, carTail: 0x39ff7e, tree: 0x063318,
    bloom: { strength: 0.44, radius: 0.42, threshold: 0.0 },
    stars: 0, rain: 0x39ff7e, grid: 0x0a4a22,
  },
  ethereum: {
    sky: { top: 0x05030f, mid: 0x0c0a2c, hor: 0x3a2370, sun: 0x5566ff },
    sunPos: [-66, 58, -36], sunColor: 0x8a96ff, sunInt: 1.25,
    ambient: 0x171b3e, ambientInt: 0.6,
    hemiSky: 0x3a3f86, hemiGround: 0x070518, hemiInt: 0.55,
    fog: 0x0a0824, fogNear: 70, fogFar: 250, exposure: 1.06,
    ground: 0x070620, lot: 0x121238, grass: 0x14305a,
    facade: [0x0c1438, 0x101a44, 0x0a1030, 0x141d4e, 0x0c1a40],
    fac: { bg: '#11183e', win: '#0a0e26', lit: '#84ecff' },
    windowGlow: 0x6fe8ff, windowLit: 0.72, litRatio: 0.34,
    river: 0x1c2f9a, riverGlow: 0x2440d0,
    edges: 0x57c8ff, edgeInt: 0.8,
    car: 0x9af3ff, carTail: 0xb98cff, tree: 0x2f6f9a,
    bloom: { strength: 0.52, radius: 0.55, threshold: 0.6 },
    stars: 0x9fb4ff, rain: 0, grid: 0, agents: true,
  },
}

// --------------------------------------------------------------- seeded rng
function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6d2b79f5) | 0
    let t = Math.imul(a ^ (a >>> 15), 1 | a)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

// ---------------------------------------------------- procedural facade map
// Returns { map, emit }: `map` is the daylight facade (concrete + window
// grid), `emit` is black except for the windows that are lit and glow.
function makeFacade(rng, P) {
  const cols = 4, rows = 10, mx = 6, my = 5
  const cw = (64 - mx * 2) / cols, ch = (128 - my * 2) / rows
  const mk = () => {
    const c = document.createElement('canvas')
    c.width = 64; c.height = 128
    return [c, c.getContext('2d')]
  }
  const [fc, fx] = mk()
  const [ec, ex] = mk()
  fx.fillStyle = P.fac.bg; fx.fillRect(0, 0, 64, 128)
  ex.fillStyle = '#000000'; ex.fillRect(0, 0, 64, 128)
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const lit = rng() < P.litRatio
      const px = mx + c * cw + 1.2, py = my + r * ch + 1.2
      const pw = cw - 2.4, ph = ch - 2.4
      fx.fillStyle = lit ? P.fac.lit : P.fac.win
      fx.fillRect(px, py, pw, ph)
      if (lit) {
        ex.fillStyle = P.fac.lit
        ex.fillRect(px, py, pw, ph)
      }
    }
  }
  const tex = (c) => {
    const t = new THREE.CanvasTexture(c)
    t.wrapS = t.wrapT = THREE.RepeatWrapping
    t.colorSpace = THREE.SRGBColorSpace
    return t
  }
  return { map: tex(fc), emit: tex(ec) }
}

// ================================================================== city
export function startCity(canvas, variant) {
  const P = PALETTES[variant] || PALETTES.base
  const rng = mulberry32(0x9c1a73) // fixed seed → identical layout per variant
  const rr = (a, b) => a + (b - a) * rng()
  const ri = (a, b) => Math.floor(rr(a, b + 0.999))

  let W = window.innerWidth || 1280
  let H = window.innerHeight || 720

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true })
  renderer.setSize(W, H, false)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  renderer.shadowMap.enabled = true
  renderer.shadowMap.type = THREE.PCFSoftShadowMap
  renderer.toneMapping = THREE.ACESFilmicToneMapping
  renderer.toneMappingExposure = P.exposure
  renderer.outputColorSpace = THREE.SRGBColorSpace

  const scene = new THREE.Scene()
  scene.fog = new THREE.Fog(P.fog, P.fogNear, P.fogFar)

  const camera = new THREE.PerspectiveCamera(34, W / H, 0.5, 900)
  camera.position.set(74, 50, 94)

  // ---- sky dome ------------------------------------------------------------
  function skyMaterial() {
    return new THREE.ShaderMaterial({
      side: THREE.BackSide, depthWrite: false, fog: false,
      uniforms: {
        cTop: { value: new THREE.Color(P.sky.top) },
        cMid: { value: new THREE.Color(P.sky.mid) },
        cHor: { value: new THREE.Color(P.sky.hor) },
        cSun: { value: new THREE.Color(P.sky.sun) },
        sunDir: { value: new THREE.Vector3(...P.sunPos).normalize() },
      },
      vertexShader: `varying vec3 vD;
        void main(){ vD = position; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }`,
      fragmentShader: `
        uniform vec3 cTop,cMid,cHor,cSun,sunDir; varying vec3 vD;
        void main(){
          vec3 d = normalize(vD); float y = d.y;
          vec3 col = mix(cHor, cMid, smoothstep(-0.04, 0.26, y));
          col = mix(col, cTop, smoothstep(0.20, 0.78, y));
          float s = max(dot(d, normalize(sunDir)), 0.0);
          col += cSun * pow(s, 7.0) * 0.85;
          col += cSun * pow(s, 90.0) * 1.7;
          gl_FragColor = vec4(col, 1.0);
        }`,
    })
  }
  const sky = new THREE.Mesh(new THREE.SphereGeometry(420, 32, 20), skyMaterial())
  scene.add(sky)

  // image-based lighting from the same sky gradient
  const pmrem = new THREE.PMREMGenerator(renderer)
  const envScene = new THREE.Scene()
  const envSky = new THREE.Mesh(new THREE.SphereGeometry(40, 24, 14), skyMaterial())
  envScene.add(envSky)
  scene.environment = pmrem.fromScene(envScene, 0.5).texture
  envSky.geometry.dispose()

  // ---- lighting ------------------------------------------------------------
  scene.add(new THREE.AmbientLight(P.ambient, P.ambientInt))
  scene.add(new THREE.HemisphereLight(P.hemiSky, P.hemiGround, P.hemiInt))
  const sun = new THREE.DirectionalLight(P.sunColor, P.sunInt)
  sun.position.set(...P.sunPos)
  sun.castShadow = true
  sun.shadow.mapSize.set(4096, 4096)
  sun.shadow.camera.near = 10
  sun.shadow.camera.far = 320
  sun.shadow.camera.left = -90; sun.shadow.camera.right = 90
  sun.shadow.camera.top = 90; sun.shadow.camera.bottom = -90
  sun.shadow.bias = -0.0004
  sun.shadow.normalBias = 0.04
  scene.add(sun)
  const fill = new THREE.DirectionalLight(P.hemiSky, P.sunInt * 0.18)
  fill.position.set(-P.sunPos[0], P.sunPos[1] * 0.7, -P.sunPos[2])
  scene.add(fill)

  // ---- city container ------------------------------------------------------
  const city = new THREE.Group()
  scene.add(city)

  // ground
  const ground = new THREE.Mesh(
    new THREE.PlaneGeometry(900, 900),
    new THREE.MeshStandardMaterial({ color: P.ground, roughness: 0.95, metalness: 0.05 }),
  )
  ground.rotation.x = -Math.PI / 2
  ground.position.y = -0.02
  ground.receiveShadow = true
  city.add(ground)

  // block layout — 5×5 grid of lots, river runs the z=x diagonal
  const BX = [-36, -18, 0, 18, 36]
  const LOT = 15
  const isRiver = (cx, cz) => Math.abs(cx - cz) < 9
  const parkI = 1, parkJ = 3 // one block is a park

  const lotMat = new THREE.MeshStandardMaterial({ color: P.lot, roughness: 0.92, metalness: 0.08 })
  const grassMat = new THREE.MeshStandardMaterial({ color: P.grass, roughness: 0.95, metalness: 0 })

  // facade textures (a few variants, reused across buildings)
  const winSets = []
  for (let i = 0; i < 6; i++) winSets.push(makeFacade(rng, P))

  const _v = new THREE.Vector3()

  function facadeMaterial(w, h) {
    if (variant === 'invisible') {
      return new THREE.MeshBasicMaterial({ color: 0x040806 })
    }
    const set = winSets[ri(0, winSets.length - 1)]
    const rx = Math.max(1, Math.round(w / 3.6))
    const ry = Math.max(2, Math.round(h / 3.8))
    const map = set.map.clone(); map.needsUpdate = true
    map.wrapS = map.wrapT = THREE.RepeatWrapping; map.repeat.set(rx, ry)
    const emit = set.emit.clone(); emit.needsUpdate = true
    emit.wrapS = emit.wrapT = THREE.RepeatWrapping; emit.repeat.set(rx, ry)
    return new THREE.MeshStandardMaterial({
      color: P.facade[ri(0, P.facade.length - 1)],
      map,
      emissive: 0xffffff,
      emissiveMap: emit,
      emissiveIntensity: P.windowLit,
      roughness: variant === 'ethereum' ? 0.36 : 0.66,
      metalness: variant === 'ethereum' ? 0.62 : 0.22,
      envMapIntensity: variant === 'ethereum' ? 1.15 : 0.85,
    })
  }
  const trimMat = new THREE.MeshStandardMaterial({
    color: variant === 'invisible' ? 0x040806 : (variant === 'ethereum' ? 0x1a2a6a : 0x8b94a2),
    roughness: 0.5, metalness: 0.6,
  })

  function addBox(parent, w, h, d, x, y, z, mat) {
    const geo = new THREE.BoxGeometry(w, h, d)
    const m = new THREE.Mesh(geo, mat)
    m.position.set(x, y, z)
    m.castShadow = true; m.receiveShadow = true
    m.userData.edge = true
    parent.add(m)
    return m
  }
  function addCyl(parent, rt, rb, h, x, y, z, mat) {
    const geo = new THREE.CylinderGeometry(rt, rb, h, 26)
    const m = new THREE.Mesh(geo, mat)
    m.position.set(x, y, z)
    m.castShadow = true; m.receiveShadow = true
    m.userData.edge = true
    parent.add(m)
    return m
  }

  // ---- one building --------------------------------------------------------
  function building(gx, gz, w, d, h) {
    const g = new THREE.Group()
    g.position.set(gx, 0, gz)
    const style = rng()
    if (style < 0.16) {
      // cylindrical tower
      const r = Math.min(w, d) / 2
      addCyl(g, r, r, h, 0, h / 2, 0, facadeMaterial(w, h))
      addCyl(g, r * 0.35, r * 0.35, h * 0.16, 0, h + h * 0.08, 0, trimMat)
    } else if (style < 0.5) {
      // tiered ziggurat
      let cy = 0, cw = w, cd = d, ch = h
      for (let t = 0; t < 3 && ch > 2; t++) {
        addBox(g, cw, ch, cd, 0, cy + ch / 2, 0, facadeMaterial(cw, ch))
        cy += ch
        cw *= 0.68; cd *= 0.68; ch *= 0.5
      }
    } else {
      // slab with rooftop kit
      addBox(g, w, h, d, 0, h / 2, 0, facadeMaterial(w, h))
      const r = rng()
      if (r < 0.4) {
        addCyl(g, w * 0.16, w * 0.16, 0.9, w * 0.2, h + 0.45, d * 0.18, trimMat) // tank
      } else if (r < 0.72) {
        addBox(g, w * 0.5, 0.8, d * 0.5, 0, h + 0.4, 0, trimMat) // penthouse
      }
      if (h > 16 || rng() < 0.3) {
        addCyl(g, 0.07, 0.07, h * 0.34, 0, h + h * 0.17, 0, trimMat) // antenna
      }
    }
    city.add(g)
  }

  // ---- buildings per block -------------------------------------------------
  for (let i = 0; i < BX.length; i++) {
    for (let j = 0; j < BX.length; j++) {
      const cx = BX[i], cz = BX[j]
      if (isRiver(cx, cz)) continue
      if (i === parkI && j === parkJ) {
        const gp = new THREE.Mesh(new THREE.PlaneGeometry(LOT, LOT), grassMat)
        gp.rotation.x = -Math.PI / 2; gp.position.set(cx, 0.03, cz); gp.receiveShadow = true
        city.add(gp)
        for (let t = 0; t < 11; t++) tree(cx + rr(-6, 6), cz + rr(-6, 6))
        continue
      }
      const lp = new THREE.Mesh(new THREE.PlaneGeometry(LOT, LOT), lotMat)
      lp.rotation.x = -Math.PI / 2; lp.position.set(cx, 0.02, cz); lp.receiveShadow = true
      city.add(lp)

      // downtown rises toward the centre
      const dwn = 1 - Math.min(1, Math.hypot(cx, cz) / 64)
      const sub = rng() < 0.55 ? 2 : 1 // 1 big or 4 smaller buildings
      const cell = LOT / sub
      for (let a = 0; a < sub; a++) {
        for (let b = 0; b < sub; b++) {
          if (sub === 2 && rng() < 0.16) continue
          const ox = cx - LOT / 2 + cell * (a + 0.5)
          const oz = cz - LOT / 2 + cell * (b + 0.5)
          const w = cell * rr(0.5, 0.78)
          const d = cell * rr(0.5, 0.78)
          const h = rr(7, 13) + dwn * rr(10, 46) * (sub === 1 ? 1.25 : 0.8)
          building(ox, oz, w, d, h)
        }
      }
    }
  }

  // ---- trees ---------------------------------------------------------------
  function tree(x, z) {
    const g = new THREE.Group()
    g.position.set(x, 0, z)
    const trunkMat = new THREE.MeshStandardMaterial({
      color: variant === 'invisible' ? 0x041208 : 0x3a2a1c, roughness: 0.95,
    })
    const leafMat = new THREE.MeshStandardMaterial({
      color: P.tree, roughness: 0.85, metalness: 0,
      emissive: variant === 'invisible' ? P.tree : 0x000000,
      emissiveIntensity: variant === 'invisible' ? 0.4 : 0,
    })
    const th = rr(1.4, 2.4)
    addCyl(g, 0.12, 0.18, th, 0, th / 2, 0, trunkMat)
    const cr = rr(1.1, 1.8)
    const cm = new THREE.Mesh(new THREE.IcosahedronGeometry(cr, 1), leafMat)
    cm.position.y = th + cr * 0.7
    cm.scale.y = 0.85
    cm.castShadow = true
    cm.userData.edge = true
    g.add(cm)
    city.add(g)
  }
  // street trees along the central avenues
  for (const c of BX) {
    for (let s = -50; s <= 50; s += 12.5) {
      if (Math.abs(c - s) < 9) continue
      if (rng() < 0.5) tree(c + 9, s)
      if (rng() < 0.5) tree(s, c + 9)
    }
  }

  // ---- river + bridges -----------------------------------------------------
  const riverMat = new THREE.MeshStandardMaterial({
    color: P.river, emissive: P.riverGlow, emissiveIntensity: 0.5,
    roughness: 0.06, metalness: 0.9, envMapIntensity: 1.6,
  })
  const river = new THREE.Mesh(new THREE.PlaneGeometry(170, 13), riverMat)
  river.rotation.x = -Math.PI / 2
  river.rotation.z = Math.PI / 4
  river.position.y = 0.05
  river.receiveShadow = true
  city.add(river)
  // bridges — both avenues at x=c and z=c cross the diagonal river at (c,c)
  for (const c of [-45, -27, -9, 9, 27, 45]) {
    if (Math.abs(c) > 50) continue
    const bridge = new THREE.Group()
    bridge.position.set(c, 0, c)
    addBox(bridge, 19, 0.5, 5, 0, 0.6, 0, trimMat)
    addBox(bridge, 5, 0.5, 19, 0, 0.6, 0, trimMat)
    for (const e of [-1, 1]) {
      addCyl(bridge, 0.18, 0.18, 3.4, e * 8.5, 2.0, 0, trimMat)
      addCyl(bridge, 0.18, 0.18, 3.4, 0, 2.0, e * 8.5, trimMat)
    }
    city.add(bridge)
  }

  // ---- streetlights --------------------------------------------------------
  const bulbMat = new THREE.MeshBasicMaterial({ color: P.windowGlow })
  const poleMat = trimMat
  function streetlight(x, z) {
    const g = new THREE.Group()
    g.position.set(x, 0, z)
    addCyl(g, 0.1, 0.14, 4.4, 0, 2.2, 0, poleMat)
    const b = new THREE.Mesh(new THREE.SphereGeometry(0.34, 12, 8), bulbMat)
    b.position.y = 4.5
    g.add(b)
    city.add(g)
  }
  for (const c of [-45, -27, -9, 9, 27, 45]) {
    for (let s = -48; s <= 48; s += 24) {
      if (Math.abs(c - s) < 10) continue
      streetlight(c, s)
    }
  }

  // ---- cars (animated) -----------------------------------------------------
  const cars = []
  const carGeo = new THREE.BoxGeometry(0.9, 0.5, 2.0)
  const ROADS = [-45, -27, -9, 9, 27, 45]
  function spawnCars(axis, fixed) {
    const n = ri(2, 4)
    for (let k = 0; k < n; k++) {
      const head = rng() < 0.5
      const mat = new THREE.MeshStandardMaterial({
        color: 0x0a0a0a, emissive: head ? P.car : P.carTail,
        emissiveIntensity: variant === 'base' ? 1.1 : 1.7, roughness: 0.5, metalness: 0.3,
      })
      const m = new THREE.Mesh(carGeo, mat)
      m.castShadow = true
      if (axis === 'x') m.rotation.y = Math.PI / 2
      city.add(m)
      cars.push({
        m, axis, fixed,
        p: rr(-52, 52),
        dir: head ? 1 : -1,
        lane: head ? 1.4 : -1.4,
        speed: rr(8, 17),
      })
    }
  }
  for (const r of ROADS) { spawnCars('x', r); spawnCars('z', r) }

  // ---- AI agents — the city's inhabitants: most trade, some prey -----------
  const agents = []
  if (P.agents) {
    const bodyGeo = new THREE.CapsuleGeometry(0.72, 2.8, 6, 14)
    const headGeo = new THREE.SphereGeometry(0.78, 16, 12)
    function makeAgent(role) {
      const glow = role === 'thief' ? 0xff4368 : 0x4fdcff
      const m = new THREE.MeshStandardMaterial({
        color: 0x05060c, emissive: glow, emissiveIntensity: 2.1,
        roughness: 0.45, metalness: 0.2,
      })
      const g = new THREE.Group()
      const body = new THREE.Mesh(bodyGeo, m); body.position.y = 2.3; body.castShadow = true
      const head = new THREE.Mesh(headGeo, m); head.position.y = 4.5; head.castShadow = true
      g.add(body); g.add(head)
      if (role === 'thief') {
        const hood = new THREE.Mesh(new THREE.ConeGeometry(0.96, 1.3, 16),
          new THREE.MeshStandardMaterial({ color: 0x1a0710, emissive: glow, emissiveIntensity: 0.6, roughness: 0.7 }))
        hood.position.y = 4.85
        g.add(hood)
      }
      city.add(g)
      return { g, role, mat: m }
    }
    for (let i = 0; i < 18; i++) {
      const a = makeAgent('trader')
      a.onX = rng() < 0.5
      a.fixed = ROADS[ri(0, ROADS.length - 1)]
      a.p = rr(-50, 50)
      a.dir = rng() < 0.5 ? 1 : -1
      a.speed = rr(5, 9)
      a.lane = (rng() < 0.5 ? 1 : -1) * 2.1
      agents.push(a)
    }
    for (let i = 0; i < 7; i++) {
      const a = makeAgent('thief')
      a.g.position.set(rr(-40, 40), 0, rr(-40, 40))
      a.target = null
      a.retimer = rr(0, 4)
      agents.push(a)
    }
  }
  const traders = agents.filter((a) => a.role === 'trader')

  // ---- stars (ethereum) ----------------------------------------------------
  if (P.stars) {
    const sg = new THREE.BufferGeometry()
    const sp = []
    for (let i = 0; i < 600; i++) {
      const v = new THREE.Vector3().setFromSphericalCoords(
        rr(260, 380), rr(0.15, 1.3) * Math.PI * 0.5, rr(0, Math.PI * 2))
      sp.push(v.x, v.y, v.z)
    }
    sg.setAttribute('position', new THREE.Float32BufferAttribute(sp, 3))
    scene.add(new THREE.Points(sg, new THREE.PointsMaterial({
      color: P.stars, size: 1.1, sizeAttenuation: true, transparent: true, opacity: 0.85, fog: false,
    })))
  }

  // ---- Matrix floor grid + digital rain (invisible) ------------------------
  let rain = null
  if (P.grid) {
    const grid = new THREE.GridHelper(150, 50, P.grid, P.grid)
    grid.position.y = 0.06
    grid.material.transparent = true
    grid.material.opacity = 0.35
    city.add(grid)
  }
  if (P.rain) {
    const N = 1400
    const rg = new THREE.BufferGeometry()
    const pos = new Float32Array(N * 3)
    for (let i = 0; i < N; i++) {
      pos[i * 3] = rr(-90, 90)
      pos[i * 3 + 1] = rr(0, 120)
      pos[i * 3 + 2] = rr(-90, 90)
    }
    rg.setAttribute('position', new THREE.BufferAttribute(pos, 3))
    rain = new THREE.Points(rg, new THREE.PointsMaterial({
      color: P.rain, size: 0.5, transparent: true, opacity: 0.55, fog: true,
    }))
    scene.add(rain)
  }

  // ---- merged glowing edges (invisible / ethereum) -------------------------
  // Done as a post-build pass so every mesh's world matrix is final — the
  // building-group offsets must be baked into the merged line geometry.
  if (P.edges) {
    const edgePts = []
    city.updateMatrixWorld(true)
    city.traverse((o) => {
      if (!o.isMesh || !o.userData.edge) return
      const eg = new THREE.EdgesGeometry(o.geometry, 22)
      const pos = eg.attributes.position
      for (let i = 0; i < pos.count; i++) {
        _v.fromBufferAttribute(pos, i).applyMatrix4(o.matrixWorld)
        edgePts.push(_v.x, _v.y, _v.z)
      }
      eg.dispose()
    })
    const eg = new THREE.BufferGeometry()
    eg.setAttribute('position', new THREE.Float32BufferAttribute(edgePts, 3))
    city.add(new THREE.LineSegments(eg, new THREE.LineBasicMaterial({
      color: P.edges, transparent: true, opacity: P.edgeInt,
    })))
  }

  // ---- controls ------------------------------------------------------------
  const controls = new OrbitControls(camera, renderer.domElement)
  controls.enableDamping = true
  controls.dampingFactor = 0.06
  controls.target.set(0, 8, 0)
  controls.minDistance = 44
  controls.maxDistance = 210
  controls.minPolarAngle = 0.18
  controls.maxPolarAngle = 1.46
  controls.autoRotate = true
  controls.autoRotateSpeed = 0.32
  controls.rotateSpeed = 0.6
  controls.update()

  // ---- post ----------------------------------------------------------------
  const composer = new EffectComposer(renderer)
  composer.addPass(new RenderPass(scene, camera))
  const bloom = new UnrealBloomPass(
    new THREE.Vector2(W, H), P.bloom.strength, P.bloom.radius, P.bloom.threshold)
  composer.addPass(bloom)
  composer.addPass(new OutputPass())
  composer.setSize(W, H)

  // ---- resize --------------------------------------------------------------
  function resize() {
    W = window.innerWidth; H = window.innerHeight
    camera.aspect = W / H
    camera.updateProjectionMatrix()
    renderer.setSize(W, H, false)
    composer.setSize(W, H)
  }
  window.addEventListener('resize', resize)

  // ---- loop ----------------------------------------------------------------
  let raf = 0
  let prev = performance.now()
  function tick() {
    raf = requestAnimationFrame(tick)
    const now = performance.now()
    const dt = Math.min((now - prev) / 1000, 0.05)
    prev = now
    controls.update()
    for (const c of cars) {
      c.p += c.dir * c.speed * dt
      if (c.p > 54) c.p = -54
      if (c.p < -54) c.p = 54
      if (c.axis === 'x') c.m.position.set(c.p, 0.45, c.fixed + c.lane)
      else c.m.position.set(c.fixed + c.lane, 0.45, c.p)
    }
    const tt = now / 1000
    for (const a of agents) {
      if (a.role === 'trader') {
        a.p += a.dir * a.speed * dt
        if (a.p > 53) a.p = -53
        if (a.p < -53) a.p = 53
        const x = a.onX ? a.p : a.fixed + a.lane
        const z = a.onX ? a.fixed + a.lane : a.p
        a.g.position.set(x, Math.abs(Math.sin(tt * 7 + a.p)) * 0.35, z)
        a.g.rotation.y = a.onX ? (a.dir > 0 ? Math.PI / 2 : -Math.PI / 2) : (a.dir > 0 ? 0 : Math.PI)
        a.mat.emissiveIntensity += (2.1 - a.mat.emissiveIntensity) * 0.06
      } else {
        a.retimer -= dt
        if (!a.target || a.retimer <= 0) {
          a.target = traders[ri(0, traders.length - 1)]
          a.retimer = rr(3.5, 7)
        }
        const tp = a.target.g.position
        const dx = tp.x - a.g.position.x, dz = tp.z - a.g.position.z
        const dist = Math.hypot(dx, dz) || 1
        const sp = dist > 5 ? 7.5 : 17 // a sudden lunge when close
        a.g.position.x += (dx / dist) * sp * dt
        a.g.position.z += (dz / dist) * sp * dt
        a.g.position.y = Math.abs(Math.sin(tt * 10)) * 0.45
        a.g.rotation.y = Math.atan2(dx, dz)
        if (dist < 3.4) a.target.mat.emissiveIntensity = 0.35 + Math.random() * 0.5
      }
    }
    if (rain) {
      const pos = rain.geometry.attributes.position
      for (let i = 0; i < pos.count; i++) {
        let y = pos.getY(i) - dt * 26
        if (y < 0) y = rr(80, 130)
        pos.setY(i, y)
      }
      pos.needsUpdate = true
    }
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
