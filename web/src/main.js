import { createApp } from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
import { createRouter, createWebHistory } from "vue-router";
import Home from "./components/Home.vue";
import About from "./components/About.vue";
import HelloWorld from "./components/HelloWorld.vue";

loadFonts();

const routes = [
  { path: "/", component: Home, name: "home" },
  { path: "/about", component: About, name: "about" },
  { path: "/helloworld", component: HelloWorld, name: "helloworld" },
];

const router = createRouter({
  history: createWebHistory(),
  routes, // short for `routes: routes`
});

createApp(App).use(router).use(vuetify).mount("#app");
