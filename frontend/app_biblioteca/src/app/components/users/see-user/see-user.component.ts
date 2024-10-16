import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { UsuariosService } from '../../../services/usuarios.service';
declare var window: any; // Esto es para usar Bootstrap Modal con JavaScript

interface User {
  usuarioID: number;
  nombre: string;
  apellido: string;
  email: string;
  telefono: number;
  rol: string;
  photo: string; // Suponiendo que sigues usando una foto
}

@Component({
  selector: 'app-see-user',
  templateUrl: './see-user.component.html',
  styleUrls: ['./see-user.component.css']
})
export class SeeUserComponent {
  
  //   { 
  //     usuarioID: 1, 
  //     nombre: 'John', 
  //     apellido: 'Doe', 
  //     email: 'johndoe@example.com', 
  //     telefono: 1234567890, 
  //     rol: 'User', 
  //     photo: 'descarga (1).png' 
  //   },
  //   { 
  //     usuarioID: 2, 
  //     nombre: 'Jane', 
  //     apellido: 'Smith', 
  //     email: 'janesmith@example.com', 
  //     telefono: 9876543210, 
  //     rol: 'Librarian', 
  //     photo: 'descarga (1).png' 
  //   },
  //   { 
  //     usuarioID: 3, 
  //     nombre: 'Admin', 
  //     apellido: 'User', 
  //     email: 'adminuser@example.com', 
  //     telefono: 5551234567, 
  //     rol: 'Admin', 
  //     photo: 'descarga (1).png' 
  //   },
  //   { 
  //     usuarioID: 4, 
  //     nombre: 'Michael', 
  //     apellido: 'Johnson', 
  //     email: 'michaeljohnson@example.com', 
  //     telefono: 1231231234, 
  //     rol: 'User', 
  //     photo: 'descarga (1).png' 
  //   },
  //   { 
  //     usuarioID: 5, 
  //     nombre: 'Emily', 
  //     apellido: 'Davis', 
  //     email: 'emilydavis@example.com', 
  //     telefono: 3213214321, 
  //     rol: 'Librarian', 
  //     photo: 'descarga (1).png' 
  //   },
  //   { 
  //     usuarioID: 6, 
  //     nombre: 'William', 
  //     apellido: 'Brown', 
  //     email: 'williambrown@example.com', 
  //     telefono: 4564564567, 
  //     rol: 'User', 
  //     photo: 'descarga (1).png' 
  //   },
  //   { 
  //     usuarioID: 7, 
  //     nombre: 'Olivia', 
  //     apellido: 'Martinez', 
  //     email: 'oliviamartinez@example.com', 
  //     telefono: 7897897890, 
  //     rol: 'Admin', 
  //     photo: 'descarga (1).png' 
  //   },
  //   { 
  //     usuarioID: 8, 
  //     nombre: 'James', 
  //     apellido: 'Garcia', 
  //     email: 'jamesgarcia@example.com', 
  //     telefono: 6546546543, 
  //     rol: 'User', 
  //     photo: 'descarga (1).png' 
  //   },
  //   { 
  //     usuarioID: 9, 
  //     nombre: 'Sophia', 
  //     apellido: 'Wilson', 
  //     email: 'sophiawilson@example.com', 
  //     telefono: 9879879870, 
  //     rol: 'Librarian', 
  //     photo: 'descarga (1).png' 
  //   },
  //   { 
  //     usuarioID: 10, 
  //     nombre: 'Mason', 
  //     apellido: 'Lopez', 
  //     email: 'masonlopez@example.com', 
  //     telefono: 3216549870, 
  //     rol: 'Admin', 
  //     photo: 'descarga (1).png' 
  //   }
  // 

  users: User[] = []
  selectedUser: User = {
    usuarioID: 0,
    nombre: '',
    apellido: '',
    email: '',
    telefono: 0,
    rol: '',
    photo: ''
  };
  
  editUserModal: any;

  constructor(
    private router: Router,
    private usuariosService: UsuariosService
  ){}
    
  ngOnInit() {
    this.usuariosService.getUsers().subscribe((rta:any) => {
      console.log('usuarios api: ',rta);
      this.users = rta.animales || [];
      this.editUserModal = new window.bootstrap.Modal(
        document.getElementById('editUserModal')
      );
      //this.filteredUsers = [...this.arrayUsuarios]
    })
  }
    
  // ngOnInit() {
  //   // Inicializamos el modal al cargar el componente
  //   this.editUserModal = new window.bootstrap.Modal(
  //     document.getElementById('editUserModal')
  //   );
  // }

  // Función para eliminar un usuario
  deleteUser(usuarioID: number): void {
    this.users = this.users.filter(user => user.usuarioID !== usuarioID);
    // Lógica adicional, como una llamada a una API para eliminar el usuario del servidor.
  }

  // Función para abrir el modal con los datos del usuario seleccionado
  openEditModal(user: User): void {
    this.selectedUser = { ...user }; // Clonamos el usuario seleccionado
    this.editUserModal.show();
  }

  // Función para guardar los cambios del usuario editado
  saveUser(): void {
    const index = this.users.findIndex(u => u.usuarioID === this.selectedUser.usuarioID);
    if (index !== -1) {
      this.users[index] = { ...this.selectedUser }; // Actualizamos el usuario en la lista
      this.editUserModal.hide(); // Cerramos el modal después de guardar
    } else {
      console.error("Usuario no encontrado"); // Manejo de errores
    }
  }
}
