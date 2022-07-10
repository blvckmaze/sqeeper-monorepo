<script lang="ts">
export default {
    props: ["modalOpen"],
};
</script>

<template>
  <AuthSubmitForm
    formName="login"
    :modalOpen="modalOpen"
  />
</template>
