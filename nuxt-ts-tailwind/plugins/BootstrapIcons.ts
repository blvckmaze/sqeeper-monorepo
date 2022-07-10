import { BootstrapIconsPlugin } from 'bootstrap-icons-vue';

export default defineNuxtPlugin(nuxtApp => {
    nuxtApp.vueApp.use(BootstrapIconsPlugin)
})
