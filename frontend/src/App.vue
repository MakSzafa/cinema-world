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
  components: {
    Header,
    Footer,
  },
  beforeCreate() {
    this.$store.commit("initStore");

    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }

    if (localStorage.getItem("id")) {
      axios
        .get("/api/v1/users/me")
        .then((response) => {
          localStorage.setItem("id", response.data.id);

          axios
            .get(`/api/v1/profile/${localStorage.getItem("id")}`)
            .then((response2) => {
              const user = {
                id: response.data.id,
                email: response.data.email,
                favourite_genres: response2.data.favourite_genres,
                favourite_cinemas: response2.data.favourite_cinemas,
              };

              this.$store.commit("setUser", user);
            })
            .catch((error) => {
              console.log(error);
            });
        })
        .catch((error) => {
          console.log(error);
        });
    } else {
      this.$store.commit("removeUser");
    }

    axios
      .get("/api/v1/buildings-list")
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
      .get("/api/v1/genres-list")
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
      .get("/api/v1/cities-list")
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
</style>
