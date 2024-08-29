// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import Home from "@/components/LibrarianDashboard.vue";
import LibrarianLogin from "@/components/LibrarianLogin.vue";
import StudentRegister from "@/components/UserRegister.vue";
import Studen_Login from "@/components/UserLogin.vue";
import librarian_register from "@/components/LibrarianRegister.vue";
import UserDashboard from "@/components/UserDashboard.vue";
import LibrarianDashboardSection from "@/components/LibrarianDashboardSection.vue";
import AddBook from "@/components/AddBook.vue";
import ONREQUEST from "@/components/ViewRequest.vue";
import VIEWBOOKS from "@/components/ViewBooks.vue";
import librarian_stats from "@/components/LibraryStats.vue";
import OURBOOKS from "@/components/OurBooks.vue";
const routes = [
  { path: "/VIEWBOOKS", name: "VIEWBOOKS", component: VIEWBOOKS },

  {
    path: "/librarian_stats",
    name: "librarian_stats",
    component: librarian_stats,
  },

  { path: "/OURBOOKS", name: "OURBOOKS", component: OURBOOKS },

  { path: "/ONREQUEST", name: "ONREQUEST", component: ONREQUEST },
  {
    path: "/ADDBOOKS",
    name: "AddBook",
    component: AddBook,
  },
  {
    path: "/LibrarianDashboardSection",
    name: "LibrarianDashboardSection",
    component: LibrarianDashboardSection,
  },
  { path: "/", component: Home },
  { path: "/librarian_login", component: LibrarianLogin },
  {
    path: "/UserDashboard",
    name: "UserDashboard",
    component: UserDashboard,
  },
  {
    name: "StudentRegister",
    path: "/Studen_Register",
    component: StudentRegister,
  },
  { path: "/Studen_Login", component: Studen_Login },
  { path: "/librarian_register", component: librarian_register },
  // { path: "/features", component: Features },
  // { path: "/pricing", component: Pricing },
  // { path: "/about", component: About },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
