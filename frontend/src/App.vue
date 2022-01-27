<template>
  <div id="app">
    <Header />
    <section class="section">
      <router-view />
    </section>
    <Footer />
  </div>
</template>

<script>
import axios from 'axios'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

export default {
  components: {
    Header,
    Footer
  },
  beforeCreate() {
    this.$store.commit('initStore')

    if (this.$store.state.id) {
      axios
        .get("/api/v1/token/users/", this.$store.state.id)
        .then(response => {
          const user = response.data.user

          this.$store.commit('setUser', user)
        })
        .catch(error => {
          console.log(error)
        })
    } else {
      this.$store.commit('removeUser')
    }

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Bearer' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
}
</script>

<style lang="scss">
#app {
  min-height: 100vh;
  margin: 0;
  display: grid;
  grid-template-rows: auto 1fr auto;
}

.body {
  display: flex;
  flex-direction: column;
  align-items: center;
}

</style>
