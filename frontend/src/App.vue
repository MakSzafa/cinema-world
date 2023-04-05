<template>
  <div id="app">
    <Header />
    <section class="section">
      <router-view />
    </section>
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";

export default {
  name: "App",
  components: {
    Header,
    Footer,
  },
  async beforeCreate() {
    await this.$store.dispatch("refreshAccessToken");

    if (localStorage.getItem("id")) {
      await this.$store.dispatch("getUser", localStorage.getItem("id"));

      localStorage.setItem("favCinemas", this.$store.state.users.user.favourite_cinemas);
      localStorage.setItem("favGenres", this.$store.state.users.user.favourite_genres);
    }

    axios
      .get("/api/buildings-list/")
      .then((response) => {
        let buildings = [];
        response.data.forEach((element) => {
          buildings.push(element.name);
        });
        this.$store.commit("setBuildings", buildings);
      })
      .catch((error) => {
        console.log(error);
      });

    axios
      .get("/api/genres-list/")
      .then((response) => {
        let genres = [];
        response.data.forEach((element) => {
          genres.push(element.name);
        });
        this.$store.commit("setGenres", genres);
      })
      .catch((error) => {
        console.log(error);
      });

    axios
      .get("/api/cities-list/")
      .then((response) => {
        let cities = [];
        response.data.forEach((element) => {
          cities.push(element.name);
        });
        this.$store.commit("setCities", cities);
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style lang="scss">
@import "@/assets/main.scss";

html {
  overflow-y: auto !important;
}

#app {
  min-height: 100vh;
  margin: 0;
  display: grid;
  grid-template-rows: auto 1fr auto;
  background-color: $grey-light;
}

.body {
  display: flex;
  flex-direction: column;
  align-items: center;
}

@include touch {
  #app {
    grid-template-rows: 1fr auto;
  }

  body {
    padding-top: 4.7rem !important;
  }
}
</style>
