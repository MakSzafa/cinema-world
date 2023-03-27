<template>
  <div class="body">
    <h1 class="title">Moje konto</h1>
    <div class="account-grid">
      <div class="account-section-grid-1">
        <h1 class="subtitle">Informacje o koncie</h1>
        <h2 class="info-label">E-mail:</h2>
        <h2>{{ this.$store.state.users.user.email }}</h2>
        <h2 class="info-label">Hasło:</h2>
        <button v-if="!isChangePasswordActive" class="button is-dark"
          @click="isChangePasswordActive = !isChangePasswordActive">
          Zmień hasło
        </button>
        <span v-if="isChangePasswordActive" class="close">
          <i class="fas fa-times" style="font-size: 2.5rem; cursor: pointer; color: rgb(40, 42, 42)"
            @click="cancelNewPassword"></i>
        </span>
        <form v-if="isChangePasswordActive" class="password-change-form" @submit.prevent="changePassword">
          <div class="field">
            <label class="label">Nowe hasło</label>
            <div class="control has-icons-left has-icons-right">
              <span class="icon is-left">
                <i class="fas fa-lock"></i>
              </span>
              <input class="input" :class="{
                'is-success': passwordAccepted,
                'is-danger': passwordInvalid,
              }" type="password" v-model="newPassword" />
              <span v-if="passwordAccepted" class="icon is-right">
                <i class="fas fa-check"></i>
              </span>
              <span v-if="passwordInvalid" class="icon is-right">
                <i class="fas fa-exclamation-triangle"></i>
              </span>
              <p v-if="passwordAccepted" class="help is-success">
                Hasło spełnia wymagania
              </p>
              <p v-if="passwordInvalid" class="help is-danger">
                Podane hasło jest za krótkie
              </p>
            </div>
          </div>
          <div class="field">
            <label class="label">Powtórz hasło</label>
            <div class="control has-icons-left has-icons-right">
              <span class="icon is-left">
                <i class="fas fa-lock"></i>
              </span>
              <input class="input" :class="{
                'is-success': password2Accepted,
                'is-danger': password2Invalid,
              }" type="password" v-model="newPassword2" />
              <span v-if="password2Accepted" class="icon is-right">
                <i class="fas fa-check"></i>
              </span>
              <span v-if="password2Invalid" class="icon is-right">
                <i class="fas fa-exclamation-triangle"></i>
              </span>
              <p v-if="password2Accepted" class="help is-success">
                Hasła są identyczne
              </p>
              <p v-if="password2Invalid" class="help is-danger">
                Podane hasła róznią się
              </p>
            </div>
          </div>
          <div class="field submit-button">
            <div class="control">
              <button class="button is-dark" :class="{ 'is-loading': isLoading }">
                Zmień hasło
              </button>
            </div>
          </div>
        </form>
      </div>
      <div class="account-section-grid-2">
        <h1 class="subtitle">Ulubione</h1>
        <div class="account-subsection-grid">
          <h2 class="info-label">Ulubione kina:</h2>
          <button v-if="!isEditCinemasActive" class="button is-dark fav-btn"
            @click="isEditCinemasActive = !isEditCinemasActive">
            Edytuj
          </button>
          <span v-if="isEditCinemasActive" style="text-align: end">
            <i class="fas fa-times" style="font-size: 1.4rem; cursor: pointer; color: rgb(40, 42, 42)"
              @click="cancelEditCinemas"></i>
          </span>
          <div class="select is-primary add-fav is-small" v-if="isEditCinemasActive">
            <select name="cinemas" id="cinemas">
              <option value="">---Dodaj kino---</option>
              <option v-for="cinema in cinemas" :value="cinema" :key="cinema">
                {{ cinema }}
              </option>
            </select>
          </div>
          <button v-if="isEditCinemasActive" class="button is-dark fav-btn" @click="addFavCinema">
            Dodaj
          </button>
          <div class="favourites">
            <div class="fav-item" v-for="cinema in this.$store.state.users.user.favourite_cinemas" :key="cinema">
              <h3>
                {{ cinema }}
              </h3>
              <i v-if="isEditCinemasActive" class="fas fa-trash-alt del-fav" @click="deleteFavCinema(cinema)"></i>
            </div>
          </div>
        </div>
        <div class="account-subsection-grid">
          <h2 class="info-label">Ulubione gatunki:</h2>
          <button v-if="!isEditGenresActive" class="button is-dark fav-btn"
            @click="isEditGenresActive = !isEditGenresActive">
            Edytuj
          </button>
          <span v-if="isEditGenresActive" style="text-align: end">
            <i class="fas fa-times" style="font-size: 1.4rem; cursor: pointer; color: rgb(40, 42, 42)"
              @click="cancelEditGenres"></i>
          </span>
          <div class="select is-primary add-fav is-small" v-if="isEditGenresActive">
            <select name="genres" id="genres">
              <option value="">---Dodaj gatunek---</option>
              <option v-for="genre in genres" :value="genre" :key="genre">
                {{ genre }}
              </option>
            </select>
          </div>
          <button v-if="isEditGenresActive" class="button is-dark fav-btn" @click="addFavGenre">
            Dodaj
          </button>
          <div class="favourites">
            <div class="fav-item" v-for="genre in this.$store.state.users.user.favourite_genres" :key="genre">
              <h3>
                {{ genre }}
              </h3>
              <i v-if="isEditGenresActive" class="fas fa-trash-alt del-fav" @click="deleteFavGenre(genre)"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { toast } from "bulma-toast";

export default {
  name: "AccountPage",
  data() {
    return {
      isEditCinemasActive: false,
      cinemas: [],
      isEditGenresActive: false,
      genres: [],
      isChangePasswordActive: false,
      newPassword: "",
      newPassword2: "",
      passwordAccepted: false,
      passwordInvalid: false,
      password2Accepted: false,
      password2Invalid: false,
      isLoading: false,
    };
  },
  mounted() {
    document.title = "Filmarket | Moje konto";
  },
  updated() {
    if (
      this.cinemas.length === 0 &&
      this.$store.state.buildings.length !==
      this.$store.state.users.user.favourite_cinemas.length
    ) {
      this.$store.state.buildings.forEach((element) => {
        if (!this.$store.state.users.user.favourite_cinemas.includes(element)) {
          this.cinemas.push(element);
        }
      });
    }
    if (
      this.genres.length === 0 &&
      this.$store.state.genres.length !==
      this.$store.state.users.user.favourite_genres.length
    ) {
      this.$store.state.genres.forEach((element) => {
        if (!this.$store.state.users.user.favourite_genres.includes(element)) {
          this.genres.push(element);
        }
      });
    }
  },
  watch: {
    newPassword: function () {
      if (this.isChangePasswordActive) {
        if (this.newPassword.length >= 8) {
          setTimeout(() => {
            this.passwordAccepted = true;
            this.passwordInvalid = false;
          }, 500);
        } else {
          setTimeout(() => {
            this.passwordAccepted = false;
            this.passwordInvalid = true;
          }, 500);
        }
        if (this.newPassword === this.newPassword2) {
          setTimeout(() => {
            this.password2Accepted = true;
            this.password2Invalid = false;
          }, 500);
        } else {
          setTimeout(() => {
            this.password2Accepted = false;
            this.password2Invalid = true;
          }, 500);
        }
      }
    },
    newPassword2: function () {
      if (this.isChangePasswordActive) {
        if (this.newPassword === this.newPassword2) {
          setTimeout(() => {
            this.password2Accepted = true;
            this.password2Invalid = false;
          }, 500);
        } else {
          setTimeout(() => {
            this.password2Accepted = false;
            this.password2Invalid = true;
          }, 500);
        }
      }
    },
  },
  methods: {
    async changePassword() {
      if (
        this.passwordAccepted &&
        this.password2Accepted &&
        localStorage.getItem("id")
      ) {
        this.isLoading = true;

        const User = {
          id: localStorage.getItem("id"),
          password: this.newPassword,
        };

        try {
          await this.$store.dispatch("editUser", User);

          toast({
            message: "Hasło zostało poprawnie zmienione.",
            type: "is-success",
            duration: 2000,
            position: "center",
            dismissible: true,
            pauseOnHover: true,
          });

          this.newPassword = '';
          this.newPassword2 = '';
          this.passwordAccepted = false;
          this.passwordInvalid = false;
          this.password2Accepted = false;
          this.password2Invalid = false;
          this.isChangePasswordActive = false;
          this.isLoading = false;
        } catch (e) {
          console.log(e);

          toast({
            message: "Wystąpił błąd, spróbuj ponownie.",
            type: "is-danger",
            duration: 2000,
            position: "center",
            dismissible: true,
            pauseOnHover: true,
          });

          this.newPassword = '';
          this.newPassword2 = '';
          this.passwordAccepted = false;
          this.passwordInvalid = false;
          this.password2Accepted = false;
          this.password2Invalid = false;
          this.isChangePasswordActive = false;
          this.isLoading = false;
        }
      }
    },
    cancelNewPassword() {
      this.isChangePasswordActive = false;
      this.newPassword = "";
      this.newPassword2 = "";
      this.passwordAccepted = false;
      this.passwordInvalid = false;
      this.password2Accepted = false;
      this.password2Invalid = false;
    },
    async addFavCinema() {
      if (
        document.getElementById("cinemas").value !== "" &&
        localStorage.getItem("id")
      ) {
        let user = this.$store.state.users.user;
        user.favourite_cinemas.push(document.getElementById("cinemas").value);
        this.$store.commit("setUser", user);

        this.cinemas = this.cinemas.filter(
          (element) => element !== document.getElementById("cinemas").value
        );

        const User = {
          id: localStorage.getItem("id"),
          favourite_cinemas: user.favourite_cinemas,
        };

        await this.$store.dispatch("editUser", User);
      }
    },
    async deleteFavCinema(cinema) {
      let user = this.$store.state.users.user;
      user.favourite_cinemas = user.favourite_cinemas.filter(
        (element) => element !== cinema
      );
      this.$store.commit("setUser", user);

      this.cinemas.push(cinema);

      const User = {
        id: localStorage.getItem("id"),
        favourite_cinemas: user.favourite_cinemas,
      };

      await this.$store.dispatch("editUser", User);
    },
    cancelEditCinemas() {
      this.isEditCinemasActive = false;
    },
    async addFavGenre() {
      if (
        document.getElementById("genres").value !== "" &&
        localStorage.getItem("id")
      ) {
        let user = this.$store.state.users.user;
        user.favourite_genres.push(document.getElementById("genres").value);
        this.$store.commit("setUser", user);

        this.genres = this.genres.filter(
          (element) => element !== document.getElementById("genres").value
        );
        const User = {
          id: localStorage.getItem("id"),
          favourite_genres: user.favourite_genres,
        };

        await this.$store.dispatch("editUser", User);
      }
    },
    async deleteFavGenre(genre) {
      let user = this.$store.state.users.user;
      user.favourite_genres = user.favourite_genres.filter(
        (element) => element !== genre
      );
      this.$store.commit("setUser", user);

      this.genres.push(genre);

      const User = {
        id: localStorage.getItem("id"),
        favourite_genres: user.favourite_genres,
      };

      await this.$store.dispatch("editUser", User);
    },
    cancelEditGenres() {
      this.isEditGenresActive = false;
    },
  },
};
</script>

<style scoped lang="scss">
@import "@/assets/main.scss";

.account-grid {
  display: grid;
  grid-template-columns: 1fr 2fr;
  column-gap: 10rem;
  width: 90vw;

  @include until-widescreen {
    column-gap: 6rem;
  }

  @include touch {
    grid-template-columns: 1fr;
  }
}

.account-section-grid-1 {
  display: grid;
  grid-template-columns: 25% 75%;
  grid-template-rows: 50px 50px 50px;
  align-items: start;
  row-gap: 1rem;

  button {
    width: 120px;
    height: 35px;
  }

  .close {
    text-align: end;
  }

  @include until-widescreen {
    grid-template-columns: 30% 70%;
  }

  @include touch {
    margin-bottom: 2rem;

    .close {
      text-align: start;
      margin-left: 270px;
    }
  }

  @media screen and (max-width: 500px) {
    .close {
      text-align: end;
      margin-left: 0;
    }
  }
}

.account-section-grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 50px 1fr;
  align-items: start;
  row-gap: 1rem;
  column-gap: 5rem;

  @include mobile {
    margin-bottom: 2rem;
    grid-template-columns: 1fr;

    .subtitle {
      grid-column: 1;
    }
  }

  .account-subsection-grid {
    display: grid;
    grid-template-columns: 1fr auto;

    .fav-btn {
      width: 70px;
      height: 25px;
      font-size: 0.8rem;
      place-self: center;
    }

    .add-fav {
      justify-self: center;
    }

    .favourites {
      grid-column: 1 / 3;
      margin-top: 0.7rem;

      .fav-item {
        display: grid;
        grid-template-columns: 1fr 20px;

        h3:before {
          content: "•";
          color: $text;
          display: inline-block;
          margin: 3px 5px;
        }

        .del-fav {
          place-self: center;
          cursor: pointer;
        }
      }
    }
  }
}

.subtitle {
  justify-self: center;
  grid-column: 1 / 3;
}

.info-label {
  font-weight: bold;
}

.button {
  max-width: 10rem;
}

.button:focus {
  box-shadow: none !important;
}

.password-change-form {
  grid-column-start: 2;

  @include touch {
    grid-column: 1 / 3;
    grid-column-start: 1;

    .field {
      max-width: 300px;
      margin-left: auto;
      margin-right: auto;
    }
  }
}

.submit-button {
  text-align: center;
}

i:hover {
  color: #222323 !important;
}
</style>
