<template>
  <!-- 本文スライド: 右下に Merkle Japan ロゴ＋ページ番号 (1 ページ目はページ番号なし)。
       $nav はテンプレート内でのみ確実に解決する（script setup 内だと全ページで誤作動する）。 -->
  <div class="mj-footer">
    <img src="/images/merklejapan_logo.png" alt="Merkle Japan" class="mj-logo" />
    <span v-if="$nav.currentPage !== 1" class="page-number">{{ $nav.currentPage }}</span>
  </div>
</template>

<style scoped>
.mj-footer {
  position: fixed;
  bottom: 16px;
  right: 24px;
  z-index: 100;
  display: flex;
  align-items: center;
  gap: 8px;
  pointer-events: none;
}

.mj-logo {
  width: 96px;
  height: auto;
  opacity: 0.9;
}

.page-number {
  font-family: 'BIZ UDPMincho', serif;
  font-size: 14px;
  color: #000000;
  margin-left: 8px;
}
</style>
