<script setup>
import { computed } from 'vue'

const isFirstSlide = computed(() => $nav.currentPage === 1)
</script>

<template>
  <div class="nyx-footer">
    <img src="/aladdin-logo-footer.png" alt="Aladdin" class="nyx-logo" />
    <span v-if="!isFirstSlide" class="page-number">{{ $nav.currentPage }}</span>
  </div>
</template>

<style scoped>
.nyx-footer {
  position: fixed;
  bottom: 12px;
  right: 20px;
  z-index: 100;
  display: flex;
  align-items: center;
  gap: 6px;
  pointer-events: none;
}

.nyx-logo {
  width: 60px;
  height: auto;
}

.page-number {
  font-family: 'Noto Sans JP', sans-serif;
  font-size: 12px;
  color: #999;
  margin-left: 6px;
}
</style>
