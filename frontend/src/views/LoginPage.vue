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
          <input
            class="input"
            :class="{
              'is-danger': emailInvalid,
            }"
            type="email"
            v-model="email"
          />
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
          <input
            class="input"
            :class="{
              'is-danger': passwordInvalid,
            }"
            type="password"
            v-model="password"
          />
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

        localStorage.removeItem("token");

        const logUser = {
          username: this.email,
          password: this.password,
        };

        await axios
          .post("/api/v1/token/login/", logUser)
          .then((response) => {
            const token = response.data.auth_token;

            this.$store.commit("setToken", token);

            axios.defaults.headers.common["Authorization"] = "Token " + token;

            localStorage.setItem("token", token);

            const toPath = this.$route.query.to || "/";

            this.$router.push(toPath);
          })
          .catch((error) => {
            // TODO: odpowiedzi powinny ustawiac co jest zle - email / haslo !!!
            toast({
              message: "Błędne dane logowania",
              type: "is-danger",
              duration: 2000,
              position: "center",
              dismissible: true,
              pauseOnHover: true,
            });

            this.isLoading = false;
            if (error.response) {
              // Request made and server responded
              console.log(error.response.data);
              console.log(error.response.status);
              console.log(error.response.headers);
            } else if (error.request) {
              // The request was made but no response was received
              console.log(error.request);
            } else {
              // Something happened in setting up the request that triggered an Error
              console.log("Error", error.message);
            }
          });
        await axios
          .get("/api/v1/users/me")
          .then((response) => {
            localStorage.setItem("id", response.data.id);
          })
          .catch((error) => {
            console.log(error);
          });
        await axios
          .get(`/api/v1/profile/${localStorage.getItem("id")}`)
          .then((response) => {
            const user = {
              id: parseInt(localStorage.getItem("id")),
              email: this.email,
              favourite_genres: response.data.favourite_genres,
              favourite_cinemas: response.data.favourite_cinemas,
            };

            this.$store.commit("setUser", user);
          })
          .catch((error) => {
            console.log(error);
          });
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
