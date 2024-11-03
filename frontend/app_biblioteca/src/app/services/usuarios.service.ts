import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsuariosService {
  url = '/api';
  
  constructor(private httpClient: HttpClient) { }

  getUsers(page: number = 1): Observable<any> {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}` 
    });
    const requestOptions = { headers: headers };
    console.log(`Page on getUsers: ${page}`);
    return this.httpClient.get(`${this.url}/usuarios?page=${page}`, requestOptions);
  }
  
<<<<<<< HEAD
  getUsersByRole(rol: string, page: number = 1): Observable<any> {
=======
  getUser(usuarioID: number): Observable<any> {
>>>>>>> 48c3bd332ba56be2b1ec5652fa0086c6b60b95c8
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };

<<<<<<< HEAD
    return this.httpClient.get(`${this.url}/usuarios?rol=${encodeURIComponent(rol)}&page=${page}`, requestOptions);
=======
    return this.httpClient.get(`${this.url}/usuario/${usuarioID}`, requestOptions);
>>>>>>> 48c3bd332ba56be2b1ec5652fa0086c6b60b95c8
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
