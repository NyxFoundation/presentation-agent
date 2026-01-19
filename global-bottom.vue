<script setup>
import { computed } from 'vue'

const isFirstSlide = computed(() => $nav.currentPage === 1)
</script>

<template>
  <div class="nyx-footer">
    <img src="/images/nyx_logo.svg" alt="Nyx" class="nyx-logo" />
    <span v-if="!isFirstSlide" class="page-number">{{ $nav.currentPage }}</span>
  </div>
</template>

<style scoped>
.nyx-footer {
  position: fixed;
  bottom: 20px;
  right: 30px;
  z-index: 100;
  display: flex;
  align-items: center;
  gap: 6px;
  pointer-events: none;
}

.nyx-logo {
  width: 160px;
  height: auto;
}

.page-number {
  font-family: 'BIZ UDPMincho', serif;
  font-size: 14px;
  color: #000000;
  margin-left: 8px;
}
</style>
