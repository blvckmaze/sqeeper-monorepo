<script lang="ts">
export default {
  props: ["modalOpen", "noteId", "title", "description", "isValid"],

  methods: {
    async submit(id: number, config = useRuntimeConfig()) {
      await fetch(config.baseURL.concat("/notes/update/", String(id)), {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({
          title: this.title,
          description: this.description,
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
        <form method="dialog">
          <h1 class="text-2xl text-center font-bold">Update note</h1>
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
              class="btn btn-primary"
              @click="submit(noteId), $emit('update', false)"
              :disabled="!isValid(title)"
            >
              Update
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
