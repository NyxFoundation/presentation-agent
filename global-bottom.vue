<template>
  <!-- 表紙(1)・最終ページ: Nyx ロゴを下部中央に。本文スライド: 右下に Nyx ロゴ＋ページ番号。
       $nav はテンプレート内でのみ確実に解決する（script setup 内だと誤作動する）。 -->
  <div v-if="$nav.currentPage === 1 || $nav.currentPage === $nav.total" class="nyx-center">
    <img src="/images/nyx_logo.svg" alt="Nyx Foundation" class="nyx-logo-c" />
  </div>
  <div v-else class="nyx-footer">
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

.nyx-center {
  position: fixed;
  bottom: 30px;
  left: 0;
  right: 0;
  z-index: 100;
  display: flex;
  justify-content: center;
  pointer-events: none;
}

.nyx-logo-c {
  width: 170px;
  height: auto;
}
</style>
