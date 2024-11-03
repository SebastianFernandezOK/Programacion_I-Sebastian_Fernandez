import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BookService } from '../../services/book.service';


@Component({
  selector: 'app-book-details',
  templateUrl: './book-details.component.html',
  styleUrls: ['./book-details.component.css']
})
export class BookDetailsComponent implements OnInit {
  bookId: number | null = null; // ID del libro
  titulo: string = ''; // Título del libro
  image: string = ''; // Ruta de la imagen del libro
  editorial: string = ''; // Editorial del libro
  genero: string = ''; // Genero del libro
  autores: string = ''; // Autor del libro
  cantidad: number = 0; // Cantidad de copias disponibles

  constructor(
    private route: ActivatedRoute,
    private bookService: BookService
  ) {}

  ngOnInit() {
    // Obtén el ID del libro desde la URL
    this.bookId = Number(this.route.snapshot.paramMap.get('id'));
    // Llama a la función para obtener los detalles del libro
    this.getBook(this.bookId);
  }

  // Función para obtener los detalles del libro
  getBook(id: number) {
    this.bookService.getBook(id).subscribe((data: any) => {
      this.titulo = data.titulo;
      this.image = data.image;
      console.log("Ruta de la imagen:", this.image); // Verificar ruta en la consola
      this.editorial = data.editorial;
      this.cantidad = data.cantidad;
      this.genero = data.genero;
  
      if (data.autores && data.autores.length > 0) {
        this.autores = data.autores.map((autor: any) => `${autor.autor_nombre} ${autor.autor_apellido}`).join(', ');
      }
    });
  }
  
}
