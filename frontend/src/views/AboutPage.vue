<template>
  <div class="body">
    <h1 class="title">Informacje o stronie</h1>

    <p style="margin-bottom: 15px">
      <span><i class="fas fa-film" style="color: #970c0f"></i></span>
      <span><i class="fas fa-film" style="color: #970c0f"></i></span>
      Strona została stworzona z myślą o użytkownikach kin i ma na celu
      ułatwienie im znalezienia dogodnego seansu.
      <span><i class="fas fa-film" style="color: #970c0f"></i></span>
      <span><i class="fas fa-film" style="color: #970c0f"></i></span>
    </p>
    <p>
      <span><i class="far fa-file-code" style="color: #006400"></i></span>
      Strona jest obecnie w fazie deweloperskiej, dlatego będę wdzięczny za
      wszelkie uwagi oraz pomysły jak można ją usprawnić.
      <span><i class="far fa-file-code" style="color: #006400"></i></span>
    </p>
    <p style="color: #970c0f; font-size: 1.4rem">
      Na ten moment strona obsługuje kina sieci Cinema City, Helios oraz
      Multikino i pozwala jedynie na przeglądanie repertuaru. Repertuar nie jest regularnie aktualizowany, ponieważ kina
      nie udostępniają dostępu do swojej bazy danych. W przyszłości chciałbym wprowadzić również możliwość
      bezpośredniego zakupu biletów.
    </p>
    <p>
      Chciałbyś / chciałabyś, aby Twoje ulubione kino również znalazło się na
      tej liście?
    </p>
    <p>Może brakuje Ci jakiejś funkcji, która ułatwiłaby pracę ze stroną?</p>
    <p>Może widzisz, że jakaś funkcjonalność mogłaby działać lepiej?</p>
    <p style="color: #006400; margin-bottom: 15px; font-size: 1.4rem">
      Nie wahaj się i daj mi o tym znać. Uwagi i pomysły proszę wysyłać drogą
      mailową.
    </p>
    <p>
      <span><i class="fas fa-dollar-sign" style="color: #006400"></i></span>
      Jeśli chciałbyś wesprzeć projekt finansowo, poniżej znajduje się odnośnik
      do strony, która to umożliwia.
      <span><i class="fas fa-dollar-sign" style="color: #006400"></i></span>
    </p>
    <a href="https://buycoffee.to/maniek_programista" target="_blank"><img
        src="https://buycoffee.to/btn/buycoffeeto-btn-primary.svg" style="width: 150px"
        alt="Postaw mi kawę na buycoffee.to" /></a>
  </div>
</template>

<script>
export default {
  name: "AboutPage",
  mounted() {
    document.title = "Filmarket | Informacje";
  },
};
</script>

<style scoped lang="scss">
p {
  font-size: 1.2rem;
  text-align: center;
  font-weight: bold;
}

a {
  margin: 1rem;
}
</style>
