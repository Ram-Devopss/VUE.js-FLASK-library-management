import { createApp } from "vue";
import App from "./App.vue";
import "bootstrap/dist/css/bootstrap.css"; // Import Bootstrap CSS
import router from "./router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

createApp(App).use(router).mount("#app");
