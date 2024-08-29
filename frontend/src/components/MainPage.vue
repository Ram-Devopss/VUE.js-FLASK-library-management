<template>
  <div class="search-container">
    <input type="text" class="search-input" placeholder="Search..." />
    <button class="filter-button">Filter</button>
  </div>
  <div class="card-container">
    <div class="card">
      <h3>Section_History</h3>
      <p>Date</p>
      <p>Description</p>
      <button class="add-book">Add Book</button>
    </div>
    <div class="card">
      <h3>Section_02</h3>
      <p>Date</p>
      <p>Description</p>
      <button class="add-book">Add Book</button>
    </div>
    <div class="card">
      <h3>Section_03</h3>
      <p>Date</p>
      <p>Description</p>
      <button class="add-book">Add Book</button>
    </div>
  </div>
  <div class="circular-button-container">
    <button class="circular-button">+</button>
  </div>
</template>

<script>
export default {
  name: "MainPage",
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
