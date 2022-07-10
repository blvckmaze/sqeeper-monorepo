import { defineNuxtConfig } from "nuxt";

export default defineNuxtConfig({
  ssr: false,

  content: ["./pages/**/*.{html,js}", "./components/**/*.{html,js}"],

  typescript: {
    shim: false,
  },

  server: {
    port: 3000,
    host: "0.0.0.0",
    timing: false,
  },

  build: {
    postcss: {
      postcssOptions: {
        plugins: {
          tailwindcss: {},
          autoprefixer: {},
        },
      },
    },
  },

  css: ["~/assets/css/tailwind.css"],

  publicRuntimeConfig: {
    baseURL: process.env.BASE_URL || "https://nuxtjs.org",
  },
});
