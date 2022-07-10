<!-- TODO -->

<script setup lang="ts">
var year: number = new Date().getFullYear();
</script>

<template>
  <footer class="footer footer-center p-3 bg-base-300 text-base-content">
    <div>
      <b class="font-extrabold text-lime-500"> [In development] </b>
      <p v-if="year > 2022">2022 - {{ year }}</p>
    </div>
  </footer>
</template>
