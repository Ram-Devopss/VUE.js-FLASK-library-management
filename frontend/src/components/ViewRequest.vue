<template>
  <div class="container mt-5">
    <h2 class="text-center mb-4">Requested List</h2>
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
            <div v-else>
              <button
                type="button"
                class="btn btn-info me-2"
                @click="updateAction"
              >
                Agree
              </button>
              <button
                type="button"
                class="btn btn-danger"
                @click="deleteAction"
              >
                Reject
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ONREQUEST",
  data() {
    return {
      books: [],
    };
  },
  created() {
    this.VIEWREQUEST();
  },
  methods: {
    async ONREQUEST(bookId, username) {
      try {
        // Make the request to update the access status
        const response = await axios.post(
          "http://localhost:5000/UPDATE_ACCESS",
          {
            book_id: bookId,
            student_name: username,
          }
        );

        if (response.data.message === "Access granted") {
          alert("Request granted successfully!");
          // Update the book's access status in the frontend
          const book = this.books.find((b) => b.id === bookId);
          if (book) book.access = true;
        } else {
          alert("Request failed: " + response.data.message);
        }
      } catch (error) {
        console.error("Request Failed:", error);
      }
    },
    async VIEWREQUEST() {
      try {
        const response = await axios.get("http://localhost:5000/VIEWREQUEST");
        this.books = response.data.books;
      } catch (error) {
        console.error("Failed to fetch books:", error);
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
