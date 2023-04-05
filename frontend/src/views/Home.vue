<template>
  <div class="body-wrapper">
    <div class="body" v-if="!isLoading">
      <h1 class="title">Strona główna</h1>
      <h1 class="subtitle">Najgorętsze filmy</h1>

      <div v-for="movie in hottestMovies" :key="movie.id" class="movie-list-item">
        <movie-box :movie="movie" @click="openMovieDetails(movie.get_absolute_url, movie.id, movie.clicked)"></movie-box>
        <hr />
      </div>
    </div>
    <Loader v-if="isLoading"></Loader>
  </div>
</template>

<script>
import axios from "axios";
import MovieBox from "../components/MovieBox.vue";
import Loader from "../components/Loader.vue";

export default {
  components: {
    MovieBox,
    Loader
  },
  name: "Home",
  data() {
    return {
      hottestMovies: [],
      isLoading: false,
    };
  },
  mounted() {
    document.title = "Filmarket | Strona główna";
    this.getHottestMovies();
  },
  methods: {
    async getHottestMovies() {
      this.isLoading = true
      await axios
        .get("/api/hottest-movies/")
        .then((response) => {
          this.hottestMovies = response.data;
          this.isLoading = false
        })
        .catch((error) => {
          console.log(error);
        });
    },
    openMovieDetails(url, id, clicked) {
      axios
        .patch(`/api/movie-details/${id}/`, {
          clicked: clicked + 1,
        })
        .then(this.$router.push(url))
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped lang="scss">
@import "@/assets/main.scss";

.movie-list-item {
  width: 90vw;
  align-self: start;
  margin-left: auto;
}

.movie-box:hover {
  cursor: pointer;
  background-color: $grey-dark;
}

hr {
  height: 1px;
}
</style>
