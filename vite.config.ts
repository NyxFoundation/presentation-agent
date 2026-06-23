import { defineConfig } from 'vite'

export default defineConfig({
  optimizeDeps: {
    include: ['three', 'three-stdlib', '@tresjs/core', '@tresjs/cientos'],
  },
  server: {
    fs: { strict: false, allow: ['..', '.'] },
  },
} as any)
