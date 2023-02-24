import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

require("@/assets/main.scss");

axios.defaults.baseURL = "http://filmarket.makszafa.pl";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

createApp(App).use(store).use(router, axios).mount("#app");
