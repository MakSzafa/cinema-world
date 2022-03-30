<template>
  <nav class="navbar is-dark">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item is-size-2 logo">
        <img src="@/assets/logo.png" alt="" height="28" width="28" />
        <strong>Cinemarket</strong>
      </router-link>

      <a
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbar-menu"
        :class="{ 'is-active': showMobileMenu }"
        @click="showMobileMenu = !showMobileMenu"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div
      class="navbar-menu"
      id="navbar-menu"
      :class="{ 'is-active': showMobileMenu }"
    >
      <div class="navbar-start">
        <div class="navbar-item">
          <form method="get" action="/search">
            <div class="field">
              <div class="control has-icons-right">
                <input
                  type="text"
                  class="input is-primary"
                  placeholder="Wpisz miasto lub nazwę filmu"
                  name="query"
                  size="40"
                />
                <span class="icon is-right">
                  <i class="fas fa-search"></i>
                </span>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="navbar-end">
        <router-link to="/about" class="navbar-item">Informacje</router-link>

        <div class="navbar-item">
          <div class="buttons">
            <router-link
              to="/my-account"
              v-if="this.$store.state.isAuthenticated"
              class="button is-light"
              >Moje konto</router-link
            >
            <router-link
              to="/login"
              v-if="!this.$store.state.isAuthenticated"
              class="button is-light"
              >Zaloguj się</router-link
            >
            <router-link
              to="/register"
              v-if="!this.$store.state.isAuthenticated"
              class="button is-success"
              >Zarejestruj się</router-link
            >
            <button
              v-if="this.$store.state.isAuthenticated"
              class="button is-danger"
              @click="logOut"
            >
              Wyloguj się
            </button>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import axios from "axios";

export default {
  name: "Header",

  data() {
    return {
      showMobileMenu: false,
    };
  },
  methods: {
    logOut() { 
      axios.defaults.headers.common["Authorization"] = "";
      // TODO: czy username i userid tutaj maja sens???
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");

      this.$store.commit("removeToken");

      this.$router.push("/");
    },
  },
};
</script>

<style scoped lang="scss">
.navbar {
  position: sticky;
  top: 0;
  z-index: 2;
}

.logo:hover,
.logo:focus {
  background-color: #363636 !important;
}
</style>
