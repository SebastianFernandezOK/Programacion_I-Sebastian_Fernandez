import { Component, Input } from '@angular/core'; 
import { Router } from '@angular/router';
import { UsuariosService } from '../../../services/usuarios.service';

@Component({
  selector: 'app-see-user',
  templateUrl: './see-user.component.html',
  styleUrls: ['./see-user.component.css']
})
export class SeeUserComponent {
  
  @Input() id: number = 0;
  @Input() nombre: string = '';
  @Input() apellido: string = '';
  @Input() email: string = '';
  @Input() telefono: string = '0';
  @Input() rol: string = '';

  user: any;
  
  constructor(
    private router: Router,
    private usuariosService: UsuariosService
  ) {}

  ngOnInit() {
    this.usuariosService.getUser(this.id).subscribe((rta:any) => {
      console.log('usuarios api: ', rta);
      this.user = rta || [];
    });
  }
 
  deleteUser(usuarioID: number): void {
    this.usuariosService.deleteUser(usuarioID).subscribe(() => {}, error => {
      console.error('Error al eliminar el usuario:', error);
    });
  }

  openEditModal(user: any): void {
    console.log('User:', user);
  }

  // openEditModal(user: User): void {
  //   this.selectedUser = { ...user }; // Clonamos el usuario seleccionado
  //   this.editUserModal.show();
  // }

  // // Función para guardar los cambios del usuario editado
  // saveUser(): void {
  //   console.log('Usuario a actualizar:', this.selectedUser); // Debugging
  //   this.usuariosService.updateUser(this.selectedUser.usuarioID, this.selectedUser)
  //     .subscribe(
  //       response => {
  //         console.log('Usuario actualizado:', response);
  //         const index = this.users.findIndex(u => u.usuarioID === this.selectedUser.usuarioID);
  //         if (index !== -1) {
  //           this.users[index] = { ...this.selectedUser }; // Actualiza el usuario en la lista
  //         }
  //         this.editUserModal.hide(); // Cierra el modal después de guardar
  //       },
  //       error => {
  //         console.error('Error al actualizar el usuario:', error);
  //       }
  //     );
  // }
}
