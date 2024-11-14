import { Component, ViewEncapsulation } from '@angular/core';
import { AuthService } from '../../services/auth.service'
import { Router } from "@angular/router"
import { FormBuilder, FormGroup, Validators } from "@angular/forms"
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
})
export class LoginComponent {
  loginForm!: FormGroup;
  constructor(
    private authService: AuthService,
    private router:Router,
    private formBuilder: FormBuilder
  ) {
    this.loginForm = this.formBuilder.group({
      usuario_email: ["",Validators.required],
      usuario_contraseña: ["", Validators.required]
    })
  }
  irLogin(dataLogin: any) {
    this.authService.login(dataLogin).subscribe({
      next: (rta: any) => {
        alert('Credenciales correctas');
        // Guardar el token en sessionStorage 
        sessionStorage.setItem("token", rta.access_token);
        this.router.navigateByUrl("home");
      },
      error: (err: any) => {
        alert('Usuario o contraseña incorrecta');
        console.log('Error:', err);
        sessionStorage.removeItem("token");
      },
    });
  }
  

  sumbit(){
    if(this.loginForm.valid){
      this.irLogin(this.loginForm.value);
      
    }  else {
      alert("Los valores son requeridos")
    }
    
  }

}
