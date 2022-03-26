<template>
  <div class="body">
    <h1 class="title">Szukam {{ this.$route.query.query }}</h1>

    <div v-for="movie in movies" :key="movie.id" class="movie-list-item">
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
import MovieBox from "@/components/MovieBox.vue";

export default {
  name: "SearchPage",
  components: {
    MovieBox,
  },
  data() {
    return {
      movies: [],
    };
  },
  mounted() {
    document.title = "Filmarket | Wyszukiwanie";
    this.performSearch();
  },
  methods: {
    async performSearch() {
      await axios
        .get(`http://127.0.0.1:8000/api/v1/movies-list/?search=${this.$route.query.query}`)
        .then((response) => {
          this.movies = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    openMovieDetails(url, id, clicked) {
      axios
        .patch(`http://127.0.0.1:8000/api/v1/movie-details/${id}`, {
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
.movie-list-item {
  width: 90vw;
  align-self: start;
  margin-left: 5rem;
}

.movie-box:hover {
  cursor: pointer;
  background-color: gray;
}

hr {
  border-top: 1px solid black;
}
</style>
