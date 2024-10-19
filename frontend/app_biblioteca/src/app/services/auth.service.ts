import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable, take } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  url = '/api';
  constructor(
    private httpClient: HttpClient,
    private router:Router
  ) { }

  login(dataLogin:any): Observable<any> {
    // let dataLogin = {
    //   usuario_email: "hola@gmail",
    //   usuario_contraseña: "123"
    // }

    return this.httpClient.post(this.url+'/auth/login', dataLogin).pipe(take(1));
  }
  
  register(dataRegister: any): Observable<any> {
    return this.httpClient.post(this.url + '/auth/register', dataRegister).pipe(take(1));
  }

  logout(){
    localStorage.removeItem("token");
    this.router.navigateByUrl("home");
  }
}

