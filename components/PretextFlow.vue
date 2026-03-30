<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import { prepareWithSegments, layoutNextLine } from '@chenglou/pretext'

const props = defineProps({
  text: { type: String, required: true },
  font: { type: String, default: '20px Noto Sans JP' },
  lineHeight: { type: Number, default: 30 },
  charSrc: { type: String, default: '/images/character.png' },
  charWidth: { type: Number, default: 120 },
  charHeight: { type: Number, default: 180 },
})

const containerRef = ref(null)
const charX = ref(0)
const charY = ref(80)
const dragging = ref(false)
const dragOffset = ref({ x: 0, y: 0 })
const lines = ref([])
// Per-row outline: for each pixel row of the image, store { left, right } of opaque area
const outlineRows = ref([])
// Animation
let animFrameId = null
const speedX = 0.4
const speedY = 0.2
const dirX = ref(1)
const dirY = ref(1)
let lastLayoutX = 0
let lastLayoutY = 0

function animate() {
  if (dragging.value || !containerRef.value) {
    animFrameId = requestAnimationFrame(animate)
    return
  }
  const containerWidth = containerRef.value.clientWidth
  const containerHeight = containerRef.value.clientHeight

  charX.value += speedX * dirX.value
  charY.value += speedY * dirY.value

  if (charX.value + props.charWidth >= containerWidth) {
    charX.value = containerWidth - props.charWidth
    dirX.value = -1
  } else if (charX.value <= 0) {
    charX.value = 0
    dirX.value = 1
  }

  if (charY.value + props.charHeight >= containerHeight) {
    charY.value = containerHeight - props.charHeight
    dirY.value = -1
  } else if (charY.value <= 0) {
    charY.value = 0
    dirY.value = 1
  }

  const dx = Math.abs(charX.value - lastLayoutX)
  const dy = Math.abs(charY.value - lastLayoutY)
  if (dx >= 2 || dy >= 2) {
    lastLayoutX = charX.value
    lastLayoutY = charY.value
    layoutText()
  }

  animFrameId = requestAnimationFrame(animate)
}

// Scan the image on a canvas to find opaque pixel bounds per row, then smooth
function buildOutline(img) {
  const canvas = document.createElement('canvas')
  canvas.width = img.naturalWidth
  canvas.height = img.naturalHeight
  const ctx = canvas.getContext('2d')
  ctx.drawImage(img, 0, 0)
  const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height)
  const data = imageData.data
  const raw = []
  for (let row = 0; row < canvas.height; row++) {
    let left = -1
    let right = -1
    for (let col = 0; col < canvas.width; col++) {
      const alpha = data[(row * canvas.width + col) * 4 + 3]
      if (alpha > 10) {
        if (left === -1) left = col
        right = col
      }
    }
    raw.push(left === -1 ? null : { left, right })
  }

  // Smooth outline with a small window to reduce jaggedness
  const smoothRadius = 3
  const rows = []
  for (let i = 0; i < raw.length; i++) {
    if (!raw[i]) { rows.push(null); continue }
    let sumL = 0, sumR = 0, count = 0
    for (let j = Math.max(0, i - smoothRadius); j <= Math.min(raw.length - 1, i + smoothRadius); j++) {
      if (raw[j]) {
        sumL += raw[j].left
        sumR += raw[j].right
        count++
      }
    }
    rows.push({ left: Math.round(sumL / count), right: Math.round(sumR / count) })
  }

  rows._naturalWidth = canvas.width
  outlineRows.value = rows
}

// For a given text line (y range), find the opaque bounds in display coordinates
function getOpaqueRange(lineTop, lineBottom) {
  const cTop = charY.value
  const cBottom = charY.value + props.charHeight
  if (lineBottom <= cTop || lineTop >= cBottom) return null

  const imgH = outlineRows.value.length
  if (imgH === 0) return null

  const scaleY = imgH / props.charHeight

  // Sample at the vertical center of the text line for tighter fit
  const lineCenter = (lineTop + lineBottom) / 2
  const imgRow = Math.round((lineCenter - cTop) * scaleY)
  if (imgRow < 0 || imgRow >= imgH) return null

  const row = outlineRows.value[imgRow]
  if (!row) return null
  const minLeft = row.left
  const maxRight = row.right

  // Convert image pixel coords to display coords
  const imgNaturalWidth = outlineRows.value._naturalWidth
  const dLeft = charX.value + (minLeft / imgNaturalWidth) * props.charWidth
  const dRight = charX.value + ((maxRight + 1) / imgNaturalWidth) * props.charWidth

  return { left: dLeft, right: dRight }
}

function layoutText() {
  if (!containerRef.value) return
  const containerWidth = containerRef.value.clientWidth
  const prepared = prepareWithSegments(props.text, props.font)

  const result = []
  let cursor = { segmentIndex: 0, graphemeIndex: 0 }
  let y = 0
  const padding = 4

  for (let i = 0; i < 400; i++) {
    const lineTop = y
    const lineBottom = y + props.lineHeight

    const opaque = getOpaqueRange(lineTop, lineBottom)

    if (opaque) {
      const spaceLeft = opaque.left - padding
      const spaceRight = containerWidth - opaque.right - padding

      // Layout left side
      if (spaceLeft > 40) {
        const leftLine = layoutNextLine(prepared, cursor, spaceLeft)
        if (!leftLine) break
        result.push({ text: leftLine.text, x: 0, y, width: leftLine.width })
        cursor = leftLine.end
      }

      // Layout right side
      if (spaceRight > 40) {
        const rightLine = layoutNextLine(prepared, cursor, spaceRight)
        if (!rightLine) break
        result.push({ text: rightLine.text, x: opaque.right + padding, y, width: rightLine.width })
        cursor = rightLine.end
      }

      // If neither side has space, use full width
      if (spaceLeft <= 40 && spaceRight <= 40) {
        const line = layoutNextLine(prepared, cursor, containerWidth)
        if (!line) break
        result.push({ text: line.text, x: 0, y, width: line.width })
        cursor = line.end
      }
    } else {
      const line = layoutNextLine(prepared, cursor, containerWidth)
      if (!line) break
      result.push({ text: line.text, x: 0, y, width: line.width })
      cursor = line.end
    }

    y += props.lineHeight
  }

  lines.value = result
}

function onMouseDown(e) {
  dragging.value = true
  const rect = containerRef.value.getBoundingClientRect()
  dragOffset.value = {
    x: e.clientX - rect.left - charX.value,
    y: e.clientY - rect.top - charY.value,
  }
  e.preventDefault()
}

function onMouseMove(e) {
  if (!dragging.value || !containerRef.value) return
  const rect = containerRef.value.getBoundingClientRect()
  charX.value = Math.max(0, e.clientX - rect.left - dragOffset.value.x)
  charY.value = Math.max(0, e.clientY - rect.top - dragOffset.value.y)
  layoutText()
}

function onMouseUp() {
  dragging.value = false
}

onMounted(() => {
  const img = new Image()
  img.src = props.charSrc
  img.onload = () => {
    buildOutline(img)
    nextTick(() => {
      layoutText()
      animate()
    })
  }
  window.addEventListener('mousemove', onMouseMove)
  window.addEventListener('mouseup', onMouseUp)
})

onUnmounted(() => {
  if (animFrameId) cancelAnimationFrame(animFrameId)
  window.removeEventListener('mousemove', onMouseMove)
  window.removeEventListener('mouseup', onMouseUp)
})
</script>

<template>
  <div ref="containerRef" class="pretext-flow">
    <!-- Character (draggable) -->
    <img
      :src="charSrc"
      :style="{
        position: 'absolute',
        left: charX + 'px',
        top: charY + 'px',
        width: charWidth + 'px',
        height: charHeight + 'px',
        objectFit: 'contain',
        cursor: 'grab',
        zIndex: 10,
        userSelect: 'none',
      }"
      draggable="false"
      @mousedown="onMouseDown"
    />

    <!-- Text lines rendered by pretext -->
    <span
      v-for="(line, i) in lines"
      :key="i"
      :style="{
        position: 'absolute',
        left: line.x + 'px',
        top: line.y + 'px',
        whiteSpace: 'pre',
        font: font,
        lineHeight: lineHeight + 'px',
        color: '#111',
      }"
    >{{ line.text }}</span>
  </div>
</template>

<style scoped>
.pretext-flow {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
</style>
