import { createStore } from 'vuex'

export default createStore({
  state: {
    areCookiesAccepted: false,
    isAuthenticated: false,
    token: '',
    id: null,
    user: {
      email: 'maniek918@gmail.com',
      favourite_genres: ['akcja', 'fantasy', 'romantyczne'],
      favourite_cinemas: [1, 4, 7],
    },
    isLoading: false,
  },
  mutations: {
    initStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.id = localStorage.getItem('id')
        state.isAuthenticated = true
      } else {
        state.token = ''
        state.id = null // TODO: zmien na null docelowo / zmien na cyfre do testow ale jakich?
        state.isAuthenticated = false
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    setId(state, id) {
      state.id = id
    },
    removeId(state) {
      state.id = null
    },
    setUser(state, user) {
      state.user = user
    },
    removeUser(state) {
      state.user = {} //TODO: czy potem bedzie dobrze nadpisywac jak sie ponownie zalogujesz?
    },
  },
  actions: {
  },
  modules: {
  }
})
