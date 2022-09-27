<template>
  <div class="body" id="body">
    <h1 class="title">Najczęściej zadawane pytania</h1>
    <div class="content-wrapper">
      <p class="question">P: Czy trzeba płacić za korzystanie ze strony?</p>
      <p class="answer">
        O: Korzystanie ze strony oraz rejestracja jest całkowicie bezpłatna.
      </p>
      <p class="question">P: Czemu na stronie nie ma kina X?</p>
      <p class="answer">
        O: Cały czas staram się rozbudowywać bazę obsługiwanych kin. Jeśli
        chcesz zaproponować swoje kino do dodania w serwisie daj mi o tym znać.
      </p>
      <p class="question">P: Czy trzeba płacić za korzystanie ze strony?</p>
      <p class="answer">
        O: Korzystanie ze strony oraz rejestracja jest całkowicie bezpłatna.
      </p>
      <p class="question">P: Czy trzeba płacić za korzystanie ze strony?</p>
      <p class="answer">
        O: Korzystanie ze strony oraz rejestracja jest całkowicie bezpłatna.
      </p>
      <p class="question">P: Czy trzeba płacić za korzystanie ze strony?</p>
      <p class="answer">
        O: Korzystanie ze strony oraz rejestracja jest całkowicie bezpłatna.
      </p>
      <p class="question">P: Czy trzeba płacić za korzystanie ze strony?</p>
      <p class="answer">
        O: Korzystanie ze strony oraz rejestracja jest całkowicie bezpłatna.
      </p>
      <p class="question">P: Czy trzeba płacić za korzystanie ze strony?</p>
      <p class="answer">
        O: Korzystanie ze strony oraz rejestracja jest całkowicie bezpłatna.
      </p>
    </div>
    <div class="arrow-up">
      <i
        class="fas fa-arrow-circle-up"
        style="color: #282a2a; font-size: 3rem; background-color: #979b9b"
        @click="goToTop()"
      ></i>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelpPage',
  mounted() {
    document.title = 'Filmarket | Pomoc'
  },
  methods: {
    goToTop() {
      document.getElementById('body').scrollIntoView({ behavior: 'smooth' })
    },
  }
}
</script>

<style scoped lang="scss">
.body {
  scroll-margin-top: 90px;
}

.content-wrapper {
  align-self: start;
  margin-left: 2rem;
}

.question {
  font-weight: bold;
}

.answer {
  margin-bottom: 1rem;
}

.arrow-up {
  align-self: end;
  position: sticky;
  right: 40px;
  bottom: 40px;
  z-index: 2;
  cursor: pointer;
}
</style>