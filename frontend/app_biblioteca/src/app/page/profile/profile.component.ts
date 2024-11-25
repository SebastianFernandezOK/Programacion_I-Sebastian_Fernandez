import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { PerfilService } from '../../services/perfil.service';
import { ActivatedRoute, Router } from '@angular/router';
import jwtDecode from 'jwt-decode'; // Importación correcta de jwt-decode

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  profileForm: FormGroup;
  usuarioID!: number;

  constructor(
    private fb: FormBuilder,
    private perfilService: PerfilService,
    private route: ActivatedRoute,
    private router: Router
  ) {
    this.profileForm = this.fb.group({
      nombre: ['', Validators.required],
      lastName: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      phone: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    // Obtener el token desde sessionStorage
    const token = sessionStorage.getItem('token');
    if (token) {
      try {
        // Decodificar el token para obtener el usuarioID
        const decodedToken: any = jwtDecode(token);
        console.log('Token decodificado:', decodedToken); // Verificar la estructura del token decodificado

        // Ajustar según la estructura real del token decodificado
        this.usuarioID = decodedToken.usuarioID || decodedToken.sub || decodedToken.id || decodedToken.userId;

        console.log('ID del usuario obtenido del token:', this.usuarioID);

        // Verificar si tenemos un ID de usuario válido
        if (this.usuarioID) {
          this.perfilService.getUserProfileById(this.usuarioID).subscribe(
            (data) => {
              console.log('Datos del usuario obtenidos:', data);
              if (data && Object.keys(data).length > 0) {
                // Ajustar los nombres de los campos para que coincidan con los recibidos del backend
                this.profileForm.patchValue({
                  nombre: data.usuario_nombre,
                  lastName: data.usuario_apellido,
                  email: data.usuario_email,
                  phone: data.usuario_telefono
                });
              } else {
                console.error('Los datos del usuario están vacíos o incompletos');
                alert('No se pudieron obtener los datos del perfil. Asegúrate de estar autenticado.');
              }
            },
            (error) => {
              console.error('Error al obtener los datos del perfil', error);
              alert('Ocurrió un error al obtener los datos del perfil. Por favor, intenta nuevamente.');
            }
          );
        } else {
          console.error('No se pudo obtener un ID de usuario válido del token');
          alert('No estás autenticado. Por favor, inicia sesión primero.');
          this.router.navigate(['/login']);
        }
      } catch (error) {
        console.error('Error al decodificar el token:', error);
        alert('Hubo un problema con la autenticación. Por favor, inicia sesión de nuevo.');
        this.router.navigate(['/login']);
      }
    } else {
      console.error('No se encontró el token en sessionStorage');
      alert('No estás autenticado. Por favor, inicia sesión primero.');
      this.router.navigate(['/login']);
    }
  }

  onSave(): void {
    if (this.profileForm.valid) {
      const updatedData = {
        id: this.usuarioID,
        usuario_nombre: this.profileForm.value.nombre,
        usuario_apellido: this.profileForm.value.lastName,
        usuario_email: this.profileForm.value.email,
        usuario_telefono: this.profileForm.value.phone
      };

      console.log('Datos que se enviarán al backend para actualizar:', updatedData);

      // Actualizar los datos del perfil en el backend
      this.perfilService.updateUser(this.usuarioID, updatedData).subscribe(
        (response) => {
          console.log('Perfil actualizado con éxito', response);
          alert('Perfil actualizado con éxito');
        },
        (error) => {
          console.error('Error al actualizar el perfil', error);
          console.error('Detalles del error:', error.error); // Para más detalles sobre el error
          alert('Ocurrió un error al actualizar el perfil. Por favor, intenta nuevamente.');
        }
      );
    } else {
      alert('Por favor completa todos los campos correctamente antes de guardar.');
    }
  }
}
