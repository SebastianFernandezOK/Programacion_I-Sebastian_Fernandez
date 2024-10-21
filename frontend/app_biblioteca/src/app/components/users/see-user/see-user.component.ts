import { Component } from '@angular/core'; 
import { Router } from '@angular/router';
import { UsuariosService } from '../../../services/usuarios.service';
declare var window: any; // Esto es para usar Bootstrap Modal con JavaScript

interface User {
  usuarioID: number;
  usuario_nombre: string;
  usuario_apellido: string;
  usuario_email: string;
  usuario_telefono: number;
  rol: string;
  photo: string; // Suponiendo que sigues usando una foto
}

@Component({
  selector: 'app-see-user',
  templateUrl: './see-user.component.html',
  styleUrls: ['./see-user.component.css']
})
export class SeeUserComponent {
  users: User[] = [];
  selectedUser: User = {
    usuarioID: 0,
    usuario_nombre: '',
    usuario_apellido: '',
    usuario_email: '',
    usuario_telefono: 0,
    rol: '',
    photo: ''
  };

  // Estado del rol seleccionado
  selectedRole: string = 'all'; // Por defecto, muestra todos los usuarios
  
  editUserModal: any;

  constructor(
    private router: Router,
    private usuariosService: UsuariosService
  ) {}

  ngOnInit() {
    this.usuariosService.getUsers().subscribe((rta:any) => {
      console.log('usuarios api: ', rta);
      this.users = rta.usuarios || [];
      this.editUserModal = new window.bootstrap.Modal(
        document.getElementById('editUserModal')
      );
    });
  }
 
  
  // Función para filtrar usuarios
get filteredUsers() {
  if (this.selectedRole === 'Todos') {
    return this.users; // Devuelve todos los usuarios si 'Todos' está seleccionado
  }
  return this.users.filter(user => user.rol === this.selectedRole); // Filtra por rol
}


  // Función para eliminar un usuario
  deleteUser(usuarioID: number): void {
    this.users = this.users.filter(user => user.usuarioID !== usuarioID);
  }

  // Función para abrir el modal con los datos del usuario seleccionado
  openEditModal(user: User): void {
    this.selectedUser = { ...user }; // Clonamos el usuario seleccionado
    this.editUserModal.show();
  }

  // Función para guardar los cambios del usuario editado
  saveUser(): void {
    console.log('Usuario a actualizar:', this.selectedUser); // Debugging
    this.usuariosService.updateUser(this.selectedUser.usuarioID, this.selectedUser)
      .subscribe(
        response => {
          console.log('Usuario actualizado:', response);
          const index = this.users.findIndex(u => u.usuarioID === this.selectedUser.usuarioID);
          if (index !== -1) {
            this.users[index] = { ...this.selectedUser }; // Actualiza el usuario en la lista
          }
          this.editUserModal.hide(); // Cierra el modal después de guardar
        },
        error => {
          console.error('Error al actualizar el usuario:', error);
        }
      );
  }
}
