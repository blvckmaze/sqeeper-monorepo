<script lang="ts">
definePageMeta({
  middleware: "auth",
});

export default {
  data() {
    let action: string;
    let responseData: Array<any>;
    let updateModalOpen: boolean;
    let createModalOpen: boolean;
    let noteId: number;
    let noteTitle: string;
    let noteDescription: string;

    return {
      action,
      responseData,
      updateModalOpen,
      createModalOpen,
      noteId,
      noteTitle,
      noteDescription,
    };
  },

  async created() {
    this.getNotesData();
  },

  methods: {
    isValid(attr?: any): boolean {
      if (typeof attr == "undefined" || attr.replace(/\s/g, "").length < 3) {
        return false;
      }
      return true;
    },

    refresh() {
      function delay(time: number) {
        return new Promise((resolve) => setTimeout(resolve, time));
      }

      delay(200).then(() => this.getNotesData());
    },

    async deleteNote(id: number, config = useRuntimeConfig()) {
      await fetch(config.baseURL.concat("/notes/delete/", String(id)), {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });

      this.refresh();
    },

    async getNotesData(config = useRuntimeConfig()) {
      const getResponse: Response = await fetch(
        config.baseURL.concat("/notes/view/all?format=json"),
        {
          headers: { "Content-Type": "application/json" },
          credentials: "include",
        }
      );

      this.responseData = getResponse ? await getResponse.json() : undefined;
    },

    updateModalState(modal: string, status?: boolean) {
      switch (modal) {
        case "create":
          this.createModalOpen = status;
          this.refresh();
        case "update":
          this.updateModalOpen = status;
          this.noteId = undefined;
          this.refresh();
      }
    },
  },
};
</script>

<template>
  <div>
    <NoteCreateForm
      :isValid="isValid"
      :modalOpen="createModalOpen"
      @update="updateModalState('create')"
    />
    <NoteUpdateForm
      :isValid="isValid"
      :modalOpen="updateModalOpen"
      :noteId="noteId"
      :title="noteTitle"
      :description="noteDescription"
      @update="updateModalState('update')"
    />
    <div
      class="
        grid grid-cols-1
        md:grid-cols-2
        lg:grid-cols-3
        xl:grid-cols-4
        gap-6
      "
    >
      <div
        v-for="entry in responseData"
        :key="entry.id"
        class="card w-90 bg-base-200 shadow-xl"
      >
        <div class="card-body">
          <label class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">
            <BIconX
              class="h-8 w-8"
              style="color: orangered"
              @click="deleteNote(entry.id)"
            />
          </label>
          <label
            class="btn btn-sm btn-circle btn-ghost absolute right-10 top-2"
          >
            <BIconPen
              class="h-4 w-4"
              @click="
                (updateModalOpen = true),
                  ([noteId, noteTitle, noteDescription] = [
                    entry.id,
                    entry.title,
                    entry.description,
                  ])
              "
            />
          </label>
          <h2 class="card-title pb-2">{{ entry.title }}</h2>
          <p style="white-space: pre-line">{{ entry.description }}</p>
          <div class="pt-6 card-actions justify-end">
            <i class="text-gray-500 text-sm">
              <template v-if="!entry?.updated_at">
                Created: {{ entry.created }}
              </template>
              <template v-else> Last update: {{ entry.updated_at }} </template>
            </i>
          </div>
        </div>
      </div>
    </div>
    <div class="absolute bottom-6 right-6" style="position: fixed">
      <button
        class="
          btn btn-ghost
          upper-case
          text-xl
          font-extrabold
          text-transparent
          bg-clip-text bg-gradient-to-r
          from-green-600
          to-lime-500
        "
        @click="createModalOpen = true"
      >
        Take a note!
      </button>
    </div>
  </div>
</template>
