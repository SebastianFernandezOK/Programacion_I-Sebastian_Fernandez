import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsuariosService {
  url = '/api';
  
  constructor(private httpClient: HttpClient) { }

  getUsers(page: number = 1, perPage: number = 9, nombre?: string, apellido?: string, nr_prestamos?: number, rol?: string): Observable<any> {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    let params: any = { page, per_page: perPage };
    if (nombre) params.nombre = nombre;
    if (apellido) params.apellido = apellido;
    if (nr_prestamos) params.nr_prestamos = nr_prestamos;
    if (rol && rol !== 'Todos') params.rol = rol;  

    return this.httpClient.get(`${this.url}/usuarios`, { headers, params });
}


  
  getUser(usuarioID: number): Observable<any> {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };

    return this.httpClient.get(`${this.url}/usuario/${usuarioID}`, requestOptions);
  }

  updateUser(usuarioID: number, userData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };
    return this.httpClient.put(`${this.url}/usuario/${usuarioID}`, userData, requestOptions);
  }

  // Método para eliminar un usuario
  deleteUser(usuarioID: number): Observable<void> {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    const requestOptions = { headers: headers };

    return this.httpClient.delete<void>(`${this.url}/usuario/${usuarioID}`, requestOptions);
  }
}
