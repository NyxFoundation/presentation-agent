<script setup lang="ts">
import { TresCanvas } from '@tresjs/core'
import AsconCityScene from './AsconCityScene.vue'
</script>

<template>
  <TresCanvas clear-color="#06081a" :antialias="true">
    <AsconCityScene />
  </TresCanvas>
</template>

<style scoped>
:deep(canvas) {
  display: block;
  width: 100% !important;
  height: 100% !important;
  outline: none;
}
</style>
