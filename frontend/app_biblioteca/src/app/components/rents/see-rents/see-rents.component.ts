import { Component, Input, ChangeDetectorRef } from '@angular/core';
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
  
  @Input() loans: Loan[] = [];  // Recibe la lista de préstamos del componente padre

  selectedLoan: Loan | null = null; 
  renewLoanModal: any;
  daysLeft: number | null = null; 

  constructor(private cdr: ChangeDetectorRef) {}

  ngOnInit() {
    // Inicializar el modal
    this.renewLoanModal = new window.bootstrap.Modal(document.getElementById('renewLoanModal'));
    this.cdr.detectChanges(); 
  }

  openRenewModal(loan: Loan) {
    this.selectedLoan = { ...loan }; 
    this.daysLeft = this.selectedLoan.daysLeft; 
    this.renewLoanModal.show(); 
  }

  renewLoan() {
    if (this.selectedLoan && this.daysLeft !== null) { 
      const index = this.loans.findIndex(loan => loan.title === this.selectedLoan!.title);
      if (index !== -1) {
        this.loans[index].daysLeft = this.daysLeft; 
        this.renewLoanModal.hide(); 
      }
    }
  }

  deleteLoan(index: number) {
    this.loans.splice(index, 1); 
  }
}
