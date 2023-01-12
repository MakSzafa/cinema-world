import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/search/:query?",
    name: "search",
    component: () => import("../views/SearchPage.vue"),
  },
  {
    path: "/:movie/:id",
    name: "product",
    component: () => import("../views/ProductPage.vue"),
  },
  {
    path: "/about",
    name: "about",
    component: () => import("../views/AboutPage.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../views/RegisterPage.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/LoginPage.vue"),
  },
  {
    path: "/my-account",
    name: "account",
    component: () => import("../views/AccountPage.vue"),
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/help",
    name: "help",
    component: () => import("../views/HelpPage.vue"),
  },
  {
    path: "/regulations",
    name: "regulations",
    component: () => import("../views/RegulationsPage.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return { left: 0, top: 0 };
  },
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !localStorage.getItem("id")
  ) {
    next({ name: "login", query: { to: to.path } });
  } else {
    next();
  }
});

export default router;
