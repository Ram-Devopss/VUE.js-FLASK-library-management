<template>
  <div class="container mt-4">
    <h2 class="text-center mb-4">Statistics Dashboard</h2>
    <div class="row">
      <div class="col-md-6 col-lg-4 mb-4">
        <div class="card shadow-sm">
          <div class="card-body">
            <h5 class="card-title">Total Books</h5>
            <p class="card-text">{{ stats.totalBooks }}</p>
            <button class="btn btn-primary" @click="fetchTotalBooks">
              Refresh
            </button>
          </div>
        </div>
      </div>
      <div class="col-md-6 col-lg-4 mb-4">
        <div class="card shadow-sm">
          <div class="card-body">
            <h5 class="card-title">Books Checked Out</h5>
            <p class="card-text">{{ stats.booksCheckedOut }}</p>
            <button class="btn btn-primary" @click="fetchBooksCheckedOut">
              Refresh
            </button>
          </div>
        </div>
      </div>
      <div class="col-md-6 col-lg-4 mb-4">
        <div class="card shadow-sm">
          <div class="card-body">
            <h5 class="card-title">Pending Requests</h5>
            <p class="card-text">{{ stats.pendingRequests }}</p>
            <button class="btn btn-primary" @click="fetchPendingRequests">
              Refresh
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MyStats",
  data() {
    return {
      stats: {
        totalBooks: 0,
        booksCheckedOut: 0,
        pendingRequests: 0,
      },
    };
  },
  created() {
    this.fetchStats();
  },
  methods: {
    async fetchStats() {
      try {
        // Fetching all statistics from the API
        const [
          totalBooksResponse,
          booksCheckedOutResponse,
          pendingRequestsResponse,
        ] = await Promise.all([
          axios.get("http://localhost:5000/total_books"),
          axios.get("http://localhost:5000/books_checked_out"),
          axios.get("http://localhost:5000/pending_requests"),
        ]);

        this.stats.totalBooks = totalBooksResponse.data.totalBooks;
        this.stats.booksCheckedOut =
          booksCheckedOutResponse.data.booksCheckedOut;
        this.stats.pendingRequests =
          pendingRequestsResponse.data.pendingRequests;
      } catch (error) {
        console.error("Failed to fetch stats:", error);
      }
    },
    async fetchTotalBooks() {
      try {
        const response = await axios.get("http://localhost:5000/total_books");
        this.stats.totalBooks = response.data.totalBooks;
      } catch (error) {
        console.error("Failed to fetch total books:", error);
      }
    },
    async fetchBooksCheckedOut() {
      try {
        const response = await axios.get(
          "http://localhost:5000/books_checked_out"
        );
        this.stats.booksCheckedOut = response.data.booksCheckedOut;
      } catch (error) {
        console.error("Failed to fetch books checked out:", error);
      }
    },
    async fetchPendingRequests() {
      try {
        const response = await axios.get(
          "http://localhost:5000/pending_requests"
        );
        this.stats.pendingRequests = response.data.pendingRequests;
      } catch (error) {
        console.error("Failed to fetch pending requests:", error);
      }
    },
  },
};
</script>

<style scoped>
.card {
  border-radius: 10px;
  overflow: hidden;
}

.card-title {
  font-size: 1.25rem;
  font-weight: bold;
}

.card-text {
  font-size: 1.5rem;
}

.btn-primary {
  background-color: #007bff;
  border: none;
}

.btn-primary:hover {
  background-color: #0056b3;
}
</style>
