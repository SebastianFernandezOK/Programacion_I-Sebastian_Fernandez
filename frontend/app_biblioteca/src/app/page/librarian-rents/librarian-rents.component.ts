import { Component } from '@angular/core';
import { RentsService } from '../../services/rents.service';

@Component({
  selector: 'app-librarian-rents',
  templateUrl: './librarian-rents.component.html',
  styleUrls: ['./librarian-rents.component.css']
})
export class LibrarianRentsComponent {
  rents: any[] = [];
  searchQuery = '';
  filteredRents: any[] = [];
  
  page = 1; // Página actual
  pages = 1; // Total de páginas

  constructor(private rentService: RentsService) {}

  ngOnInit() {
    this.getRents(this.page); // Obtener préstamos en la página inicial
  }

  getRents(page: number) {
    this.page = page; // Actualiza la página actual
    this.rentService.getRents(page).subscribe(
      (answer: any) => {
        console.log('Respuesta de la API:', answer);
        const today = new Date();
        this.rents = answer.prestamos || [];
        this.pages = answer.pages || 1; // Asegúrate de que estás usando 'pages' correcto

        // Actualiza los días restantes
        this.updateDaysLeft(today);

        // Filtra los préstamos y muestra solo los de la página actual
        this.filterRents(); 
      },
      (error) => console.error('Error al obtener préstamos:', error)
    );
}

updateDaysLeft(today: Date) {
    this.rents.forEach(prestamo => {
        prestamo.daysLeft = prestamo.fecha_devolucion
            ? Math.ceil((new Date(prestamo.fecha_devolucion).getTime() - today.getTime()) / (1000 * 3600 * 24))
            : 0;
    });
}

filterRents() {
    const today = new Date();
    
    // Filtra por el título del libro si hay una búsqueda activa
    const filteredBySearch = this.rents.filter(prestamo => {
      return prestamo.libro && prestamo.libro.titulo &&
             prestamo.libro.titulo.toLowerCase().includes(this.searchQuery.toLowerCase());
    });

    // Pagina los resultados filtrados
    const startIndex = (this.page - 1) * 9; // Calcula el índice inicial para la página
    const endIndex = startIndex + 9; // Calcula el índice final
    this.filteredRents = filteredBySearch.slice(startIndex, endIndex); // Slicing para obtener solo los libros de la página actual

    console.log('Total de libros mostrados:', this.filteredRents.length); // Log para depuración
}

trackRent(index: number, rent: any) {
    return rent.prestamoID; // O la propiedad que sea única para cada préstamo
}
}