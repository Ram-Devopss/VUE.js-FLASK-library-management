<!-- Navbar.vue -->
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
</template>

<script>
export default {
  name: "MyHeader",
};
</script>

<style scoped>
.navbar-nav .nav-link {
  margin-right: 10px;
}
</style>
