<template>
  <div>
    <div class="search-container">
      <input type="text" class="search-input" placeholder="Search..." />
      <button class="filter-button">Filter</button>
    </div>
    <div class="current">
      <h2 class="current-heading">Current</h2>
      <div class="current-container">
        <div class="info-left">
          <div class="info-item">Book Title</div>
          <div class="info-item">Author</div>
          <div class="info-item">Section</div>
        </div>
        <button class="return-button">return</button>
      </div>
      <div class="current-container">
        <div class="info-left">
          <div class="info-item">Book Title</div>
          <div class="info-item">Author</div>
          <div class="info-item">Section</div>
        </div>
        <button class="return-button">return</button>
      </div>
    </div>
  </div>
  <div class="completed">
    <h2 class="completed-heading">Completed</h2>
    <div class="completed-container">
      <div class="info-left">
        <div class="info-item">Book Title</div>
        <div class="info-item">Author</div>
        <div class="info-item">Section</div>
      </div>
      <button class="view-button">view</button>
    </div>
    <div class="completed-container">
      <div class="info-left">
        <div class="info-item">Book Title</div>
        <div class="info-item">Author</div>
        <div class="info-item">Section</div>
      </div>
      <button class="view-button">view</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserDashboardMyBooks",
};
</script>

<style scoped>
.search-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  margin-bottom: 20px;
  float: right;
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

.current-heading {
  margin-top: 70px;
  margin-right: 76%;
}

.current-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 2px solid #ddd;
  border-radius: 5px;
  padding: 20px;
  margin-top: 20px;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  background-color: #f8f9fa;
}

.info-left {
  display: flex;
}

.info-item {
  padding: 0 10px;
  position: relative;
}

.info-item:not(:last-child)::after {
  content: "|";
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  color: #645a5a;
  width: 1.5px;
  height: 25px;
}

.return-button {
  padding: 8px 16px;
  border: 2px solid #e4e261;
  background-color: #e4e261;
  color: rgb(255, 255, 255);
  border-radius: 4px;
  cursor: pointer;
  font-size: 100%;
}

.completed {
  margin-top: 40px;
}

.completed-heading {
  margin-top: 70px;
  margin-right: 73%;
}

.completed-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 2px solid #ddd;
  border-radius: 5px;
  padding: 20px;
  margin-top: 20px;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  background-color: #f8f9fa;
}

.view-button {
  padding: 8px 16px;
  border: 2px solid #7fe461;
  background-color: #7fe461;
  color: rgb(255, 255, 255);
  border-radius: 4px;
  cursor: pointer;
  font-size: 100%;
}
</style>
