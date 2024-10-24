import { Component } from '@angular/core';
import { RentService } from '../../services/rent.service';

@Component({
  selector: 'app-librarian-rents',
  templateUrl: './librarian-rents.component.html',
  styleUrls: ['./librarian-rents.component.css']
})
export class LibrarianRentsComponent {
  rents: any[] = [];
  searchQuery = '';
  filteredRents: any[] = []; // Asegúrate de inicializar este arreglo

  constructor(private rentService: RentService) {}

  ngOnInit() {
    this.getRents(1); // Aquí pasa un número de página o el id correcto
  }
  
  getRents(page: number) {
    this.rentService.getRent(page).subscribe(
      (answer: any) => {
        console.log('Respuesta de la API:', answer); // Para verificar los datos
        const today = new Date(); // Obtener la fecha actual
        this.rents = answer.prestamos || []; // Asignar los préstamos
  
        // Procesar los préstamos para calcular los días restantes
        this.rents.forEach(prestamo => {
          prestamo.daysLeft = prestamo.fecha_devolucion
            ? Math.ceil((new Date(prestamo.fecha_devolucion).getTime() - today.getTime()) / (1000 * 3600 * 24))
            : null;
        });
  
        this.filteredRents = [...this.rents]; // Asignar a los préstamos filtrados
      },
      (error) => console.error('Error al obtener préstamos:', error)
    );
  }
  

  filterRents() {
    this.filteredRents = this.rents.filter(prestamo => {
      // Asegúrate de que la propiedad 'libro' y 'titulo' existan
      return prestamo.libro && prestamo.libro.titulo &&
             prestamo.libro.titulo.toLowerCase().includes(this.searchQuery.toLowerCase());
    });
  }
}
