<template>
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
    integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
    crossorigin="anonymous"
  />
  <div class="register-container">
    <h2>Librarian Register</h2>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="username">Enter Username</label>
        <input type="text" id="username" v-model="username" required />
      </div>

      <div class="form-group">
        <label for="email">Enter Email</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="password">Enter Password</label>
        <input type="password" id="password" v-model="password" required />
      </div>

      <button type="submit" class="register-button">Register</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "librarian_register",
  data() {
    return {
      username: "",
      password: "",
      email: "",
    };
  },
  methods: {
    async handleRegister() {
      try {
        const response = await axios.post(
          "http://localhost:5000/Librarian_register",
          {
            username: this.username,
            password: this.password,
            email: this.email,
          }
        );
        this.$router.push("/");
        //Local Storage
        localStorage.setItem(
          "librarian",
          JSON.stringify({ username: this.username })
        );

        // End Local Storage
        alert(response.data.message);
      } catch (error) {
        alert("Registration failed: " + error.response.data.message);
      }
    },
  },
};
</script>

<style scoped>
.register-container {
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
  width: 40%;
  padding: 10px;
  background-color: #308ec4;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-right: 10px;
}

.register-button {
  width: 40%;
  padding: 10px;
  background-color: #ddcc30;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
