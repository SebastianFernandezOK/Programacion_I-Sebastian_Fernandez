import { Component, Input, OnInit, ChangeDetectorRef } from '@angular/core';
import { RentsService } from '../../../services/rents.service'; 

@Component({
  selector: 'app-see-rents',
  templateUrl: './see-rents.component.html',
  styleUrls: ['./see-rents.component.css']
})
export class SeeRentsComponent implements OnInit {
  @Input() id: number = 0;
  @Input() title: string = 'Default title';
  @Input() author: string = 'Default author';
  @Input() daysLeft: Date = new Date();
  @Input() rentedBy: string = "Default user";
  @Input() image: string = 'media/default-book-cover.jpg';

  loans: any[] = []; // Para almacenar los préstamos
  selectedLoan: any; // Para el modal de préstamo seleccionado
  renewLoanModal: any;

  constructor(
    private cdr: ChangeDetectorRef, 
    private rentsService: RentsService // Inyecta el servicio
  ) {}

  ngOnInit() {
    this.loadRents(); // Llama a la función para cargar los préstamos
  }

  // Cargar todos los préstamos usando el servicio RentsService
  loadRents() {
    this.rentsService.getRents().subscribe(
      (response: any) => {
        this.loans = response.prestamos; // Asigna los préstamos obtenidos
        console.log('Préstamos cargados:', this.loans);
      },
      (error) => {
        console.error('Error al cargar préstamos:', error);
      }
    );
  }

  // Función para calcular los días restantes
  calculateDaysLeft(): number {
    const today = new Date();
    const remainingTime = new Date(this.daysLeft).getTime() - today.getTime();
    return Math.ceil(remainingTime / (1000 * 3600 * 24));
  }

  // Verifica si un préstamo está por vencer
  isAboutToExpire(): boolean {
    return this.calculateDaysLeft() <= 3;
  }

  // Abre el modal de renovación y asigna el préstamo seleccionado
  openRenewModal(loan: any) {
    this.selectedLoan = loan;
    this.renewLoanModal.show();
  }

  // Renueva el préstamo seleccionado usando el servicio
  renewLoan() {
    if (this.selectedLoan) {
      this.rentsService.renewLoan(this.selectedLoan.id).subscribe(
        (response) => {
          console.log('Préstamo renovado:', response);
          this.renewLoanModal.hide(); // Cierra el modal al finalizar
        },
        (error) => {
          console.error('Error al renovar el préstamo:', error);
        }
      );
    }
  }

  // Elimina un préstamo de la lista
  deleteLoan(index: number) {
    const loanToDelete = this.loans[index];
    if (loanToDelete) {
      this.rentsService.deleteLoan(loanToDelete.id).subscribe(
        (response) => {
          console.log('Préstamo eliminado:', response);
          this.loans.splice(index, 1); // Elimina el préstamo de la lista
        },
        (error) => {
          console.error('Error al eliminar el préstamo:', error);
        }
      );
    }
  }
}
