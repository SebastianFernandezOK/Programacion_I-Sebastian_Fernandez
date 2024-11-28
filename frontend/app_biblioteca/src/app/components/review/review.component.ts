import { Component,Input } from '@angular/core';
import { StarComponent } from '../star/star.component';
import { UsuariosService } from '../../services/usuarios.service';

@Component({
  selector: 'app-review',
  templateUrl: './review.component.html',
  styleUrl: './review.component.css'
})
export class ReviewComponent {
  @Input() id!: number; 
  @Input() rating: number = 0;
  @Input() comment: string = '';
  user: any = null;

  constructor(private usuariosService: UsuariosService) {}

  ngOnInit() {
    this.usuariosService.getUser(this.id).subscribe(user => {
    this.user = user;
  });
  }

  getUser(usuarioID: number): void  {
    this.usuariosService.getUserName(usuarioID).subscribe(user => {
      this.user = user;
    })
  }

}