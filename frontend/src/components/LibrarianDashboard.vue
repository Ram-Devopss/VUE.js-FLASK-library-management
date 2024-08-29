<template>
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css"
    integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG"
    crossorigin="anonymous"
  />
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
            <router-link class="nav-link" to="/librarian_login"
              >Librarian</router-link
            >
          </li>

          <!-- <li class="nav-item">
            <router-link class="nav-link" to="/librarian_register"
              >Management Register</router-link
            >
          </li> -->
          <li class="nav-item">
            <router-link class="nav-link" to="Studen_Login"
              >Student
            </router-link>
          </li>
          <!-- <li class="nav-item">
            <router-link class="nav-link" to="Studen_Register"
              >Student Register</router-link
            >
          </li> -->
        </ul>
      </div>
    </div>
  </nav>
  <div class="main-page">
    <div class="background-image">
      <div class="content">
        <h1 style="color: whitesmoke">Welcome to Library Management</h1>
        <p>Discover amazing features and content here!</p>
        <button @click="handleAction">Get Started</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LibrarianPage",
  methods: {
    handleAction() {
      // Add your action logic here
      alert("Pls Register Or Login As a Student/Librarian");
    },
  },
};
</script>

<style scoped>
.main-page {
  position: relative;
  height: 100vh;
  overflow: hidden;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("https://img.freepik.com/free-vector/public-library-with-many-books-shelves_107791-26807.jpg");
  background-size: cover; /* Cover the entire container */
  background-position: center; /* Center the image */
  background-repeat: no-repeat; /* Prevent image repeat */
  display: flex;
  align-items: center; /* Center content vertically */
  justify-content: center; /* Center content horizontally */
}

.content {
  text-align: center;
  color: white;
  background: rgba(
    0,
    0,
    0,
    0.5
  ); /* Semi-transparent background for better readability */
  padding: 20px;
  border-radius: 8px;
}

h1 {
  font-size: 3rem;
  margin-bottom: 10px;
}

p {
  font-size: 1.2rem;
  margin-bottom: 20px;
}

button {
  padding: 10px 20px;
  font-size: 1rem;
  color: white;
  background-color: #308ec4;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #2078a0;
}

/* Existing styles */
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
  text-align: center;
  font-family: "Arial", sans-serif;
}

.card h3 {
  margin-top: 0;
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
