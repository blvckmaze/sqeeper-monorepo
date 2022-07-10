<script lang="ts">
export default defineComponent({
  async beforeCreate(config = useRuntimeConfig()) {
    await fetch(config.baseURL.concat("/users/logout/"), {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
    }).then(this.$router.push("/auth/login"));
  },
});
</script>
