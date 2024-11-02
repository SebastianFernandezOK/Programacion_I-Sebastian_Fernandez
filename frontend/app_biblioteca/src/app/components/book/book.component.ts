import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';

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
  
  constructor(private router: Router) {}

  // Método para navegar a la página de detalles del libro
  navigateToBookDetails() {
    this.router.navigate([`/book`, this.id]); 
  }

  onDeleteBook() {
    // Lógica para eliminar el libro
  }

  onEditBook() {
    // Lógica para editar el libro
  }

  onRentBook() {
    // Lógica para rentar el libro
  }
}
