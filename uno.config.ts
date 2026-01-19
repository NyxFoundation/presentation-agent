import { defineConfig } from 'unocss'

export default defineConfig({
  theme: {
    colors: {
      primary: {
        DEFAULT: '#2563EB', // Royal Blue
        light: '#60A5FA',
        dark: '#1E40AF',
        bg: '#EFF6FF', // blue-50
      },
      secondary: {
        DEFAULT: '#9333EA', // Purple
        light: '#C084FC',
        dark: '#6B21A8',
        bg: '#F3E8FF', // purple-50
      },
      tertiary: {
        DEFAULT: '#E11D48', // Rose
        light: '#FB7185',
        dark: '#9F1239',
        bg: '#FFF1F2', // rose-50
      },
      success: {
        DEFAULT: '#059669', // Emerald
        light: '#34D399',
        dark: '#047857',
        bg: '#ECFDF5', // emerald-50
      },
      info: {
        DEFAULT: '#3B82F6', // Blue
        bg: '#EFF6FF',
      }
    }
  }
})
