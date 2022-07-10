<script setup lang="ts">
const route = useRoute();

useHead({
  title: "SQeeper",
  charset: "utf-8",
  link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.png" }],
});
</script>

<!-- TODO
<script lang="ts">
export default {
  errorCaptured(err) {
    console.log(err);
  },
};
</script> 
-->

<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<style>
input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus,
input:-webkit-autofill:active {
  transition: background-color 5000s ease-in-out 0s;
  -webkit-text-fill-color: white !important;
}

input:focus,
textarea:focus,
select:focus {
  outline: none;
}
</style>
