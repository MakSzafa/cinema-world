<template>
  <nav class="navbar">
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
                  placeholder="Wpisz miasto, kino lub nazwę filmu"
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
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link is-arrowless">Filtry</a>
          <navbar-filters></navbar-filters>
        </div>
      </div>
      <div class="navbar-end">
        <router-link to="/about" class="navbar-item info"
          >Informacje</router-link
        >

        <div class="navbar-item">
          <div class="buttons">
            <router-link
              to="/my-account"
              v-if="this.$store.state.auth.isAuthenticated"
              class="button is-light"
              >Moje konto</router-link
            >
            <router-link
              to="/login"
              v-if="!this.$store.state.auth.isAuthenticated"
              class="button is-light"
              >Zaloguj się</router-link
            >
            <router-link
              to="/register"
              v-if="!this.$store.state.auth.isAuthenticated"
              class="button is-success"
              >Zarejestruj się</router-link
            >
            <button
              v-if="this.$store.state.auth.isAuthenticated"
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
import NavbarFilters from "./NavbarFilters.vue";

export default {
  components: { NavbarFilters },
  name: "Header",

  data() {
    return {
      showMobileMenu: false,
    };
  },
  methods: {
    logOut() {
      this.$store.commit('logout')
      this.$store.commit('setUser', {})
      this.$router.push("/");

      document.getElementById("fav-cinemas").disabled = true;
      document.getElementById("fav-genres").disabled = true;
    },
  },
};
</script>

<style scoped lang="scss">
@import "@/assets/main.scss";

.navbar {
  position: sticky;
  top: 0;
  z-index: 2;
  .navbar-brand {
    .navbar-item {
      strong {
        color: $primary;
      }
    }
  }
}

.navbar-burger {
  height: auto;
  color: $primary !important;
}

.navbar-menu {
  flex-shrink: 1;
}

.navbar-start {
  margin-right: 6rem;
  .navbar-item {
    flex-shrink: 1;
    .icon {
      color: $grey-darker !important;
    }
    .navbar-link {
      background-color: $grey-darker;
      color: white;
    }
  }
  .is-hoverable:focus,
  .is-hoverable:focus-within,
  .is-hoverable:hover {
    .navbar-link,
    .navbar-link:focus,
    .navbar-link:focus-within,
    .navbar-link:hover {
      background-color: $grey-dark;
      color: white;
    }
    background-color: $grey-dark;
  }
}

.navbar-end {
  .info {
    color: white;
  }
  .info:focus {
    background-color: inherit;
    color: white;
  }
  .info:hover {
    background-color: $grey-dark;
    color: white;
  }

  .is-light,
  .is-light:focus {
    background-color: $grey-light;
    color: $text;
    box-shadow: none !important;
  }

  .is-light:hover {
    background-color: rgba(151, 155, 155, 0.7);
    color: $text;
  }

  .is-success:focus {
    box-shadow: none !important;
  }
}

@include touch {
  .navbar-burger:hover {
    color: inherit;
  }
  .navbar-menu {
    background-color: $grey-dark;
  }
  .navbar-start {
    .navbar-item {
      .navbar-link {
        background-color: $grey-dark;
        cursor: default;
      }
    }
  }
  .navbar-end {
    .info:focus {
      background-color: inherit;
      color: white;
    }
    .info:hover {
      background-color: $grey-darker;
      color: white;
    }
  }
}
</style>
