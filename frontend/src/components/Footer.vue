<template>
  <footer class="footer">
    <section class="columns">
      <div class="column is-three-fifths">
        <p class="footer-header">Filmarket.pl</p>
        <ul class="footer-list">
          <li class="footer-list-el">
            <router-link to="/help" class="footer-link">Pomoc</router-link>
          </li>
          <li class="footer-list-el">
            <router-link to="/regulations" class="footer-link">Regulamin</router-link>
          </li>
        </ul>
      </div>
      <div class="column">
        <p class="contact-header">Kontakt</p>
        <ul class="contact-list">
          <li class="footer-list-el">
            <span class="icon">
              <i class="far fa-envelope"></i>
            </span>
            <span class="">E-mail: kontakt@makszafa.pl</span>
          </li>
          <li class="footer-list-el">
            <span class="icon">
              <i class="fab fa-facebook-square"></i>
            </span>
            <a href="https://www.facebook.com/" target="_blank" class="footer-link">Facebook</a>
          </li>
          <li class="footer-list-el">
            <span class="icon">
              <i class="fab fa-instagram"></i>
            </span>
            <a href="https://www.instagram.com/" target="_blank" class="footer-link">Instagram</a>
          </li>
          <li class="footer-list-el">
            <span class="icon">
              <i class="fab fa-twitter-square"></i>
            </span>
            <a href="https://www.twitter.com/" target="_blank" class="footer-link">Twitter</a>
          </li>
          <li class="footer-list-el">
            <span class="icon">
              <i class="fab fa-discord"></i>
            </span>
            <a href="https://www.discord.com/" target="_blank" class="footer-link">Discord</a>
          </li>
        </ul>
      </div>
    </section>
    <section class="section copyright">
      <p class="has-text-centered">
        Korzystanie z portalu oznacza zaakceptowanie
        <router-link to="/regulations" class="footer-link">Regulaminu</router-link>.
      </p>
      <p class="has-text-centered">
        Opublikowane na stronie <router-link to="/" class="footer-link">www.filmarket.makszafa.pl</router-link>
        informacje lub ceny nie
        stanowią oferty w rozumieniu przepisów kodeksu cywilnego.
      </p>
      <p class="has-text-centered">Copyright © 2022 by Filmarket Sp. z o.o.</p>
    </section>
  </footer>
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style scoped lang="scss">
@import "@/assets/main.scss";

.footer-header {
  color: $primary;
  text-align: center;
  margin-bottom: 0.3rem;
  font-size: 1.3rem;
  font-weight: bold;
}

.contact-header {
  color: $primary;
  text-align: left;
  margin-bottom: 0.3rem;
  font-size: 1.3rem;
  font-weight: bold;

  @include mobile {
    text-align: center;
  }
}

.footer-list {
  text-align: center;
}

.contact-list {
  text-align: left;

  @include mobile {
    text-align: center;
  }
}

.footer-list-el {
  margin-bottom: 5px;
}

.footer-link {
  color: white;
}

.footer-link:hover {
  color: $link;
}

.copyright {
  background-color: $grey-dark;
  padding: 10px;
  font-size: 0.8rem;
}
</style>
