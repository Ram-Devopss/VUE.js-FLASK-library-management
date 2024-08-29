<template>
  <nav class="navbar">
    <div class="navbar-heading">Librarian's Dashboard</div>
    <ul class="navbar-list">
      <li><a href="#">Stats</a></li>
      <li><a href="#">LogOut</a></li>
    </ul>
  </nav>
  <div class="search-container">
    <input type="text" class="search-input" placeholder="Search..." />
    <button class="filter-button">Filter</button>
  </div>
  <div class="request">
    <h2 class="request-heading">Request</h2>
    <div class="request-container">
      <div class="info-left">
        <div class="info-item">Book Title</div>
        <div class="info-item">User__0101</div>
      </div>
      <div class="button-container">
        <button class="reject-button">reject</button>
        <button class="grant-button">grant</button>
      </div>
    </div>
    <div class="request-container">
      <div class="info-left">
        <div class="info-item">Book Title</div>
        <div class="info-item">User__0011</div>
      </div>
      <div class="button-container">
        <button class="reject-button">reject</button>
        <button class="grant-button">grant</button>
      </div>
    </div>
  </div>
  <div class="revoke">
    <div class="revoke-container">
      <div class="info-left">
        <div class="info-item">Book Title</div>
        <div class="info-item">User__1001</div>
      </div>
      <button class="revoke-button">revoke</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BookRequests'
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
  content: '';
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

.request-heading {
    margin-top: 70px;
    margin-right: 76%;
}

.request-container {
  display: flex;
  justify-content: space-between; 
  align-items: center;
  text-align: left;
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
  content: '|';
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  color: #645a5a; 
  width: 1.5px;
  height: 25px;
}

.button-container {
  display: flex;
  gap: 10px; 
}

.reject-button {
  padding: 8px 16px;
  border: 2px solid #fa8a5e;
  background-color: #fa8a5e;
  color: rgb(255, 255, 255);
  border-radius: 4px;
  cursor: pointer;
  font-size: 100%;
}

.grant-button {
  padding: 8px 16px;
  border: 2px solid #90ee64;
  background-color: #90ee64;
  color: rgb(255, 255, 255);
  border-radius: 4px;
  cursor: pointer;
  font-size: 100%;
}


.current-heading {
    margin-top: 70px;
    margin-right: 76%;
}

.revoke-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 2px solid #ddd;
  border-radius: 5px;
  padding: 20px;
  margin-top: 20px;
  width: 80%;
  margin-bottom: 20px;
  background-color: #f8f9fa;
  position: fixed;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
}

.revoke-button {
  padding: 8px 16px;
  border: 2px solid #e4e261;
  background-color: #e4e261;
  color: rgb(255, 255, 255);
  border-radius: 4px;
  cursor: pointer;
  font-size: 100%;
}

</style>
