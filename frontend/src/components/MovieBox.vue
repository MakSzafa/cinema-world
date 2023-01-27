<template>
  <div class="movie-box">
    <img :src="movie.image" alt="" height="200" width="130" />
    <div class="movie-info">
      <h1>{{ movie.name }}</h1>
      <h2>
        <span>Gatunek:</span>
        <h2 class="genre" v-for="genre in movie.genres" :key="genre.id">
          {{ genre }}
        </h2>
      </h2>
      <h2><span>Czas trwania:</span> {{ movie.duration }}</h2>
      <h2>
        <span>Opis filmu:</span> {{ movie.description }}
      </h2>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieBox",
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped lang="scss">
span {
  font-weight: bold;
}

h1 {
  margin-left: 4rem;
  margin-bottom: 1rem;
  font-size: 2rem;
  font-weight: bold;
  text-transform: uppercase;
  text-decoration: underline;
}

h2 {
  margin-left: 2rem;
  font-size: 1.2rem;
}

.genre {
  display: inline-block;
  margin-left: 5px;
}

h2 .genre:not(:last-child)::after {
  content: ",";
}

.movie-box {
  display: grid;
  grid-template-columns: 130px auto;
}

.movie-info {
  margin-left: 1rem;
}
</style>
