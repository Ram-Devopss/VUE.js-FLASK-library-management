<template>
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css"
    integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG"
    crossorigin="anonymous"
  />
  <div class="container-fluid">
    <div class="row">
      <!-- Sidebar -->
      <nav id="sidebar" class="col-md-3 col-lg-2 d-md-block bg-light sidebar">
        <div class="position-sticky">
          <h4 class="text-center mt-3">Dashboard</h4>
          <ul class="nav flex-column">
            <li class="nav-item">
              <router-link class="nav-link active" to="/dashboard">
                <i class="bi bi-house-door"></i> Home
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/dashboard/stats">
                <i class="bi bi-bar-chart-line"></i> Stats
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/dashboard/settings">
                <i class="bi bi-gear"></i> Settings
              </router-link>
            </li>
          </ul>
        </div>
      </nav>

      <!-- Main content -->
      <main class="col-md-9 ms-sm-auto col-lg-10 px-4">
        <div
          class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom"
        >
          <h1 class="h2">Dashboard Overview</h1>
          <div class="btn-toolbar mb-2 mb-md-0">
            <div class="btn-group me-2">
              <button type="button" class="btn btn-sm btn-outline-secondary">
                <i class="bi bi-calendar"></i> Calendar
              </button>
            </div>
          </div>
        </div>

        <!-- Cards Section -->
        <div class="row">
          <div class="col-md-4">
            <div class="card mb-4">
              <div class="card-body">
                <h5 class="card-title">Total Users</h5>
                <p class="card-text">1500</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card mb-4">
              <div class="card-body">
                <h5 class="card-title">New Orders</h5>
                <p class="card-text">300</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card mb-4">
              <div class="card-body">
                <h5 class="card-title">Total Revenue</h5>
                <p class="card-text">$12,000</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Chart Section -->
        <div class="row">
          <div class="col-md-12">
            <div class="card mb-4">
              <div class="card-body">
                <h5 class="card-title">Sales Overview</h5>
                <!-- You can use Chart.js or any other chart library here -->
                <canvas id="salesChart" width="400" height="200"></canvas>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import { onMounted } from "vue";

export default {
  name: "Dashboard",
  setup() {
    onMounted(() => {
      // Initialize Chart.js or any other JS libraries here
      const ctx = document.getElementById("salesChart").getContext("2d");
      new Chart(ctx, {
        type: "line",
        data: {
          labels: [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
          ],
          datasets: [
            {
              label: "Sales",
              data: [10, 20, 15, 25, 30, 45, 50],
              borderColor: "rgb(75, 192, 192)",
              backgroundColor: "rgba(75, 192, 192, 0.2)",
            },
          ],
        },
        options: {
          responsive: true,
          scales: {
            x: {
              beginAtZero: true,
            },
            y: {
              beginAtZero: true,
            },
          },
        },
      });
    });
  },
};
</script>

<style scoped>
#sidebar {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
}
.sidebar .nav-link {
  font-size: 1.1rem;
}
.card-title {
  font-size: 1.25rem;
}
.card-text {
  font-size: 1.5rem;
}
</style>
