<template>
  <div class="body">
    <h1 class="title">Strona główna</h1>
    <h1 class="subtitle">Najgorętsze filmy</h1>

    <div v-for="movie in hottestMovies" :key="movie.id" class="movie-list-item">
      <movie-box
        :movie="movie"
        @click="
          openMovieDetails(movie.get_absolute_url, movie.id, movie.clicked)
        "
      ></movie-box>
      <hr />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MovieBox from "../components/MovieBox.vue";

export default {
  components: { MovieBox },
  name: "Home",
  data() {
    return {
      hottestMovies: [],
    };
  },
  mounted() {
    document.title = "Filmarket | Strona główna";
    this.getHottestMovies();
  },
  methods: {
    async getHottestMovies() {
      await axios
        .get("/api/hottest-movies/")
        .then((response) => {
          this.hottestMovies = response.data.results;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    openMovieDetails(url, id, clicked) {
      axios
        .patch(`/api/movie-details/${id}`, {
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
