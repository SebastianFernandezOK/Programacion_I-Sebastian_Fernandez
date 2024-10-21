import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.css']
})
export class BookComponent {
  @Input() title!: string; // Propiedad de entrada
  @Input() author!: string; // Propiedad de entrada
  @Input() quantity!: number; // Propiedad de entrada
  @Input() review!: string; // Propiedad de entrada
  @Input() image!: string; // Propiedad de entrada
  
  showInfo = false; // Estado para mostrar u ocultar la información del libro

  toggleInfo() {
    this.showInfo = !this.showInfo; // Cambia el estado de showInfo
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
