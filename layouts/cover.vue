<script setup>
defineProps({
  class: {
    type: String,
    default: '',
  },
})
</script>

<template>
  <div class="slidev-layout cover" :class="$props.class">
    <!-- Top-left icon -->
    <div class="cover-icon">
      <img src="/images/nyx_icon.svg" alt="Nyx" />
    </div>

    <!-- Main content -->
    <div class="cover-content">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.cover {
  position: relative;
  width: 100%;
  height: 100%;
  background: #ffffff;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  overflow: hidden;
}

.cover-icon {
  position: absolute;
  top: -40px;
  left: -70px;
  z-index: 0;
}

.cover-icon img {
  width: 360px;
  height: auto;
  opacity: 0.4;
  filter: grayscale(100%) brightness(0.6);
}

.cover-content {
  text-align: center;
  z-index: 1;
}

.cover-content :deep(h1) {
  font-family: 'BIZ UDPMincho', serif !important;
  font-size: 2.5rem;
  font-weight: bold;
  color: #000000;
  margin-bottom: 1rem;
}

.cover-content :deep(h2) {
  font-family: 'BIZ UDPMincho', serif !important;
  font-size: 1.5rem;
  color: #000000;
  margin-bottom: 2rem;
}

.cover-content :deep(p) {
  font-family: 'BIZ UDPMincho', serif !important;
  color: #000000;
}
</style>
