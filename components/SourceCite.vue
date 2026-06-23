<script setup lang="ts">
defineProps<{
  sources: Array<{ label: string; url: string }>
}>()
</script>

<template>
  <div class="source-cite">
    <span class="label">Sources</span>
    <template v-for="(s, i) in sources" :key="s.url">
      <a :href="s.url" target="_blank" rel="noopener" class="src-link">{{ s.label }}</a>
      <span v-if="i < sources.length - 1" class="sep"> · </span>
    </template>
  </div>
</template>

<style scoped>
.source-cite {
  position: absolute;
  bottom: 16px;
  left: 24px;
  font-size: 9px;
  opacity: 0.55;
  line-height: 1.4;
  max-width: 65%;
  z-index: 50;
  font-family: ui-sans-serif, system-ui, sans-serif;
}
.label {
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-right: 6px;
  font-weight: 600;
}
.src-link {
  text-decoration: underline;
  text-decoration-style: dotted;
  text-underline-offset: 2px;
  color: inherit;
}
.src-link:hover {
  opacity: 1;
}
.sep {
  opacity: 0.5;
}
</style>
