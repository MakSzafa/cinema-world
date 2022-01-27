<template>
  <div class="body">
    <h1 class="title">Szukam {{ this.$route.query.query }}</h1>

    <MovieBox v-for="movie in movies" :key="movie.id" :movie="movie" />
  </div>
</template>

<script>
import axios from 'axios'
import MovieBox from '@/components/MovieBox.vue'

export default {
  name: 'SearchPage',
  components: {
    MovieBox
  },
  data() {
    return {
      movies: [],
    }
  },
  mounted() {
    document.title = 'Filmarket | Wyszukiwanie'

    // this.performSearch() TODO: api
  },
  methods: {
    async performSearch() {
      await axios
        .post("/api/v1/movies/search/", { 'query': this.$route.query.query })
        .then(response => {
          this.movies = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
}
</script>

<style scoped lang="scss">
</style>