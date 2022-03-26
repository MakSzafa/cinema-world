<template>
  <div class="body">
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
          <div class="movie-genre-version">
            <i class="fa-2x fas fa-video"></i>
            <div class="movie-genre-info">
              <h1 class="thema">Gatunek:</h1>
              <h1>{{ this.movie.genre }}</h1>
            </div>
            <div class="movie-version-info">
              <h1 class="thema">Wersja filmu:</h1>
              <h1>{{ this.movie.version }} | {{ this.movie.language }}</h1>
            </div>
          </div>
        </div>
        <div class="movie-picker">
          <h1 class="subtitle">Wybierz swój seans:</h1>
          <div class="select">
            <select name="cities" @change="cityChange($event)">
              <option value="">---Wybierz miasto---</option>
              <option v-for="city in cities" :value="city" :key="city">
                {{ city }}
              </option>
            </select>
          </div>
          <div class="select" :class="{ 'is-hidden': !isCityPicked }">
            <select name="buildings" @change="buildingChange($event)">
              <option value="">---Wybierz budynek---</option>
              <option
                v-for="building in this.buildings"
                :value="building.building.name"
                :key="building.building.id"
              >
                {{ building.building.name }}
              </option>
            </select>
          </div>
          <!-- <div>Wybierz swoj seans: miasto budynek date-picker time-picker</div> -->
        </div>
      </div>
      <div class="movie-description">
        <h1>{{ this.movie.description }}</h1>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProductPage",
  data() {
    return {
      movie: {},
      cities: [],
      buildings: [],
      isCityPicked: false,
    };
  },
  mounted() {
    this.getMovieDetails();
  },
  methods: {
    async getMovieDetails() {
      await axios
        .get(
          `http://127.0.0.1:8000/api/v1/movie-details/${this.$route.params.id}`
        )
        .then((response) => {
          this.movie = response.data;
          for (let building of response.data.buildings) {
            if (this.cities.indexOf(building.building.city) === -1) {
              this.cities.push(building.building.city);
            }
          }
          document.title = "Filmarket | " + this.movie.name;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    cityChange(event) {
      this.buildings = [];
      if (event.target.value !== "") {
        this.isCityPicked = true;
        for (let building of this.movie.buildings) {
          if (building.building.city === event.target.value) {
            this.buildings.push(building);
          }
        }
      } else {
        this.isCityPicked = false;
      }
    },
    // TODO: to samo dla budynkow dat i godzin - czekamy na gotowe komponenty vuetify
    buildingChange(event) {
      console.log(event.target.value);
    },
  },
};
</script>

<style scoped lang="scss">
.thema {
  font-weight: bold;
}

.movie-details-grid {
  display: grid;
  grid-template-columns: 270px 2fr 1fr;
  width: 90vw;
  align-self: start;
  margin-left: 5rem;
}

.movie-details {
  margin-left: 3rem;
  border-right: 1px solid;
}

.movie-info {
  display: grid;
  grid-template-columns: 1fr 2fr;
}

.movie-duration {
  display: grid;
  grid-template-columns: 50px 1fr;
  align-items: center;
  margin-bottom: 1rem;
}

.movie-genre-version {
  display: grid;
  grid-template-columns: 50px 1fr 1fr;
  align-items: center;
  margin-bottom: 1rem;
}

.movie-description {
  margin-left: 2rem;
}

.movie-picker {
  margin-top: 2rem;
}
</style>
