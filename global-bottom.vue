<script setup>
import { computed } from 'vue'

const isFirstSlide = computed(() => $nav.currentPage === 1)
</script>

<template>
  <div class="zk-footer">
    <img src="/images/zktokyo_logo.png" alt="ZK Tokyo" class="zk-logo" />
    <span v-if="!isFirstSlide" class="page-number">{{ $nav.currentPage }}</span>
  </div>
</template>

<style scoped>
.zk-footer {
  position: fixed;
  bottom: 20px;
  right: 30px;
  z-index: 100;
  display: flex;
  align-items: center;
  gap: 6px;
  pointer-events: none;
}

.zk-logo {
  width: 72px;
  height: auto;
}

.page-number {
  font-family: 'BIZ UDPMincho', serif;
  font-size: 14px;
  color: #000000;
  margin-left: 8px;
}
</style>
