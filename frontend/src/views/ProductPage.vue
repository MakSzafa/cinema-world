<template>
  <div class="body-wrapper">
    <div class="body" v-if="!isLoading">
      <h1 class="title">{{ this.movie.name }}</h1>
      <div class="movie-details-grid">
        <img :src="this.movie.image" alt="" height="350" width="270" />
        <div class="movie-details">
          <div class="movie-info">
            <div class="movie-duration">
              <i class="fa-2x far fa-clock"></i>
              <div class="movie-duration-info">
                <h1 class="thema">Czas trwania:</h1>
                <h1>{{ this.movie.duration }}</h1>
              </div>
            </div>
            <div class="movie-genre">
              <i class="fa-2x fas fa-video"></i>
              <div class="movie-genre-info">
                <h1 class="thema">Gatunek:</h1>
                <h1 class="genre" v-for="genre in this.movie.genres" :key="genre.id">
                  {{ genre }}
                </h1>
              </div>
            </div>
          </div>
          <div class="movie-picker">
            <h1 class="subtitle">Wybierz swój seans:</h1>
            <div class="date-picker">
              <button v-for="date in this.movie.dates" :key="date.date" class="data-button" :id="date.date"
                @click="datePicked(date)">
                {{ date.date }}
              </button>
            </div>
            <div class="buildings-list">
              <div v-for="building in this.buildings" :key="building.building" class="building-container">
                <h1>{{ building.building.name }}</h1>
                <div v-for="version in building.versions" :key="version" class="version-container">
                  {{ version.version }} | {{ version.language }}
                  <div class="showtime-container">
                    <span v-for="showtime in version.schedule" :key="showtime" class="showtime">
                      {{ showtime.time }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="movie-description">
          <h1 class="thema">Opis filmu:</h1>
          <h1>{{ this.movie.description }}</h1>
        </div>
      </div>
    </div>
    <Loader v-if="isLoading"></Loader>
  </div>
</template>

<script>
import axios from "axios";
import Loader from "../components/Loader.vue";

export default {
  name: "ProductPage",
  components: {
    Loader
  },
  data() {
    return {
      movie: {},
      buildings: [],
      isLoading: false,
    };
  },
  mounted() {
    this.getMovieDetails();
  },
  methods: {
    async getMovieDetails() {
      this.isLoading = true
      await axios
        .get(`/api/movie-details/${this.$route.params.id}/`)
        .then((response) => {
          this.movie = response.data;
          this.$nextTick(() => {
            this.datePicked(response.data.dates[0])
          })
          document.title = "Filmarket | " + this.movie.name;
          this.isLoading = false
        })
        .catch((error) => {
          console.log(error);
        });
    },
    datePicked(date) {
      this.buildings = date.buildings

      this.movie.dates.forEach(element => {
        document.getElementById(`${element.date}`).classList.remove("active");

        if (element.date === date.date) {
          document.getElementById(`${date.date}`).classList.add("active");
        }
      });
    },
  },
};
</script>

<style scoped lang="scss">
@import "@/assets/main.scss";

.thema {
  font-weight: bold;
}

.movie-details-grid {
  display: grid;
  grid-template-columns: 20% 50% 30%;
  width: 90vw;

  @include widescreen {
    margin-left: 5rem;
    align-self: start;
  }

  @include touch {
    grid-template-columns: 270px 1fr;
  }

  @include mobile {
    img {
      height: 175px;
      width: 135px;
    }

    grid-template-columns: 135px 1fr;
  }

  @media screen and (max-width: 500px) {
    img {
      margin-left: auto;
      margin-right: auto;
      margin-bottom: 1rem;
    }
    grid-template-columns: 1fr;
  }
}

.movie-details {
  padding: 0 2rem;
  border-right: 1px solid;

  @include widescreen {
    padding: 0 3rem;
  }

  @include touch {
    margin-top: 2rem;
    grid-column: 1 / 3;
    border-right: none;
  }

  @include mobile {
    padding: 0 0;
  }

  @media screen and (max-width: 500px) {
    grid-column: 1 / 2;
  }
}

.movie-info {
  display: flex;
  column-gap: 5rem;

  @include touch {
    justify-content: center;
  }

  @include mobile {
    column-gap: 2rem;
  }
}

.movie-duration {
  display: grid;
  grid-template-columns: 50px 1fr;
  align-items: center;
  margin-bottom: 1rem;
}

.movie-genre {
  display: grid;
  grid-template-columns: 50px 1fr;
  align-items: center;
  margin-bottom: 1rem;

  .genre {
    display: inline-block;
    margin-left: 5px;
  }

  .genre:not(:last-child)::after {
    content: ",";
  }
}

.movie-description {
  margin-left: 2rem;

  @include touch {
    grid-row: 1;
    grid-column: 2;
  }

  @media screen and (max-width: 500px) {
    grid-row: 2;
    grid-column: 1 / 2;
  }
}

.movie-picker {
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  row-gap: 1rem;

  .date-picker {
    align-self: center;

    @include mobile {
      margin-left: 3rem;
    }
  }

  .data-button {
    width: 6rem;
    height: 2rem;
    font-weight: bold;
    background-color: white;
    cursor: pointer;
    border: 2px solid $text;
  }

  .active,
  .data-button:hover {
    background-color: $primary;
  }

  .data-button:not(:last-child) {
    border-right: none;
  }
}

.buildings-list {

  @include widescreen {
    margin-left: 3rem;
  }

  .building-container {
    h1 {
      color: $text;
      font-weight: bold;
    }
  }

  .version-container {
    margin-left: 2rem;
    font-weight: 400;
    display: grid;
    grid-template-columns: 120px 1fr;

    @include mobile {
      margin-left: 1rem;
    }
  }

  .showtime-container {
    display: flex;
    flex-wrap: wrap;
  }

  .showtime {
    margin-left: 2rem;
    color: $grey-dark;
  }
}
</style>
