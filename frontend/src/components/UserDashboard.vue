<template>
  <nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="#">Library Management</router-link>
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
            <router-link class="nav-link active" to="/"
              >Home
              <span class="visually-hidden">(current)</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/librarian_stats"
              >STATS</router-link
            >
          </li>

          <li class="nav-item">
            <router-link class="nav-link" to="/OURBOOKS"
              >OUR BOOKS
            </router-link>
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
  <div class="container mt-5">
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
    <div>
      <!-- Book Tabs -->
      <br />
      <br />
      <br />
      <hr />

      <small>More Features Coming Soon</small>
      <hr />

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
                    @click="openModal(book.id)"
                  >
                    Request a Book
                  </button>

                  <button
                    type="button"
                    class="btn btn-success me-2"
                    @click="triggerDownload"
                  >
                    Download PDF
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
  <!-- Custom Modal -->
  <div v-if="showModal" class="custom-modal-overlay" @click.self="closeModal">
    <div class="custom-modal-content">
      <div class="custom-modal-header">
        <h5>Request Book</h5>
        <button
          type="button"
          class="btn btn-outline-danger"
          @click="closeModal"
        >
          ×
        </button>
      </div>
      <div class="custom-modal-body">
        <form @submit.prevent="submitRequest">
          <div class="mb-3">
            <label for="days" class="form-label"
              >How many days would you like to borrow this book?</label
            >
            <input
              type="number"
              class="form-control"
              id="days"
              v-model="days"
              required
            />
          </div>
          <button type="submit" class="btn btn-primary">Submit Request</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      bookId: null,
      days: "",
      showModal: false,
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
    LOGOUT() {
      // Clear the "students" data from localStorage or sessionStorage
      localStorage.removeItem("librarian");
      sessionStorage.removeItem("librarian");
      this.$router.push("/");
    },
    triggerDownload() {
      // Create a temporary anchor element
      const link = document.createElement("a");

      // Set the href to the PDF file URL
      link.href =
        "https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/wd/product/external-storage/my_book/my-book-usb-3-0-hdd-recertified/user-manual-Unencrypted%20drives-my-book-usb-recertified.pdf";

      // Set the download attribute with a desired filename
      link.setAttribute("download", "user-manual.pdf");

      // Append the link to the body (necessary for Firefox)
      document.body.appendChild(link);

      // Trigger the download by programmatically clicking the link
      link.click();

      // Remove the link from the body
      document.body.removeChild(link);
    },
    showTab(genre) {
      this.activeTab = genre;
    },
    openModal(bookId) {
      this.bookId = bookId;
      this.days = "";
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    submitRequest() {
      if (this.days && !isNaN(this.days) && this.days > 0) {
        // Handle the request

        this.isRequested = true; // Disable the button
        alert(`Book ID ${this.bookId} requested for ${this.days} days.`);
        this.closeModal();
        // Add your logic to handle the request here
      } else {
        alert("Please enter a valid number of days.");
        this.closeModal();
      }
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
  },
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
.custom-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.custom-modal-content {
  background: white;
  padding: 20px;
  border-radius: 5px;
  max-width: 500px;
  width: 100%;
  position: relative;
}

.custom-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.custom-modal-header .btn-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
}

.custom-modal-body {
  padding: 10px 0;
}

.btn-close {
  font-size: 1.5rem;
  cursor: pointer;
}
</style>
