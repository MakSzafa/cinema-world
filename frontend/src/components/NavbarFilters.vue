<template>
  <div class="navbar-dropdown is-right">
    <div class="navbar-item">
      <label class="checkbox">
        <input type="checkbox" value="true" id="fav-cinemas" v-model="useFavCinemas" />
        Ulubione kina
      </label>
      <label class="checkbox">
        <input type="checkbox" value="true" id="fav-genres" v-model="useFavGenres" />
        Ulubione gatunki
      </label>
    </div>
    <hr class="navbar-divider" />
    <div class="navbar-item">
      <h1>Filtruj miasta:</h1>
      <label v-for="city in this.$store.state.cities" :key="city" class="checkbox">
        <input type="checkbox" :value="city" :id="city" v-model="filteredCities" />
        {{ city }}
      </label>
    </div>
    <hr class="navbar-divider" />
    <div class="navbar-item">
      <h1>Filtruj gatunki:</h1>
      <label v-for="genre in this.$store.state.genres" :key="genre" class="checkbox">
        <input type="checkbox" :value="genre" :id="genre" v-model="filteredGenres" />
        {{ genre }}
      </label>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavbarFilters",

  data() {
    return {
      filteredCities: [],
      filteredGenres: [],
      useFavCinemas: "",
      useFavGenres: "",
    };
  },
  mounted() {
    if (localStorage.getItem("accessToken")) {
      document.getElementById("fav-cinemas").disabled = false;
      document.getElementById("fav-genres").disabled = false;

      this.useFavCinemas = localStorage.getItem("useFavCinemas");
      this.useFavGenres = localStorage.getItem("useFavGenres");
    } else {
      document.getElementById("fav-cinemas").disabled = true;
      document.getElementById("fav-genres").disabled = true;
    }

    if (localStorage.getItem("filteredCities")) {
      this.filteredCities = localStorage.getItem("filteredCities").split(",");
    }

    if (localStorage.getItem("filteredGenres")) {
      this.filteredGenres = localStorage.getItem("filteredGenres").split(",");
    }
  },
  updated() {
    if (localStorage.getItem("accessToken")) {
      document.getElementById("fav-cinemas").disabled = false;
      document.getElementById("fav-genres").disabled = false;

      localStorage.setItem("useFavCinemas", this.useFavCinemas);
      localStorage.setItem("useFavGenres", this.useFavGenres);
    } else {
      document.getElementById("fav-cinemas").disabled = true;
      document.getElementById("fav-genres").disabled = true;
    }

    localStorage.setItem("filteredCities", this.filteredCities);
    localStorage.setItem("filteredGenres", this.filteredGenres);
  },
};
</script>

<style scoped lang="scss">
@import "@/assets/main.scss";

.navbar-item {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  justify-items: start;

  h1 {
    grid-column: 1 / 4;
    place-self: center;
    margin-bottom: 0.4rem;
    user-select: none;
  }

  label {
    margin-right: 1rem;
    margin-bottom: 0.3rem;
    user-select: none;
  }
}

.navbar-item:first-of-type {
  grid-template-columns: 1fr 1fr;
}

@include mobile {
  .navbar-item {
    grid-template-columns: 1fr 1fr;

    h1 {
      grid-column: 1 / 3;
    }
  }
}
@include touch {
  .navbar-dropdown {
    .navbar-item {
      color: white;

      label {
        margin-right: 0;
      }

      .checkbox:hover {
        color: $link;
      }
    }
  }
}

@include desktop {
  .navbar-dropdown {
    overflow-y: auto;
    max-height: 80vh;
  }
}
</style>
