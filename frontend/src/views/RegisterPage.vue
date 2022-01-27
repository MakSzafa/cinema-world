<template>
  <div class="body">
    <h1 class="title">Zarejestruj się</h1>
    <form @submit.prevent="submitForm">
      <div class="field">
        <label class="label">E-mail</label>
        <div class="control has-icons-left has-icons-right">
          <span class="icon is-left">
            <i class="fas fa-envelope"></i>
          </span>
          <input
            class="input"
            :class="{
              'is-success': emailAccepted,
              'is-danger': emailInvalid,
            }"
            type="email"
            pattern="/^[a-zA-Z0-9.!#$%'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]{2,}$/"
            v-model="email"
          />
          <span v-if="emailAccepted" class="icon is-right">
            <i class="fas fa-check"></i>
          </span>
          <span v-if="emailInvalid" class="icon is-right">
            <i class="fas fa-exclamation-triangle"></i>
          </span>
          <p v-if="emailAccepted" class="help is-success">E-mail poprawny</p>
          <p v-if="emailInvalid" class="help is-danger">
            Podaj poprawny adres e-mail
          </p>
          <!-- <p v-if="emailUsed" class="help is-danger">
            Podany adres e-mail jest już używany
          </p> -->
        </div>
      </div>
      <div class="field">
        <label class="label">Hasło</label>
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
            v-model="password"
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
            v-model="password2"
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
      <div class="field">
        <div class="control">
          <label class="checkbox">
            <input type="checkbox" v-model="regulations" />
            Akceptuję <a href="/regulations" target="_blank">Regulamin</a>
          </label>
        </div>
      </div>
      <div class="field submit-button">
        <div class="control">
          <button
            class="button is-dark"
            :class="{ 'is-loading': isLoading }"
            :disabled="isButtonDisabled"
          >
            Zarejestruj się
          </button>
        </div>
      </div>
      <hr />
      Masz już konto? <router-link to="/login">Zaloguj się</router-link>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from 'bulma-toast'

export default {
  name: "RegisterPage",
  data() {
    return {
      email: "",
      password: "",
      password2: "",
      regulations: false,
      emailAccepted: false,
      emailInvalid: false,
      // emailUsed: false, TODO: sprawdzanie czy mail uzyty
      passwordAccepted: false,
      passwordInvalid: false,
      password2Accepted: false,
      password2Invalid: false,
      isLoading: false,
    };
  },
  mounted() {
    document.title = "Filmarket | Zarejestruj się";
  },
  computed: {
    isButtonDisabled() {
      if (this.emailAccepted && this.passwordAccepted && this.password2Accepted && this.regulations) {
        return false;
      } else {
        return true;
      }
    },
  },
  watch: {
    email: function () {
      if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]{2,}$/.test(this.email)) {
        setTimeout(() => {
          this.emailAccepted = true;
          this.emailInvalid = false;
        }, 500);
      } else {
        setTimeout(() => {
          this.emailAccepted = false;
          this.emailInvalid = true;
        }, 500);
      }
    },
    password: function () {
      if (this.password.length >= 8) {
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
    password2: function () {
      if (this.password === this.password2) {
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
    submitForm() {
      if (this.emailAccepted && this.passwordAccepted && this.password2Accepted && this.regulations) {
        this.isLoading = true

        const newUser = {
          email: this.email,
          password: this.password
        }

        axios
          .post("/api/v1/users/", newUser)
          .then(response => {
            toast({
              message: 'Konto zostało utworzone, zaloguj się',
              type: 'is-success',
              duration: 2000,
              position: 'center',
              dismissible: true,
              pauseOnHover: true,
            })

            this.isLoading = false
            this.$router.push('/login')
          })
          .catch(error => {
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
              console.log('Error', error.message);
            }
          })
      }
    },
  },
};
</script>

<style scoped lang="scss">
.submit-button {
  text-align: center;
}
</style>