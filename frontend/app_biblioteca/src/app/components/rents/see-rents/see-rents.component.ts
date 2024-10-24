import { Component, Input, ChangeDetectorRef } from '@angular/core';
import { RentsService } from '../../../services/rents.service'; 

declare var window: any; // Para usar Bootstrap Modal con JavaScript

@Component({
  selector: 'app-see-rents',
  templateUrl: './see-rents.component.html',
  styleUrls: ['./see-rents.component.css']
})
export class SeeRentsComponent {
  @Input() id: number = 0;
  @Input() title: string = 'Default title';
  @Input() author: string = 'Default author';
  @Input() daysLeft: Date = new Date();
  @Input() rentedBy: string = "Default user";
  @Input() image: string = 'media/default-book-cover.jpg';

  loans: any[] = []; // Array para almacenar los préstamos
  selectedLoan: any; // Para almacenar el préstamo seleccionado en el modal
  renewLoanModal: any;

  constructor(private cdr: ChangeDetectorRef, private rentsService: RentsService) {} // Inyecta el servicio

  ngOnInit() {
    this.renewLoanModal = new window.bootstrap.Modal(document.getElementById('renewLoanModal'));
  }

  // Función para calcular los días restantes
  calculateDaysLeft(): number {
    const today = new Date();
    const remainingTime = new Date(this.daysLeft).getTime() - today.getTime();
    return Math.ceil(remainingTime / (1000 * 3600 * 24));
  }

  // Función para verificar si el préstamo está a punto de vencer
  isAboutToExpire(): boolean {
    const daysRemaining = this.calculateDaysLeft();
    return daysRemaining <= 3; // Considera 3 días o menos como a punto de vencer
  }

  // Abre el modal de renovación y carga la información del préstamo seleccionado
  openRenewModal(loan: any) {
    this.selectedLoan = loan;
    this.renewLoanModal.show();
  }

  // Función para renovar el préstamo
  renewLoan() {
    if (this.selectedLoan) {
      this.rentsService.renewLoan(this.selectedLoan.id).subscribe(
        (response) => {
          console.log(`Préstamo renovado para: ${this.selectedLoan.title}`, response);
          this.renewLoanModal.hide();
          // Aquí puedes agregar lógica para actualizar el estado de tu componente si es necesario
        },
        (error) => {
          console.error('Error al renovar el préstamo:', error);
        }
      );
    }
  }

  // Función para eliminar el préstamo
  deleteLoan(index: number) {
    const loanToDelete = this.loans[index]; // Accede al préstamo por su índice
    if (loanToDelete) {
      this.rentsService.deleteLoan(loanToDelete.id).subscribe(
        (response) => {
          console.log(`Préstamo eliminado: ${loanToDelete.title}`, response);
          this.loans.splice(index, 1); // Elimina el préstamo de la lista
          // Aquí puedes agregar lógica para actualizar la vista si es necesario
        },
        (error) => {
          console.error('Error al eliminar el préstamo:', error);
        }
      );
    }
  }
}