import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  books = [
    { 
      id: 1, 
      title: 'Libro 1', 
      author: 'Autor 1', 
      gender: 'Misterio', 
      quantity: 5, 
      image: 'image.jpg',
      review: 'Una fascinante historia de misterio.' // Añadir reseña
    },
    { 
      id: 2, 
      title: 'Libro 2', 
      author: 'Autor 2', 
      gender: 'Fantasía', 
      quantity: 2, 
      image: 'image.jpg',
      review: 'Una aventura mágica en un mundo paralelo.' // Añadir reseña
    },
    { 
      id: 3, 
      title: 'Libro 3', 
      author: 'Autor 3', 
      gender: 'Ciencia Ficción', 
      quantity: 4, 
      image: 'image.jpg',
      review: 'Explorando los límites del espacio y el tiempo.' // Añadir reseña
    },
    { 
      id: 4, 
      title: 'Libro 4', 
      author: 'Autor 4', 
      gender: 'Misterio', 
      quantity: 1, 
      image: 'image.jpg',
      review: 'Un misterio que desafía la lógica.' // Añadir reseña
    },
    { 
      id: 5, 
      title: 'Libro 5', 
      author: 'Autor 5', 
      gender: 'Romance', 
      quantity: 3, 
      image: 'image.jpg',
      review: 'Una historia de amor que trasciende el tiempo.' // Añadir reseña
    },
    { 
      id: 6, 
      title: 'Libro 6', 
      author: 'Autor 6', 
      gender: 'Histórico', 
      quantity: 6, 
      image: 'image.jpg',
      review: 'Un viaje a través de las épocas.' // Añadir reseña
    },
    { 
      id: 7, 
      title: 'Libro 7', 
      author: 'Autor 7', 
      gender: 'Aventura', 
      quantity: 7, 
      image: 'image.jpg',
      review: 'Una emocionante aventura que no puedes dejar de leer.' // Añadir reseña
    },
    { 
      id: 8, 
      title: 'Libro 8', 
      author: 'Autor 8', 
      gender: 'Terror', 
      quantity: 2, 
      image: 'image.jpg',
      review: 'Un relato que te hará temer la oscuridad.' // Añadir reseña
    },
    { 
      id: 9, 
      title: 'Libro 9', 
      author: 'Autor 9', 
      gender: 'Biografía', 
      quantity: 4, 
      image: 'image.jpg',
      review: 'La vida de una persona extraordinaria.' // Añadir reseña
    },
    { 
      id: 10, 
      title: 'Libro 10', 
      author: 'Autor 10', 
      gender: 'Poesía', 
      quantity: 5, 
      image: 'image.jpg',
      review: 'Versos que tocan el alma.' // Añadir reseña
    },
    // Más libros...
  ];

  searchQuery = '';
  filteredBooks = this.books;

  // Filtrar libros basado en el campo de búsqueda
  filterBooks() {
    this.filteredBooks = this.books.filter(book =>
      book.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
      book.author.toLowerCase().includes(this.searchQuery.toLowerCase())
    );
  }
}
