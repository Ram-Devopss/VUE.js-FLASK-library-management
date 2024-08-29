<template>
  <div>
    <nav class="navbar">
      <div class="navbar-heading">Librarian's Dashboard</div>
      <ul class="navbar-list">
        <li><a href="#">Stats</a></li>
        <li><a href="#">Books</a></li>
        <li><a href="#">LogOut</a></li>
      </ul>
    </nav>
  </div>
  <h2>Add New Section</h2>
  <div class="section-form">
    <form @submit.prevent="addSection">
      <div class="form-group">
        <label>Title:</label>
        <input v-model="title" placeholder="Section_History" />
      </div>
      <div class="form-group">
        <label>Date created:</label>
        <input v-model="date" placeholder="DD/MM/YYYY" />
      </div>
      <div class="form-group">
        <label>Image:</label>
        <input v-model="image" placeholder="Optional" />
      </div>
      <div class="form-group">
        <label>Description:</label>
        <textarea v-model="description" placeholder="Description"></textarea>
      </div>
      <div class="form-buttons">
        <button type="button" @click="cancel" class="cancel-button">Cancel</button>
        <button type="submit" class="add-button">Add</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      date: '',
      image: '',
      description: ''
    };
  },
  methods: {
    addSection() {
    },
    cancel() {
    }
  }
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

.section-form {
  width: 400px;
  margin: 0 auto;
  border: 1px solid #ccc;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

.h2 {
  float: left;
}

.form-group {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.form-group label {
  flex: 1;
  margin-right: 10px;
  font-weight: bold;
}

.form-group input,
.form-group textarea {
  flex: 2;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

textarea {
  resize: vertical;
}

.form-buttons {
  display: flex;
  justify-content: space-between;
}

.cancel-button,
.add-button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.cancel-button {
  background-color: #f44336;
  color: #fff;
}

.add-button {
  background-color: #4caf50;
  color: #fff;
}
</style>
