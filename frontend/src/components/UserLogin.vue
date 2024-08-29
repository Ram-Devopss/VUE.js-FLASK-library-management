<template>
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
    integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
    crossorigin="anonymous"
  />
  <div class="login-container">
    <h2>Student Login</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit" class="login-button">Login</button>
      <router-link class="nav-link" to="Studen_Register"
        >Register As Member</router-link
      >
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "StudentLogin",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post(
          "http://localhost:5000/student_login",
          {
            username: this.username,
            password: this.password,
          }
        );
        alert(response.data.message);

        // Save user data to local storage
        localStorage.setItem(
          "students",
          JSON.stringify({ username: this.username })
        );

        // Navigate to the home page or dashboard
        this.$router.push("/UserDashboard");
      } catch (error) {
        alert("Login failed: " + error.response.data.message);
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  width: 300px;
  margin: 100px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

h2 {
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input {
  width: calc(100% - 10px);
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.login-button {
  width: 100%;
  padding: 10px;
  background-color: #308ec4;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
