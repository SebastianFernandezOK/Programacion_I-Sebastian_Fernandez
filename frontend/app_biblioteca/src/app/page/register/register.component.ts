import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
})
export class RegisterComponent {
  registerForm!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    this.registerForm = this.formBuilder.group({
      usuario_nombre: ['', Validators.required],
      usuario_apellido: ['', Validators.required],
      usuario_email: ['', [Validators.required, Validators.email]],  // Validación de email
      usuario_contraseña: ['', [Validators.required, Validators.minLength(6)]],  // Validación de longitud
      confirmPassword: ['', [Validators.required]],  // Campo de confirmación
      usuario_telefono: ['', [Validators.required, Validators.pattern(/^[0-9]*$/)]],  // Solo números
    }, { validator: this.passwordMatchValidator });
  }

   // Validador para verificar que las contraseñas coincidan
   passwordMatchValidator(form: FormGroup) {
    return form.get('usuario_contraseña')?.value === form.get('confirmPassword')?.value
      ? null : { mismatch: true };
  }

  submit() {
    if (this.registerForm.valid) {
      console.log('Form data:', this.registerForm.value);
      this.registerUser(this.registerForm.value);
    } else {
      alert('All fields are required and must be valid!');
    }
  }

  registerUser(registerData: any) {
    this.authService.register(registerData).subscribe({
      next: (response: any) => {
        alert('Registration successful!');
        console.log('Success:', response);
        this.router.navigateByUrl('/login'); // Redirect to login page
      },
      error: (error: any) => {
        alert('Registration failed');
        console.error('Error:', error);
      },
    });
  }
}
