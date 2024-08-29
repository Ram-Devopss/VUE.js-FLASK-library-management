<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="#"
          >Library Management</router-link
        >
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarColor02"
          aria-controls="navbarColor02"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarColor02">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <router-link class="nav-link active" to="/">
                Home
                <span class="visually-hidden">(current)</span>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/librarian_stats"
                >STATS</router-link
              >
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/VIEWBOOKS">BOOKS</router-link>
            </li>
          </ul>
        </div>
        <div class="d-flex justify-content-end">
          <button type="button" class="btn btn-outline-danger" @click="LOGOUT">
            Logout
          </button>
        </div>
      </div>
    </nav>

    <!-- Book Tabs -->
    <div class="container mt-5">
      <router-link class="navbar-brand float-end" to="/ADDBOOKS">
        <button type="button" class="btn btn-primary">Add Section</button>
      </router-link>
      <small>More Features Coming Soon</small>

      <!-- Tabs for navigation -->
      <ul class="nav nav-tabs mb-4">
        <li class="nav-item" v-for="genre in uniqueGenres" :key="genre">
          <a
            class="nav-link"
            :class="{ active: activeTab === genre }"
            @click="showTab(genre)"
          >
            {{ genre }}
          </a>
        </li>
      </ul>

      <!-- Default Section -->
      <div v-if="!activeTab">
        <h2 class="text-center mb-4">
          Welcome! Please select a Section to see the book list.
        </h2>
      </div>

      <!-- Book Lists -->
      <div v-if="activeTab">
        <h2 class="text-center mb-4">{{ activeTab }} Book List</h2>
        <table class="table table-striped table-bordered">
          <thead class="thead-dark">
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Genre</th>
              <th scope="col">Image</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="book in filteredBooks" :key="book.id">
              <td>{{ book.id }}</td>
              <td>
                <a
                  style="text-decoration: underline"
                  href="#"
                  @click.prevent="showBookDetail(book)"
                >
                  {{ book.title }}
                </a>
              </td>
              <td>{{ book.author }}</td>
              <td>{{ book.genre }}</td>
              <td>
                <img
                  :src="book.image"
                  alt="Book Image"
                  class="img-thumbnail"
                  width="100"
                />
              </td>
              <td>
                <div class="btn-group" role="group" aria-label="Basic example">
                  <button
                    type="button"
                    class="btn btn-info me-2"
                    @click="updateAction(book.id)"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger"
                    @click="deleteAction(book.id)"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Book Detail Modal -->
    <div
      v-if="selectedBook"
      class="book-detail-modal"
      @click.self="closeDetail"
    >
      <div class="book-detail-content">
        <h2>{{ selectedBook.title }}</h2>
        <p><strong>Author:</strong> {{ selectedBook.author }}</p>
        <p><strong>Genre:</strong> {{ selectedBook.genre }}</p>
        <p><strong>Description:</strong> {{ selectedBook.description }}</p>
        <button class="btn btn-secondary" @click="closeDetail">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTab: "Fiction", // Default to no tab selected
      selectedBook: null, // Book detail for modal
      books: [
        // Fiction Books
        {
          id: 1,
          title: "The Great Gatsby",
          author: "F. Scott Fitzgerald",
          genre: "Fiction",
          image: "path/to/image1.jpg",
          description: "A classic novel set in the 1920s.",
        },
        {
          id: 2,
          title: "To Kill a Mockingbird",
          author: "Harper Lee",
          genre: "Fiction",
          image: "path/to/image2.jpg",
          description: "A novel about racial injustice in the American South.",
        },
        {
          id: 3,
          title: "1984",
          author: "George Orwell",
          genre: "Fiction",
          image: "path/to/image3.jpg",
          description: "A dystopian novel about totalitarianism.",
        },
        // Non-Fiction Books
        {
          id: 4,
          title: "Sapiens: A Brief History of Humankind",
          author: "Yuval Noah Harari",
          genre: "Non-Fiction",
          image: "path/to/image4.jpg",
          description: "An exploration of the history of humanity.",
        },
        {
          id: 5,
          title: "Educated",
          author: "Tara Westover",
          genre: "Non-Fiction",
          image: "path/to/image5.jpg",
          description:
            "A memoir about a woman who escapes her survivalist family.",
        },
        {
          id: 6,
          title: "The Immortal Life of Henrietta Lacks",
          author: "Rebecca Skloot",
          genre: "Non-Fiction",
          image: "path/to/image6.jpg",
          description: "The story of the woman behind the HeLa cells.",
        },
        // Science Books
        {
          id: 7,
          title: "A Brief History of Time",
          author: "Stephen Hawking",
          genre: "Science",
          image: "path/to/image7.jpg",
          description: "A popular science book on cosmology.",
        },
        {
          id: 8,
          title: "The Gene: An Intimate History",
          author: "Siddhartha Mukherjee",
          genre: "Science",
          image: "path/to/image8.jpg",
          description: "A history of the gene as a concept.",
        },
        {
          id: 9,
          title: "Cosmos",
          author: "Carl Sagan",
          genre: "Science",
          image: "path/to/image9.jpg",
          description: "An exploration of the universe and our place in it.",
        },
        // History Books
        {
          id: 10,
          title: "Guns, Germs, and Steel",
          author: "Jared Diamond",
          genre: "History",
          image: "path/to/image10.jpg",
          description:
            "An analysis of the factors that shaped human societies.",
        },
        {
          id: 11,
          title: "The Silk Roads: A New History of the World",
          author: "Peter Frankopan",
          genre: "History",
          image: "path/to/image11.jpg",
          description:
            "A history of the world from the perspective of the Silk Roads.",
        },
        {
          id: 12,
          title: "The Histories",
          author: "Herodotus",
          genre: "History",
          image: "path/to/image12.jpg",
          description: "The classic work of history by Herodotus.",
        },
        // Math Books
        {
          id: 13,
          title: "The Joy of x: A Guided Tour of Math, from One to Infinity",
          author: "Steven Strogatz",
          genre: "Math",
          image: "path/to/image13.jpg",
          description: "A book on the beauty of mathematics.",
        },
        {
          id: 14,
          title:
            "Fermat's Enigma: The Epic Quest to Solve the World's Greatest Mathematical Problem",
          author: "Simon Singh",
          genre: "Math",
          image: "path/to/image14.jpg",
          description: "A book about the quest to solve Fermat's Last Theorem.",
        },
        {
          id: 15,
          title: "Gödel, Escher, Bach: An Eternal Golden Braid",
          author: "Douglas Hofstadter",
          genre: "Math",
          image: "path/to/image15.jpg",
          description:
            "A book exploring the connections between mathematics, art, and music.",
        },
      ],
    };
  },
  computed: {
    uniqueGenres() {
      const genres = this.books.map((book) => book.genre);
      return [...new Set(genres)]; // Use Set to remove duplicates
    },
    filteredBooks() {
      if (!this.activeTab) return []; // If no tab is selected, return an empty array
      return this.books.filter((book) => book.genre === this.activeTab);
    },
  },
  methods: {
    showTab(genre) {
      this.activeTab = genre;
    },
    showBookDetail(book) {
      this.selectedBook = book;
    },
    closeDetail() {
      this.selectedBook = null;
    },
    updateAction(id) {
      alert("Update book with ID:", id);
      // Add update logic here
    },
    deleteAction(id) {
      alert("Delete book with ID:", id);
      // Add delete logic here
    },
  },
};
</script>

<style scoped>
.nav-tabs .nav-link.active {
  background-color: #007bff; /* Bootstrap primary color */
  color: white;
}
.nav-tabs .nav-link {
  cursor: pointer;
}

.book-detail-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
}

.book-detail-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  max-width: 500px;
  width: 90%;
}

.book-detail-content button {
  margin-top: 10px;
}
</style>
