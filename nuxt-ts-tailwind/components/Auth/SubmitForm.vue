<script lang="ts">
import { validateInput } from `@/utils/validators`;
import {
  generateRequestInfo,
  generateRequestBody,
} from "@/utils/apiAuthRequests";

export default {
  props: ["formName", "modalOpen"],

  data() {
    let header: string;
    let button: string;
    let email: string;
    let password: string;
    let firstName: string;
    let lastName: string;

    return { header, button, email, password, firstName, lastName };
  },

  created() {
    this.setFormContent(this.formName);
  },

  methods: {
    isValid(formName: string = this.formName): boolean {
      switch (formName) {
        case "login":
          return validateInput(this.email, this.password);
        case "register":
          return validateInput(this.email, this.password, [
            this.firstName,
            this.lastName,
          ]);
      }
    },

    async submit(
      config = useRuntimeConfig(),
      formName: string = this.formName
    ) {
      let endpoint: string;

      switch (formName) {
        case "login":
          endpoint = "/users/login/";

          return await fetch(
            config.baseURL.concat(endpoint),
            generateRequestInfo(
              endpoint,
              "POST",
              generateRequestBody(this.email, this.password)
            )
          ).then((response) => {
            return response.ok
              ? this.$router.push("/")
              : new Error("Something went wrong");
          });

        case "register":
          endpoint = "/users/register/";

          return await fetch(
            config.baseURL.concat(endpoint),
            generateRequestInfo(
              endpoint,
              "POST",
              generateRequestBody(
                this.email,
                this.password,
                this.firstName,
                this.lastName
              )
            )
          ).then((response) => {
            return response.ok
              ? this.$router.push("/auth/login")
              : new Error("Something went wrong");
          });
      }
    },

    setFormContent(formName: string = this.formName): void {
      switch (formName) {
        case "login":
          this.header = "Sign in to your account";
          this.button = "Login";
          break;
        case "register":
          this.header = "Register a new account";
          this.button = "Register";
          break;
      }
    },
  },
};
</script>

<template>
  <div class="modal" :class="{ 'modal-open': modalOpen }">
    <div class="hero min-h-screen bg-base-200">
      <div class="hero-content flex-col lg:flex-row-reverse">
        <div id="logo" class="text-center">
          <img src="/favicon.png" style="width: 70%; height: 70%" />
        </div>
        <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
          <div class="card-body">
            <form class="mt-0 space-y-4" @submit.prevent="submit()">
              <div class="form-control">
                <h1 class="text-2xl text-center font-bold py-6">
                  {{ header }}
                </h1>
                <input
                  v-model="email"
                  name="email"
                  type="email"
                  required
                  autocomplete="email"
                  placeholder="Email address"
                  class="input input-bordered w-full"
                />
              </div>
              <div class="form-control">
                <input
                  v-model="password"
                  name="password"
                  type="password"
                  required
                  placeholder="Password"
                  autocomplete="current-password"
                  class="input input-bordered w-full"
                />
              </div>
              <template v-if="formName === 'register'">
                <div class="form-control">
                  <input
                    v-model="firstName"
                    name="first_name"
                    type="text"
                    required
                    placeholder="First name"
                    class="input input-bordered w-full"
                  />
                </div>
                <div class="form-control">
                  <input
                    v-model="lastName"
                    name="last_name"
                    type="text"
                    required
                    placeholder="Last name"
                    class="input input-bordered w-full"
                  />
                </div>
              </template>
              <div class="form-control mt-6">
                <button
                  type="submit"
                  class="btn btn-primary"
                  :disabled="!isValid()"
                >
                  {{ button }}
                </button>
              </div>
              <div class="text-center text-sm text-primary">
                <NuxtLink v-if="formName === 'register'" to="/auth/login">
                  Already have an account? Login now!
                </NuxtLink>

                <NuxtLink v-if="formName === 'login'" to="/auth/register">
                  Don't have an account? Create one!
                </NuxtLink>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@media (max-width: 1100px) {
  #logo {
    display: none;
  }
}
</style>