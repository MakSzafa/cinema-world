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
      favCinemasFilterPassed: false,
      favGenresFilterPassed: false,
      filteredCitiesFilterPassed: false,
      filteredGenresFilterPassed: false,
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
        .get(`/api/v1/movies-list/?search=${this.$route.query.query}`)
        .then((response) => {
          if (localStorage.getItem("useFavCinemas") === "true") {
            const favCinemas = localStorage.getItem("favCinemas").split(",");

            response.data.forEach((element) => {
              for (let building of element.buildings) {
                if (favCinemas.includes(building.building.name)) {
                  this.movies.push(element);
                  break;
                }
              }
            });
            this.favCinemasFilterPassed = true;
          } else if (localStorage.getItem("useFavGenres") === "true") {
            const favGenres = localStorage.getItem("favGenres").split(",");

            response.data.forEach((element) => {
              for (let genre of element.genres) {
                if (favGenres.includes(genre)) {
                  this.movies.push(element);
                  break;
                }
              }
            });
            this.favGenresFilterPassed = true;
          } else if (localStorage.getItem("filteredCities") !== "") {
            const filteredCities = localStorage
              .getItem("filteredCities")
              .split(",");

            response.data.forEach((element) => {
              for (let city of element.buildings) {
                if (filteredCities.includes(city.building.city)) {
                  this.movies.push(element);
                  break;
                }
              }
            });
            this.filteredCitiesFilterPassed = true;
          } else if (localStorage.getItem("filteredGenres") !== "") {
            const filteredGenres = localStorage
              .getItem("filteredGenres")
              .split(",");

            response.data.forEach((element) => {
              for (let genre of element.genres) {
                if (filteredGenres.includes(genre)) {
                  this.movies.push(element);
                  break;
                }
              }
            });
            this.filteredGenresFilterPassed = true;
          }

          if (
            !this.favGenresFilterPassed &&
            localStorage.getItem("useFavGenres") === "true"
          ) {
            const favGenres = localStorage.getItem("favGenres").split(",");

            this.movies.forEach((element) => {
              let included = false;

              for (let genre of element.genres) {
                if (favGenres.includes(genre)) {
                  included = true;
                  break;
                }
              }
              if (!included) {
                this.movies = this.movies.filter(
                  (e) => e.name !== element.name
                );
              }
            });
            this.favGenresFilterPassed = true;
          }
          if (
            !this.filteredCitiesFilterPassed &&
            localStorage.getItem("filteredCities") !== ""
          ) {
            const filteredCities = localStorage
              .getItem("filteredCities")
              .split(",");

            this.movies.forEach((element) => {
              let included = false;

              for (let city of element.buildings) {
                if (filteredCities.includes(city.building.city)) {
                  included = true;
                  break;
                }
              }
              if (!included) {
                this.movies = this.movies.filter(
                  (e) => e.name !== element.name
                );
              }
            });
            this.filteredCitiesFilterPassed = true;
          }
          if (
            !this.filteredGenresFilterPassed &&
            localStorage.getItem("filteredGenres") !== ""
          ) {
            const filteredGenres = localStorage
              .getItem("filteredGenres")
              .split(",");

            this.movies.forEach((element) => {
              let included = false;

              for (let genre of element.genres) {
                if (filteredGenres.includes(genre)) {
                  included = true;
                  break;
                }
              }
              if (!included) {
                this.movies = this.movies.filter(
                  (e) => e.name !== element.name
                );
              }
            });
            this.filteredGenresFilterPassed = true;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    openMovieDetails(url, id, clicked) {
      axios
        .patch(`/api/v1/movie-details/${id}`, {
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
