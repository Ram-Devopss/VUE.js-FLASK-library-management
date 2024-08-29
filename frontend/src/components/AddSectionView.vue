<template>
    <div>
    <nav class="navbar">
    <div class="navbar-heading">Librarian's Dashboard</div>
    <ul class="navbar-list">
      <li><a href="#">Stats</a></li>
      <li><a href="#">LogOut</a></li>
    </ul>
    </nav>
    </div>
    <h2>Add Section to View</h2>
    <div class="circular-button-container">
    <button class="circular-button">+</button>
    </div>
</template>
  
  <script>
  export default {
    
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

.h2 {
    float:left;
}

.circular-button-container {
  bottom: 20px;
  right: 20px;
  z-index: 1000; 
  align-items: center;
  margin-top: 400px;
}

.circular-button {
  width: 50px;
  height: 50px;
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