<template>
  <div class="body">
    <h1 class="title">Moje konto</h1>
    <div class="account-grid">
      <div class="account-section-grid">
        <h1 class="subtitle">Informacje o koncie</h1>
        <h2 class="info-label">E-mail:</h2>
        <h2>{{ this.$store.state.user.email }}</h2>
        <h2 class="info-label">Hasło:</h2>
        <button
          v-if="!isChangePasswordActive"
          class="button is-dark"
          @click="isChangePasswordActive = !isChangePasswordActive"
        >
          Zmień hasło
        </button>
        <i
          v-if="isChangePasswordActive"
          style="font-size: 2.5rem; cursor: pointer; text-align: end"
          class="fas fa-times"
          @click="cancelNewPassword"
        ></i>
        <form
          v-if="isChangePasswordActive"
          class="password-change-form"
          @submit.prevent="changePassword"
        >
          <div class="field">
            <label class="label">Nowe hasło</label>
            <div class="control has-icons-left has-icons-right">
              <span class="icon is-left">
                <i class="fas fa-lock"></i>
              </span>
              <input
                class="input"
                :class="{
                  'is-success': passwordAccepted,
                  'is-danger': passwordInvalid,
                }"
                type="password"
                v-model="newPassword"
              />
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
              <input
                class="input"
                :class="{
                  'is-success': password2Accepted,
                  'is-danger': password2Invalid,
                }"
                type="password"
                v-model="newPassword2"
              />
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
              <button
                class="button is-dark"
                :class="{ 'is-loading': isLoading }"
              >
                Zmień hasło
              </button>
            </div>
          </div>
        </form>
      </div>
      <div class="account-section-grid">
        <h1 class="subtitle">Ulubione</h1>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "AccountPage",
  data() {
    return {
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
    // TODO: co mozna robic na stronie uzytkownika - zmiana hasla / pokazuje info o uzytkowniku / manipulacja sekcja ulubionych
    axios
      .get("/api/v1/user-data/")
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error);
      });
  },
  watch: {
    newPassword: function () {
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
    },
    newPassword2: function () {
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
    },
  },
  methods: {
    changePassword() {
      if (this.passwordAccepted && this.password2Accepted) {
        this.isLoading = true;

        axios
          .patch("/api/v1/users/", this.newPassword)
          .then((response) => {
            toast({
              message: "Hasło zostało poprawnie zmienione",
              type: "is-success",
              duration: 2000,
              position: "center",
              dismissible: true,
              pauseOnHover: true,
            });

            this.isLoading = false;
          })
          .catch((error) => {
            if (error.response) {
              // Request made and server responded
              console.log(error.response.data);
              console.log(error.response.status);
              console.log(error.response.headers);
            } else if (error.request) {
              // The request was made but no response was received
              console.log(error.request);
            } else {
              // Something happened in setting up the request that triggered an Error
              console.log("Error", error.message);
            }
          });
      }
    },
    cancelNewPassword() {
      (this.isChangePasswordActive = false), (this.newPassword = "");
      this.newPassword2 = "";
      this.passwordAccepted = false;
      this.passwordInvalid = false;
      this.password2Accepted = false;
      this.password2Invalid = false;
    },
  },
};
</script>

<style scoped lang="scss">
@import "@/assets/main.scss";

.account-grid {
  display: grid;
  grid-template-columns: 1fr 2fr;
  width: 80vw;
  @include touch {
    grid-template-columns: 1fr;
  }
}

.account-section-grid {
  display: grid;
  grid-template-columns: 1fr 3fr;
  row-gap: 1rem;
  align-items: center;
  @include until-widescreen {
    grid-template-columns: 1fr 2fr;
  }
  @include mobile {
    margin-bottom: 2rem;
  }
}

.subtitle {
  justify-self: center;
  grid-column: 1 / 3;
}

.info-label {
  margin-left: 1rem;
  font-weight: bold;
}

.button {
  max-width: 10rem;
}

.password-change-form {
  grid-column-start: 2;
}

.submit-button {
  text-align: center;
}
</style>
