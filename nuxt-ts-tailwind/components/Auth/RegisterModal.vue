<script lang="ts">
export default {
    props: ["modalOpen"],
};
</script>

<template>
  <AuthSubmitForm
    formName="register"
    :modalOpen="modalOpen"
  />
</template>
