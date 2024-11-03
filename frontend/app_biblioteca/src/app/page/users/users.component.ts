import { Component, OnInit } from '@angular/core';
import { UsuariosService } from '../../services/usuarios.service';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {
  page: number = 1;         // Página actual
  pages: number = 1;        // Total de páginas (se ajustará tras la carga de datos)
  usuarios: any[] = [];     // Agregar esta propiedad para almacenar la lista de usuarios
  // Tema filtrado debe ir en pestaña general, componente usuario debe corresponder UNICAMENTE a cada usuario
  selectedRole: string = 'all'; // Por defecto, muestra todos los usuarios
  
  constructor(private usuariosService: UsuariosService) {}

  ngOnInit() {
    this.loadUsers();
    console.log(`Total de páginas inicializado: ${this.pages}`);
  }

  // Método para cargar usuarios
  loadUsers(page: number = 1) {
    this.usuariosService.getUsers(page).subscribe((data: any) => {
        if (data && typeof data.pages === 'number') {
          this.pages = data.pages; // Ajusta el valor total de `pages` con el total del backend
          console.log(`Páginas disponibles: ${this.pages}`);
        } else {
          console.error('Error: pages no encontrado en la respuesta');
        }
        this.usuarios = data.usuarios; // Cargar los usuarios
      },
      (error) => {
        console.error('Error al cargar usuarios:', error);
      }
    );
  }

  // Función para filtrar usuarios
  get filteredUsers() {
    if (this.selectedRole === 'Todos') {
      return this.usuarios; // Devuelve todos los usuarios si 'Todos' está seleccionado
    }
    return this.usuarios.filter(usuarios => usuarios.rol === this.selectedRole); // Filtra por rol
  }

  // Método para manejar el cambio de página
  onPageChange(newPage: number) {
    this.loadUsers(newPage);  // Recarga los usuarios en la nueva página
  }
}
