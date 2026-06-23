<template>
  <!-- 表紙(1)と最終ページは下部中央の Eris × Nyx ロックアップを使うため右下フッターを隠す。
       $nav はテンプレート内でのみ確実に解決するため、ここで判定する -->
  <div class="nyx-footer" v-if="$nav.currentPage !== 1 && $nav.currentPage !== $nav.total">
    <img src="/images/nyx_logo.svg" alt="Nyx" class="nyx-logo" />
    <span class="page-number">{{ $nav.currentPage }}</span>
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
