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
          <div class="movie-genre">
            <i class="fa-2x fas fa-video"></i>
            <div class="movie-genre-info">
              <h1 class="thema">Gatunek:</h1>
              <h1
                class="genre"
                v-for="genre in this.movie.genres"
                :key="genre.id"
              >
                {{ genre }}
              </h1>
            </div>
          </div>
          <div class="movie-version">
            <div class="movie-version-info">
              <h1 class="thema">Wersja filmu:</h1>
              <h1>{{ this.movie.version }} | {{ this.movie.language }}</h1>
            </div>
          </div>
        </div>
        <div class="movie-picker">
          <h1 class="subtitle">Wybierz swój seans:</h1>
          <div class="select is-primary picker">
            <select name="cities" @change="cityChange($event)">
              <option value="">---Wybierz miasto---</option>
              <option v-for="city in this.cities" :value="city" :key="city">
                {{ city }}
              </option>
            </select>
          </div>
          <div v-if="isCityPicked" class="select is-primary picker">
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
          <div v-if="isBuildingPicked" class="select is-primary picker">
            <select name="dates" @change="dateChange($event)">
              <option value="">---Wybierz datę---</option>
              <option
                v-for="date in this.dates"
                :value="date.date"
                :key="date.id"
              >
                {{ date.date }}
              </option>
            </select>
          </div>
          <div v-if="isDatePicked" class="select is-primary picker">
            <select name="times" @change="timeChange($event)">
              <option value="">---Wybierz godzinę---</option>
              <option v-for="time in this.times" :value="time" :key="time">
                {{ time }}
              </option>
            </select>
          </div>
          <button v-if="isTimePicked" class="button is-dark">Kup bilety</button>
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
      dates: [],
      times: [],
      isCityPicked: false,
      isBuildingPicked: false,
      isDatePicked: false,
      isTimePicked: false,
    };
  },
  mounted() {
    this.getMovieDetails();
  },
  methods: {
    async getMovieDetails() {
      await axios
        .get(`/api/movie-details/${this.$route.params.id}`)
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
        this.isBuildingPicked = false;
        this.isDatePicked = false;
        this.isTimePicked = false;
      }
    },
    buildingChange(event) {
      this.dates = [];
      if (event.target.value !== "") {
        this.isBuildingPicked = true;
        for (let building of this.buildings) {
          if (building.building.name === event.target.value) {
            building.dates.forEach((element) => {
              this.dates.push(element);
            });
          }
        }
      } else {
        this.isBuildingPicked = false;
        this.isDatePicked = false;
        this.isTimePicked = false;
      }
    },
    dateChange(event) {
      this.times = [];
      if (event.target.value !== "") {
        this.isDatePicked = true;
        for (let date of this.dates) {
          if (date.date === event.target.value) {
            date.schedule[0].performance_times.forEach((element) => {
              this.times.push(element);
            });
          }
        }
      } else {
        this.isDatePicked = false;
        this.isTimePicked = false;
      }
    },
    timeChange(event) {
      console.log(event.target.value);
      if (event.target.value !== "") {
        this.isTimePicked = true;
        // TODO: create link to redirect page
      } else {
        this.isTimePicked = false;
      }
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
  grid-template-columns: 270px 2fr 1fr;
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
}

.movie-info {
  display: flex;
  justify-content: space-between;
  column-gap: 1rem;
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

.movie-version {
  display: grid;
  grid-template-columns: 1fr;
  align-items: center;
  margin-bottom: 1rem;
}
.movie-description {
  margin-left: 2rem;
  @include touch {
    grid-row: 1;
    grid-column: 2;
  }
}

.movie-picker {
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  row-gap: 1rem;
  h1 {
    align-self: flex-start;
  }
  .picker {
    width: 250px;
    select {
      width: 100%;
    }
  }
}
</style>
