import { Component, ChangeDetectorRef } from '@angular/core';
declare var window: any; // Para usar Bootstrap Modal con JavaScript

interface Loan {
  title: string;
  author: string;
  daysLeft: number;
  rentedBy: string;
  imageUrl: string;
}

@Component({
  selector: 'app-see-rents',
  templateUrl: './see-rents.component.html',
  styleUrls: ['./see-rents.component.css']
})
export class SeeRentsComponent {
  loans: Loan[] = [
    {
      title: 'Book Title 1',
      author: 'Author Name',
      daysLeft: 5,
      rentedBy: 'Mason Lopez',
      imageUrl: 'images (3).jfif'
    },
    {
      title: 'Book Title 2',
      author: 'Author Name',
      daysLeft: 12,
      rentedBy: 'Sophia Wilson',
      imageUrl: 'images (2).jfif'
    },
    {
      title: 'Book Title 3',
      author: 'Author Name',
      daysLeft: 3,
      rentedBy: 'Alice Smith',
      imageUrl: 'images (4).jfif'
    },
    {
      title: 'Book Title 4',
      author: 'Author Name',
      daysLeft: 7,
      rentedBy: 'Bob Johnson',
      imageUrl: 'images (3).jfif'
    },
    {
      title: 'Book Title 5',
      author: 'Author Name',
      daysLeft: 15,
      rentedBy: 'Charlie Brown',
      imageUrl: 'images (2).jfif'
    },
    {
      title: 'Book Title 6',
      author: 'Author Name',
      daysLeft: 9,
      rentedBy: 'Diana Prince',
      imageUrl: 'images (4).jfif'
    },
  ];

  selectedLoan: Loan | null = null; // Inicializar como null
  renewLoanModal: any;
  daysLeft: number | null = null; // Nueva propiedad para el modal

  constructor(private cdr: ChangeDetectorRef) {}

  ngOnInit() {
    // Inicializar el modal
    this.renewLoanModal = new window.bootstrap.Modal(document.getElementById('renewLoanModal'));
    this.cdr.detectChanges(); // Forzar la detección de cambios
  }

  openRenewModal(loan: Loan) {
    this.selectedLoan = { ...loan }; // Clonar el préstamo seleccionado
    this.daysLeft = this.selectedLoan.daysLeft; // Inicializar la propiedad auxiliar
    this.renewLoanModal.show(); // Mostrar el modal
  }

  renewLoan() {
    if (this.selectedLoan && this.daysLeft !== null) { // Verificar que daysLeft no sea null
      const index = this.loans.findIndex(loan => loan.title === this.selectedLoan!.title);
      if (index !== -1) {
        this.loans[index].daysLeft = this.daysLeft; // Actualizar días restantes
        this.renewLoanModal.hide(); // Cerrar el modal
      }
    }
  }

  // Eliminar préstamo
  deleteLoan(index: number) {
    this.loans.splice(index, 1); // Eliminar préstamo por índice
  }
}
