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
            <router-link class="nav-link" to="/VIEWBOOKS">BOOKS </router-link>
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

  <div class="search-filter"></div>
  <div class="card-container">
    <div class="card">
      <p>Total No Of Books</p>
      <h3 style="text-align: center">{{ book }}</h3>
      <button type="button" class="btn btn-info" @click="ADDBOOKS">
        Add Book
      </button>
    </div>
    <div class="card">
      <p>Total No Of Students</p>
      <h3 style="text-align: center">{{ students }}</h3>
      <button type="button" class="btn btn-warning" @click="VIEWBOOKS">
        View Books
      </button>
    </div>
    <div class="card">
      <p>No Of Requests</p>
      <h3 style="text-align: center">{{ requests }}</h3>
      <button type="button" class="btn btn-danger" @click="ONREQUEST">
        Requests
      </button>
    </div>
  </div>

  <div class="container mt-5">
    <h2 class="text-center mb-4">Book List</h2>
    <table class="table table-striped table-bordered">
      <thead class="thead-dark">
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Title</th>
          <th scope="col">Author</th>
          <th scope="col">Genre</th>
          <th scope="col">Image</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book.id">
          <td>{{ book.id }}</td>
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
          <td>{{ book.genre }}</td>
          <td>
            <img
              :src="book.image"
              alt="Book Image"
              class="img-thumbnail"
              width="100"
            />
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="container mt-5">
    <h2 class="text-center mb-4">Requested List</h2>
    <table class="table table-striped table-bordered">
      <thead class="thead-dark">
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Book No</th>
          <th scope="col">Request Username</th>
          <th scope="col">Time</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in rbooks" :key="book.id">
          <td>{{ book.id }}</td>
          <td>{{ book.book_id }}</td>
          <td>{{ book.student_name }}</td>
          <td>{{ book.request_time }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LibrarianDashboardSection",
  data() {
    return {
      book: 0,
      students: 0,
      requests: 0,
      books: [],
      rbooks: [],
    };
  },
  created() {
    this.fetchBooks();
    this.totalstudents();
    this.totalrequest();
    this.displaybooks();
    this.VIEWREQUEST();
  },

  methods: {
    LOGOUT() {
      // Clear the "students" data from localStorage or sessionStorage
      localStorage.removeItem("librarian");
      sessionStorage.removeItem("librarian");
      this.$router.push("/");
    },
    async VIEWREQUEST() {
      try {
        const response = await axios.get("http://localhost:5000/VIEWREQUEST");
        this.rbooks = response.data.books;
      } catch (error) {
        console.error("Failed to fetch books:", error);
      }
    },
    async displaybooks() {
      try {
        const response = await axios.get("http://localhost:5000/VIEWBOOKS");
        this.books = response.data.books;
      } catch (error) {
        console.error("Failed to fetch books:", error);
      }
    },
    ONREQUEST() {
      this.$router.push("/ONREQUEST");
    },

    VIEWBOOKS() {
      this.$router.push("/VIEWBOOKS");
    },
    ADDBOOKS() {
      this.$router.push("/ADDBOOKS");
    },

    async totalstudents() {
      try {
        const response = await axios.get("http://localhost:5000/TOTALSTUDENTS");
        this.students = response.data.final_id;
      } catch (error) {
        console.error("Failed to fetch books:", error);
      }
    },
    async fetchBooks() {
      try {
        const response = await axios.get("http://localhost:5000/TOTALBOOKS");
        this.book = response.data.final_id;
      } catch (error) {
        console.error("Failed to fetch books:", error);
      }
    },

    async totalrequest() {
      try {
        const response = await axios.get("http://localhost:5000/TOTALREQUEST");
        this.requests = response.data.final_id;
      } catch (error) {
        console.error("Failed to fetch books:", error);
      }
    },
  },
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #f8f9fa;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  border-radius: 5px;
}

.navbar-heading {
  font-size: 1.5rem;
  font-weight: bold;
  color: #007bff;
}

.navbar-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}

.navbar-list li {
  margin: 0;
  padding: 0;
  position: relative;
}

.navbar-list li:not(:last-child)::after {
  content: "";
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 1.5px;
  height: 25px;
  background-color: #ddd;
}

.navbar-list li a {
  text-decoration: none;
  color: #007bff;
  padding: 0 10px;
}

.navbar-list li a:hover {
  text-decoration: underline;
}

.search-container {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
  margin-bottom: 20px;
}

.search-input {
  padding: 8px;
  border: 2px solid #ddd;
  border-radius: 5px;
  outline: none;
  margin-right: 10px;
}

.filter-button {
  padding: 8px 16px;
  border: 1px solid #007bff;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  font-size: 100%;
}

.filter-button:hover {
  background-color: #0056b3;
}

.card-container {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.card {
  border: 1px solid #000;
  border-radius: 10px;
  padding: 20px;
  width: 200px;
  text-align: left;
  font-family: "Arial", sans-serif;
}

.add-book {
  margin-top: 20px;
  padding: 10px 20px;
  border: 1px solid #000;
  border-radius: 5px;
  background-color: #fff;
  cursor: pointer;
  font-family: "Arial", sans-serif;
}

.circular-button-container {
  bottom: 20px;
  right: 20px;
  z-index: 1000;
  align-items: center;
  margin-top: 150px;
}

.circular-button {
  width: 75px;
  height: 75px;
  line-height: 50px;
  border-radius: 50%;
  border: 2px solid #007bff;
  background-color: #007bff;
  color: white;
  font-size: 24px;
  font-weight: bold;
  cursor: pointer;
  outline: none;
  transition: background-color 0.3s;
}
</style>
