import { Component } from '@angular/core';
import { RentsService } from '../../services/rents.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-librarian-rents',
  templateUrl: './librarian-rents.component.html',
  styleUrls: ['./librarian-rents.component.css']
})
export class LibrarianRentsComponent {
  rents: any[] = [];
  searchQuery = '';
  filteredRents = this.rents;

  constructor(private route: ActivatedRoute, private rentsService: RentsService) {}

  ngOnInit() {
    this.getRents(1);
  }

  getRents(page: number) {
    this.rentsService.getRents().subscribe(
      (answer: any) => {
        const today = new Date(); // Cambiado a un objeto Date
        this.rents = answer.prestamos || [];
        this.rents.forEach(prestamo => {
          prestamo.daysLeft = prestamo.fecha_devolucion
            ? Math.ceil((new Date(prestamo.fecha_devolucion).getTime() - today.getTime()) / (1000 * 3600 * 24))
            : null;
        });
        this.filteredRents = [...this.rents];
      },
      (error) => console.error('Error al obtener préstamos:', error)
    );
  }

  filterRents() {
    this.filteredRents = this.rents.filter((prestamos) => {
      return prestamos.titulo.toLowerCase().includes(this.searchQuery.toLowerCase());
    });
  }
}
