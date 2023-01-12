import { createStore } from "vuex";

import users from "@/store/modules/users";
import auth from "@/store/modules/auth";

export default createStore({
  state: {
    isLoading: false,
    cities: [],
    buildings: [],
    genres: [],
  },
  mutations: {
    setIsLoading(state, status) {
      state.isLoading = status;
    },
    setCities(state, cities) {
      state.cities = cities;
    },
    setBuildings(state, buildings) {
      state.buildings = buildings;
    },
    setGenres(state, genres) {
      state.genres = genres;
    },
  },
  actions: {},
  modules: {
    users,
    auth,
  },
});
