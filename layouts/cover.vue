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
      <img src="/aladdin-logo-cover.png" alt="Aladdin" />
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
  top: -20px;
  left: -30px;
  z-index: 0;
}

.cover-icon img {
  width: 300px;
  height: auto;
  opacity: 0.12;
}

.cover-content {
  text-align: center;
  z-index: 1;
}

.cover-content :deep(h1) {
  font-family: 'Noto Sans JP', sans-serif !important;
  font-size: 2.2rem;
  font-weight: 900;
  color: #111;
  margin-bottom: 1rem;
}

.cover-content :deep(h2) {
  font-family: 'Noto Sans JP', sans-serif !important;
  font-size: 1.3rem;
  color: #111;
  margin-bottom: 2rem;
}

.cover-content :deep(p) {
  font-family: 'Noto Sans JP', sans-serif !important;
  color: #111;
}
</style>
