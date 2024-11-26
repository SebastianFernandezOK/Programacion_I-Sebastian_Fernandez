import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';
import { BookService } from '../../services/book.service';

@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.css']
})
export class BookComponent {
  @Input() id!: number; // Propiedad de entrada para el ID del libro
  @Input() title!: string;
  @Input() author!: string;
  @Input() quantity!: number;
  @Input() review!: string;
  @Input() image!: string;

  // Propiedades para el formulario de edición
  isEditing: boolean = false;
  updatedTitle: string = '';
  updatedAuthor: string = '';
  updatedQuantity: number = 0;
  updatedReview: string = '';

  constructor(private router: Router, private bookService: BookService) {}

  // Método para navegar a la página de detalles del libro
  navigateToBookDetails() {
    this.router.navigate([`/book`, this.id]); 
  }

  onDeleteBook() {
    this.bookService.deleteBook(this.id).subscribe(() => {
      // Aquí podrías agregar lógica para mostrar un mensaje de éxito o redirigir a otra página
      console.log('Libro eliminado');
    });
  }

  onEditBook() {
    this.isEditing = true;
    // Guardamos los valores actuales en el formulario
    this.updatedTitle = this.title;
    this.updatedAuthor = this.author;
    this.updatedQuantity = this.quantity;
    this.updatedReview = this.review;
  }

  updateBook() {
    const updatedBookData = {
      titulo: this.updatedTitle,
      autor: this.updatedAuthor,
      cantidad: this.updatedQuantity,
      reseña: this.updatedReview
    };

    this.bookService.updateBook(this.id, updatedBookData).subscribe(() => {
      console.log('Libro actualizado');
      this.isEditing = false; // Oculta el formulario
      // Aquí podrías agregar lógica para mostrar un mensaje de éxito o actualizar la vista
    });
  }

  onRentBook() {
    // Lógica para rentar el libro
  }
}
