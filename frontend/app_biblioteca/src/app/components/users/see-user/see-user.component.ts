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
    this.loadUsers(); // Cargar usuarios al iniciar el componente
    this.editUserModal = new window.bootstrap.Modal(
      document.getElementById('editUserModal')
    );
  }
 
  // Método para cargar usuarios
  loadUsers(): void {
    if (this.selectedRole === 'all') {
      this.usuariosService.getUsers().subscribe((rta: any) => {
        console.log('usuarios api: ', rta);
        this.users = rta.usuarios || [];
      });
    } else {
      this.usuariosService.getUsersByRole(this.selectedRole).subscribe((rta: any) => {
        console.log('usuarios filtrados por rol: ', rta);
        this.users = rta.usuarios || [];
      });
    }
  }

  // Función para manejar el cambio de rol
  onRoleChange(): void {
    this.loadUsers(); // Cargar usuarios filtrados por rol cuando cambia el rol
  }  

  // Función para eliminar un usuario
  deleteUser(usuarioID: number): void {
    this.usuariosService.deleteUser(usuarioID).subscribe(() => {
      this.users = this.users.filter(user => user.usuarioID !== usuarioID);
    }, error => {
      console.error('Error al eliminar el usuario:', error);
    });
  }

  // Función para abrir el modal con los datos del usuario seleccionado
  openEditModal(user: User): void {
    this.selectedUser = { ...user }; // Clonamos el usuario seleccionado
    this.editUserModal.show();
  }

  // Función para guardar los cambios del usuario editado
  saveUser(): void {
    console.log('Usuario a actualizar:', this.selectedUser);
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
