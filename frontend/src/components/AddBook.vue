<template>
  <div>
    <h3 style="text-align: center">Add books to view</h3>
    <br />
    <br />

    <div class="book-form">
      <form @submit.prevent="addBook">
        <div class="form-group">
          <label for="title">Title:</label>
          <input type="text" id="title" v-model="title" required />
        </div>
        <div class="form-group">
          <label for="author">Author:</label>
          <input type="text" id="author" v-model="author" />
        </div>
        <div class="form-group">
          <label for="genre">Section:</label>
          <select id="genre" v-model="genre" required class="form-control">
            <option disabled value="">Add Section</option>
            <option
              v-for="genreOption in genres"
              :key="genreOption.id"
              :value="genreOption.name"
            >
              {{ genreOption.name }}
            </option>
          </select>
        </div>

        <div class="form-group">
          <label for="image">Image URL :</label>
          <input type="text" id="image" v-model="image" />
        </div>

        <div class="form-actions">
          <button type="button" @click="cancel" class="btn cancel">
            Cancel
          </button>
          <button type="submit" class="btn add">Add</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "AddBook",
  data() {
    return {
      genres: [
        { id: 1, name: "Adventure", count: 60 },
        { id: 2, name: "Biography", count: 45 },
        { id: 3, name: "Classics", count: 90 },
        { id: 4, name: "Crime", count: 50 },
        { id: 5, name: "Fantasy", count: 70 },
        { id: 6, name: "Historical Fiction", count: 55 },
        { id: 7, name: "Horror", count: 30 },
        { id: 8, name: "Literary Fiction", count: 40 },
        { id: 9, name: "Mathematics", count: 40 },
        { id: 10, name: "Memoir", count: 35 },
        { id: 11, name: "Mystery", count: 90 },
        { id: 12, name: "Non-fiction", count: 80 },
        { id: 13, name: "Philosophy", count: 25 },
        { id: 14, name: "Physics", count: 35 },
        { id: 15, name: "Politics", count: 50 },
        { id: 16, name: "Romance", count: 100 },
        { id: 17, name: "Science", count: 60 },
        { id: 18, name: "Science Fiction", count: 50 },
        { id: 19, name: "Self-Help", count: 70 },
        { id: 20, name: "Social Sciences", count: 45 },
        { id: 21, name: "Thriller", count: 60 },
        { id: 22, name: "Travel", count: 30 },
        { id: 23, name: "Young Adult", count: 75 },
      ].sort((a, b) => a.name.localeCompare(b.name)),

      // Add more genres as needed

      title: "",
      author: "",
      genre: "",
      image: "",
    };
  },
  methods: {
    async addBook() {
      try {
        const response = await axios.post("http://localhost:5000//ADDBOOKS", {
          title: this.title,
          author: this.author,
          genre: this.genre,
          image: this.image,
        });
        alert(response.data.message || "Book added successfully!");
        this.cancel();
      } catch (error) {
        alert(
          "Failed to add book: " +
            (error.response.data.message || error.message)
        );
        this.cancel();
      }
    },
    cancel() {
      (this.title = ""),
        (this.author = ""),
        (this.genre = ""),
        (this.image = "");
    },
  },
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

.book-form {
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 10px;
  width: 300px;
  margin: auto;
}

.book-form h3 {
  text-align: center;
}

.form-group {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.form-group label {
  flex: 0 0 30%;
  margin-right: 10px;
  text-align: left;
}

.form-group input {
  flex: 1;
  padding: 8px;
  box-sizing: border-box;
}

.form-actions {
  display: flex;
  justify-content: space-between;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn.cancel {
  background-color: #f8d7da;
  color: #721c24;
}

.btn.add {
  background-color: #d4edda;
  color: #155724;
}
</style>
