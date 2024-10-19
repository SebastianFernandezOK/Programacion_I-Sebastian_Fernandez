import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BooksService } from '../../services/books.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {

  constructor(private route: ActivatedRoute, private booksService: BooksService) { }

  books: any[] = [];

  searchQuery = '';
  filteredBooks = this.books;


  ngOnInit(): void {
    this.getBooks( 1 );
  }


  getBooks(page: Number) {
    this.booksService.getBooks(page).subscribe((answer: any) => {
      console.log(answer);
      this.books = answer.libros || [];
      this.filteredBooks = [...this.books];
    });
  }

  // Filtrar libros basado en el campo de búsqueda
  filterBooks() {
    this.filteredBooks = this.books.filter(book =>
      book.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
      book.author.toLowerCase().includes(this.searchQuery.toLowerCase())
    );
  }
}
