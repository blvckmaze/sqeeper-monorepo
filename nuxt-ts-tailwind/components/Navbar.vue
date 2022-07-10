
<script lang="ts">
import { getUserData } from `@/utils/helpers`;

export default {
  data() {
    let firstName: string;
    let lastName: string;

    return { firstName, lastName };
  },

  created() {
    this.setUserData()
  },

  methods: {
    async setUserData(data = getUserData()): Promise<void> {
      let response = await data

      this.firstName = response.first_name
      this.lastName = response.last_name
    },
  },
};
</script>

<template>
  <div class="navbar bg-base-100">
    <div class="flex-1">
      <a
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
      >
        SQeeper
      </a>
    </div>
    <div class="flex-none gap-2">
      <div class="dropdown dropdown-end">
        <label tabindex="0" class="btn btn-ghost btn-circle">
          <BIconList class="h-5 w-5" />
        </label>
        <ul
          tabindex="0"
          class="
            mt-3
            p-2
            shadow
            menu menu-compact
            dropdown-content
            bg-base-100
            rounded-box
            w-52
          "
        >
          <span class="text-sm py-2" style="text-align: center">
            Hi, {{ firstName + " " + lastName }}
          </span>
          <li>
            <NuxtLink to="/auth/logout">Logout</NuxtLink>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
