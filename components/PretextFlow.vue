<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import { prepareWithSegments, layoutNextLine } from '@chenglou/pretext'

const props = defineProps({
  text: { type: String, required: true },
  font: { type: String, default: '20px Noto Sans JP' },
  lineHeight: { type: Number, default: 30 },
  charSrc: { type: String, default: '/images/character.png' },
  charSize: { type: Number, default: 100 },
})

const containerRef = ref(null)
const charX = ref(500)
const charY = ref(80)
const dragging = ref(false)
const dragOffset = ref({ x: 0, y: 0 })
const lines = ref([])

function layoutText() {
  if (!containerRef.value) return
  const containerWidth = containerRef.value.clientWidth
  const prepared = prepareWithSegments(props.text, props.font)

  const result = []
  let cursor = { segmentIndex: 0, graphemeIndex: 0 }
  let y = 0
  const padding = 12

  for (let i = 0; i < 200; i++) {
    const lineTop = y
    const lineBottom = y + props.lineHeight
    const cTop = charY.value
    const cBottom = charY.value + props.charSize
    const cLeft = charX.value
    const cRight = charX.value + props.charSize

    let maxWidth = containerWidth
    let xOffset = 0

    // If this line vertically overlaps the character
    if (lineBottom > cTop && lineTop < cBottom) {
      const spaceLeft = cLeft - padding
      const spaceRight = containerWidth - cRight - padding

      if (spaceLeft >= spaceRight && spaceLeft > 60) {
        maxWidth = spaceLeft
        xOffset = 0
      } else if (spaceRight > 60) {
        maxWidth = spaceRight
        xOffset = cRight + padding
      } else {
        // Not enough space on either side, use full width
        maxWidth = containerWidth
      }
    }

    if (maxWidth < 40) maxWidth = 40

    const line = layoutNextLine(prepared, cursor, maxWidth)
    if (!line) break

    result.push({ text: line.text, x: xOffset, y, width: line.width })
    cursor = line.end
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
  nextTick(() => layoutText())
  window.addEventListener('mousemove', onMouseMove)
  window.addEventListener('mouseup', onMouseUp)
})

onUnmounted(() => {
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
        width: charSize + 'px',
        height: charSize + 'px',
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
