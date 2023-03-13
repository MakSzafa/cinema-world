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
      <p class="question">P: Czemu na stronie nie można kupić biletów na filmy?</p>
      <p class="answer">
        O: Na ten moment serwis nie sprzedaje biletów, a jedynie pozwala na sprawdzenie repertuaru. Być może w przyszłości
        będzie możliwość bespośredniego zakupu biletów na stronie.
      </p>
      <p class="question">P: Dlaczego na stronie nie ma wszystkich filmów?</p>
      <p class="answer">
        O: Ze względu na to, że wszystkie filmy dodaje własnoręcznie czasem może wystąpić opóźnienie w pojawieniu się
        jakiegoś tytułu lub aktualizacji repertuaru.
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelpPage",
  mounted() {
    document.title = "Filmarket | Pomoc";
  },
};
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
</style>
