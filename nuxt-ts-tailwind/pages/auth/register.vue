<script lang="ts">
definePageMeta({
  layout: "auth",
  middleware: "auth",
});

export default {
  data() {
    let modalOpen: boolean;
    return { modalOpen };
  },

  mounted() {
    this.modalOpen = true;
  },
};
</script>

<template>
  <AuthRegisterModal :modalOpen="modalOpen" />
</template>
