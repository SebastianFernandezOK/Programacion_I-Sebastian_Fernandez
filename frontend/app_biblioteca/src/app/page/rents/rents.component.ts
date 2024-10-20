import { Component } from '@angular/core';
import { RentsService } from '../../services/rents.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-rents',
  templateUrl: './rents.component.html',
  styleUrl: './rents.component.css'
})
export class RentsComponent {
constructor(private route: ActivatedRoute, private rentsService: RentsService) {}

rents: any[] = [];

searchQuery = '';
filteredRents = this.rents;

ngOnInit() {
  this.getRents( 1 );
}

getRents( page: Number ) {
  this.rentsService.getRents().subscribe((answer:any) => {
    console.log('prestamos api: ',answer);
    this.rents = answer.prestamos || [];
    this.filteredRents = [...this.rents];
  })
}

filterRents() {
  this.filteredRents = this.rents.filter((rent) => {
    return rent.titulo.toLowerCase().includes(this.searchQuery.toLowerCase());
  });
}  

}