import { Component, EventEmitter, Input, Output } from '@angular/core';


@Component({
  selector: 'app-paginate',
  templateUrl: './paginate.component.html',
  styleUrls: ['./paginate.component.css'] 
})


export class PaginateComponent {
  @Input() page: number = 1;
  @Input() pages: number = 1;
  @Output() pageChange = new EventEmitter<number>();
  
    get range(): number[] {
      return Array.from({ length: this.pages }, (_, i) => i + 1);
    }
  
    goToPage(pageNumber: number) {
      if (pageNumber >= 1 && pageNumber <= this.pages) {
          this.page = pageNumber;
          this.pageChange.emit(pageNumber); // Emitir el cambio de página
          console.log(`Cambiando a la página: ${pageNumber}`); // Log para depuración
      }
  }
  
    
  
    
  }

