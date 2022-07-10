<script lang="ts">
export default {
  props: ["modalOpen", "isValid"],

  data() {
    let title: string;
    let description: string;

    return { title, description };
  },

  methods: {
    isValid: (title: string): boolean => String(title).length >= 3,

    async submit(config = useRuntimeConfig()) {
      await fetch(config.baseURL.concat("/notes/create/"), {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({
          title: this.title,
          description: this?.description || "",
        }),
      }).then((response) => {
        if (!response.ok) {
          throw new Error("Something went wrong");
        }
      });
    },
  },
};
</script>

<template>
  <div class="modal" :class="{ 'modal-open': modalOpen }">
    <div class="card card-normal bg-base-100">
      <div class="card-body" style="min-width: 450px; min-height: 350px">
        <button
          class="btn btn-sm btn-circle absolute right-2 top-2"
          @click="$emit('update', false)"
        >
          <BIconX class="h-6 w-6" style="color: orangered" />
        </button>
        <form @submit.prevent="submit()">
          <h1 class="text-2xl text-center font-bold">Create a new note</h1>
          <div class="form-control py-5">
            <input
              v-model="title"
              name="title"
              type="text"
              required
              placeholder="Note title"
              class="input input-bordered w-full"
              maxlength="20"
            />
          </div>
          <div class="form-control">
            <textarea
              v-model="description"
              name="description"
              type="text"
              placeholder="Note description"
              class="textarea textarea-bordered h-48"
              maxlength="256"
            />
          </div>
          <div class="card-actions justify-end mt-6">
            <button
              type="submit"
              class="btn btn-primary"
              @click="$emit('update', false)"
              :disabled="!isValid(title)"
            >
              Create
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
