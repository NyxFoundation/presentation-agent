<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import { prepareWithSegments, layoutNextLine } from '@chenglou/pretext'

const props = defineProps({
  charSrc: { type: String, default: '/images/logo.png' },
  charWidth: { type: Number, default: 172 },
  charHeight: { type: Number, default: 116 },
  speedX: { type: Number, default: 0.7 },
  speedY: { type: Number, default: 0.35 },
  padding: { type: Number, default: 6 },
  textColor: { type: String, default: '#111' },
})

// Style definitions for rich text segments
const STYLES = {
  h1: { font: '900 32px "Noto Sans JP", sans-serif', lineHeight: 48, color: '#111', marginBottom: 12 },
  h2: { font: '700 24px "Noto Sans JP", sans-serif', lineHeight: 36, color: '#111', marginBottom: 8 },
  h3: { font: '700 20px "Noto Sans JP", sans-serif', lineHeight: 30, color: '#111', marginBottom: 6 },
  body: { font: '400 18px "Noto Sans JP", sans-serif', lineHeight: 28, color: '#333', marginBottom: 4 },
  bold: { font: '700 18px "Noto Sans JP", sans-serif', lineHeight: 28, color: '#111', marginBottom: 4 },
  sub: { font: '400 14px "Noto Sans JP", sans-serif', lineHeight: 22, color: '#666', marginBottom: 4 },
}

const containerRef = ref(null)
const textRef = ref(null)
const charX = ref(0)
const charY = ref(80)
const dragging = ref(false)
const dragOffset = ref({ x: 0, y: 0 })
const renderedLines = ref([])
const outlineRows = ref([])
const richSegments = ref([])
let animFrameId = null
const dirX = ref(1)
const dirY = ref(1)
let lastLayoutX = 0
let lastLayoutY = 0

// Parse rendered HTML from slot into styled segments
function parseSegments(container) {
  const segments = []
  const children = container.childNodes

  for (const node of children) {
    if (node.nodeType === Node.TEXT_NODE) {
      const text = node.textContent.trim()
      if (text) segments.push({ style: 'body', text })
      continue
    }
    if (node.nodeType !== Node.ELEMENT_NODE) continue

    const tag = node.tagName.toLowerCase()
    const text = node.textContent.trim()
    if (!text) {
      segments.push({ style: 'gap', text: '', marginBottom: 16 })
      continue
    }

    if (tag === 'h1') {
      segments.push({ style: 'h1', text })
      segments.push({ style: 'gap', text: '', marginBottom: 12 })
    } else if (tag === 'h2') {
      segments.push({ style: 'gap', text: '', marginBottom: 8 })
      segments.push({ style: 'h2', text })
    } else if (tag === 'h3') {
      segments.push({ style: 'gap', text: '', marginBottom: 6 })
      segments.push({ style: 'h3', text })
    } else if (tag === 'p') {
      // Parse inline elements within <p>
      for (const child of node.childNodes) {
        if (child.nodeType === Node.TEXT_NODE) {
          const t = child.textContent
          if (t) segments.push({ style: 'body', text: t })
        } else if (child.nodeType === Node.ELEMENT_NODE) {
          const childTag = child.tagName.toLowerCase()
          const childText = child.textContent
          if (!childText) continue
          if (childTag === 'strong' || childTag === 'b') {
            segments.push({ style: 'bold', text: childText })
          } else if (childTag === 'del' || childTag === 's') {
            segments.push({ style: 'sub', text: childText })
          } else if (childTag === 'em' || childTag === 'i') {
            segments.push({ style: 'bold', text: childText })
          } else if (childTag === 'code') {
            segments.push({ style: 'bold', text: childText })
          } else {
            segments.push({ style: 'body', text: childText })
          }
        }
      }
      segments.push({ style: 'gap', text: '', marginBottom: 6 })
    } else {
      segments.push({ style: 'body', text })
      segments.push({ style: 'gap', text: '', marginBottom: 6 })
    }
  }
  return segments
}

// Prepare pretext objects for each segment
function prepareSegments(segments) {
  return segments.map(seg => {
    if (seg.style === 'gap' || seg.style === 'linebreak') return seg
    const styleDef = STYLES[seg.style]
    return {
      ...seg,
      prepared: prepareWithSegments(seg.text, styleDef.font),
      styleDef,
    }
  })
}

function animate() {
  if (dragging.value || !containerRef.value) {
    animFrameId = requestAnimationFrame(animate)
    return
  }
  const containerWidth = containerRef.value.clientWidth
  const containerHeight = containerRef.value.clientHeight

  charX.value += props.speedX * dirX.value
  charY.value += props.speedY * dirY.value

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

function getOpaqueRange(lineTop, lineBottom) {
  const cTop = charY.value
  const cBottom = charY.value + props.charHeight
  if (lineBottom <= cTop || lineTop >= cBottom) return null

  const imgH = outlineRows.value.length
  if (imgH === 0) return null

  const scaleY = imgH / props.charHeight
  const lineCenter = (lineTop + lineBottom) / 2
  const imgRow = Math.round((lineCenter - cTop) * scaleY)
  if (imgRow < 0 || imgRow >= imgH) return null

  const row = outlineRows.value[imgRow]
  if (!row) return null

  const imgNaturalWidth = outlineRows.value._naturalWidth
  const dLeft = charX.value + (row.left / imgNaturalWidth) * props.charWidth
  const dRight = charX.value + ((row.right + 1) / imgNaturalWidth) * props.charWidth

  return { left: dLeft, right: dRight }
}

// Layout a single segment's line within available width, handling wrapping around the image
function layoutSegmentLine(prepared, cursor, y, lh, containerWidth) {
  const fragments = []
  const lineTop = y
  const lineBottom = y + lh
  const opaque = getOpaqueRange(lineTop, lineBottom)

  if (opaque) {
    const spaceLeft = opaque.left - props.padding
    const spaceRight = containerWidth - opaque.right - props.padding

    if (spaceLeft > 40) {
      const leftLine = layoutNextLine(prepared, cursor, spaceLeft)
      if (leftLine) {
        fragments.push({ text: leftLine.text, x: 0, y, width: leftLine.width })
        cursor = leftLine.end
      }
    }

    if (spaceRight > 40) {
      const rightLine = layoutNextLine(prepared, cursor, spaceRight)
      if (rightLine) {
        fragments.push({ text: rightLine.text, x: opaque.right + props.padding, y, width: rightLine.width })
        cursor = rightLine.end
      }
    }

    if (spaceLeft <= 40 && spaceRight <= 40) {
      const line = layoutNextLine(prepared, cursor, containerWidth)
      if (line) {
        fragments.push({ text: line.text, x: 0, y, width: line.width })
        cursor = line.end
      }
    }
  } else {
    const line = layoutNextLine(prepared, cursor, containerWidth)
    if (line) {
      fragments.push({ text: line.text, x: 0, y, width: line.width })
      cursor = line.end
    }
  }

  return { fragments, cursor }
}

function layoutText() {
  if (!containerRef.value || richSegments.value.length === 0) return
  const containerWidth = containerRef.value.clientWidth
  const result = []
  let y = 0

  for (const seg of richSegments.value) {
    if (seg.style === 'gap') {
      y += seg.marginBottom || 16
      continue
    }
    if (seg.style === 'linebreak') {
      continue
    }

    const { prepared, styleDef } = seg
    if (!prepared || !styleDef) continue

    let cursor = { segmentIndex: 0, graphemeIndex: 0 }
    let safety = 0

    while (safety++ < 100) {
      const { fragments, cursor: newCursor } = layoutSegmentLine(
        prepared, cursor, y, styleDef.lineHeight, containerWidth
      )
      if (fragments.length === 0) break

      for (const frag of fragments) {
        result.push({
          text: frag.text,
          x: frag.x,
          y: frag.y,
          font: styleDef.font,
          lineHeight: styleDef.lineHeight,
          color: styleDef.color,
        })
      }

      cursor = newCursor
      y += styleDef.lineHeight

      // Check if we consumed all text
      const totalSegs = prepared.segments.length
      if (cursor.segmentIndex >= totalSegs) break
    }

    y += styleDef.marginBottom || 0
  }

  renderedLines.value = result
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
  if (textRef.value) {
    const segments = parseSegments(textRef.value)
    richSegments.value = prepareSegments(segments)
  }

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
  <div class="slidev-layout pretext-flow-layout">
    <!-- Hidden slot to extract text content -->
    <div ref="textRef" style="display: none"><slot /></div>

    <div ref="containerRef" class="pretext-container">
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

      <span
        v-for="(line, i) in renderedLines"
        :key="i"
        :style="{
          position: 'absolute',
          left: line.x + 'px',
          top: line.y + 'px',
          whiteSpace: 'pre',
          font: line.font,
          lineHeight: line.lineHeight + 'px',
          color: line.color,
        }"
      >{{ line.text }}</span>
    </div>
  </div>
</template>

<style scoped>
.pretext-flow-layout {
  padding: 2rem;
  font-family: 'Noto Sans JP', sans-serif;
}

.pretext-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
</style>
