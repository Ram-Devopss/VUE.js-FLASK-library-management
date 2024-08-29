<template>
  <nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="#">Library Management</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarColor02"
        aria-controls="navbarColor02"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarColor02">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <router-link class="nav-link active" to="/"
              >Home
              <span class="visually-hidden">(current)</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/librarian_stats"
              >STATS</router-link
            >
          </li>

          <li class="nav-item">
            <router-link class="nav-link" to="/OURBOOKS"
              >OUR BOOKS
            </router-link>
          </li>
        </ul>
      </div>
      <div class="d-flex justify-content-end">
        <button type="button" class="btn btn-outline-danger" @click="LOGOUT">
          Logout
        </button>
      </div>
    </div>
  </nav>
  <div class="container mt-5">
    <h2 class="text-center mb-4">Granted Books List</h2>
    <table class="table table-striped table-bordered">
      <thead class="thead-dark">
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Book No</th>
          <th scope="col">Request Username</th>
          <th scope="col">Time</th>
          <th scope="col">Access</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book.id">
          <td>{{ book.id }}</td>
          <td>{{ book.book_id }}</td>
          <td>{{ book.student_name }}</td>
          <td>{{ book.request_time }}</td>
          <td>
            <button
              type="button"
              v-if="book.access"
              class="btn btn-success"
              disabled
            >
              Granted
            </button>
            <button type="button" v-else class="btn btn-info" disabled>
              Waiting
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "OURBOOKS",
  data() {
    return {
      books: [],
      username: "",
    };
  },
  created() {
    this.fetchBooks();
  },
  methods: {
    LOGOUT() {
      // Clear the "students" data from localStorage or sessionStorage
      localStorage.removeItem("librarian");
      sessionStorage.removeItem("librarian");
      this.$router.push("/");
    },
    async fetchBooks() {
      try {
        // Assuming the username is stored under the key 'students' in localStorage
        const user = localStorage.getItem("students");
        if (!user) {
          alert("Something went wrong: User data not found.");
          return;
        }
        this.username = JSON.parse(user).username;
        const response = await axios.post("http://localhost:5000/OURBOOKS", {
          student_name: this.username, // Pass the correct property name expected by the backend
        });
        this.books = response.data.books;
        console.log(response.data);
      } catch (error) {
        console.error("Error:", error); // Log the error for debugging
        alert(error.response?.data?.message || error.message);
      }
    },
  },
};
</script>

<style scoped>
.table {
  width: 100%;
  margin: auto;
}

.img-thumbnail {
  max-width: 100px;
  max-height: 100px;
  object-fit: cover;
}
</style>
