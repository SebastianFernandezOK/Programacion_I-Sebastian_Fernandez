import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BookService } from '../../services/book.service';

@Component({
  selector: 'app-book-details',
  templateUrl: './book-details.component.html',
  styleUrls: ['./book-details.component.css']
})
export class BookDetailsComponent implements OnInit {
  book: any; // Propiedad para almacenar la información del libro

  constructor(
    private route: ActivatedRoute,
    private bookService: BookService
  ) {}

  ngOnInit(): void {
    // Obtén el ID del libro desde la URL y conviértelo a número
    const libroID = Number(this.route.snapshot.paramMap.get('id'));
    if (libroID) {
      // Llama al servicio para obtener los detalles del libro
      this.bookService.getBook(libroID).subscribe((data) => {
        this.book = data;
      });
    }
  }
}
