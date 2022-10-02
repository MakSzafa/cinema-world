import { createStore } from "vuex";

export default createStore({
  state: {
    areCookiesAccepted: false,
    isAuthenticated: false,
    token: "",
    user: {
      id: null,
      email: "",
      favourite_genres: [],
      favourite_cinemas: [],
    },
    isLoading: false,
    cities: [],
    buildings: [],
    genres: [],
  },
  mutations: {
    initStore(state) {
      if (localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
      }
    },
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
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
    },
    setUser(state, user) {
      state.user = user;
    },
    removeUser(state) {
      state.user = {};
    },
  },
  actions: {},
  modules: {},
});
