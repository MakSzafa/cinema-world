<template>
  <div class="body">
    <h1 class="title">Zaloguj się</h1>
    <form @submit.prevent="submitForm">
      <div class="field">
        <label class="label">E-mail</label>
        <div class="control has-icons-left has-icons-right">
          <span class="icon is-left">
            <i class="fas fa-envelope"></i>
          </span>
          <input class="input" :class="{
            'is-danger': emailInvalid,
          }" type="email" v-model="email" />
          <span v-if="emailInvalid" class="icon is-right">
            <i class="fas fa-exclamation-triangle"></i>
          </span>
          <p v-if="emailInvalid" class="help is-danger">
            Podany adres e-mail jest niepoprawny
          </p>
        </div>
      </div>
      <div class="field">
        <label class="label">Hasło</label>
        <div class="control has-icons-left has-icons-right">
          <span class="icon is-left">
            <i class="fas fa-lock"></i>
          </span>
          <input class="input" :class="{
            'is-danger': passwordInvalid,
          }" type="password" v-model="password" />
          <span v-if="passwordInvalid" class="icon is-right">
            <i class="fas fa-exclamation-triangle"></i>
          </span>
          <p v-if="passwordInvalid" class="help is-danger">
            Podane hasło jest niepoprawne
          </p>
        </div>
      </div>
      <div class="field submit-button">
        <div class="control">
          <button class="button is-dark" :class="{ 'is-loading': isLoading }">
            Zaloguj się
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
      emailInvalid: false,
      passwordInvalid: false,
      isLoading: false,
    };
  },
  mounted() {
    document.title = "Filmarket | Zaloguj się";
  },
  methods: {
    async submitForm() {
      if (!this.emailInvalid && !this.passwordInvalid) {
        this.isLoading = true;

        axios.defaults.headers.common["Authorization"] = "";

        localStorage.removeItem("accessToken");

        const logUser = {
          email: this.email,
          password: this.password,
        };

        try {
          const response = await axios.post("/api/token/", logUser);
          this.$store.commit("login", response.data);
          this.$store.commit("setAuthError", false);

          const toPath = this.$route.query.to || "/";

          this.$router.push(toPath);

          document.getElementById("fav-cinemas").disabled = false;
          document.getElementById("fav-genres").disabled = false;

          await this.$store.dispatch("getUser", localStorage.getItem("id"));
        } catch (e) {
          this.$store.commit("setAuthError", true);
          console.log(e);
          // TODO: add info about what is wrong - email / password
          toast({
            message: "Błędne dane logowania",
            type: "is-danger",
            duration: 2000,
            position: "center",
            dismissible: true,
            pauseOnHover: true,
          });
          this.isLoading = false;
        }
      }
    },
  },
};
</script>

<style scoped lang="scss">
.submit-button {
  text-align: center;
}
</style>
