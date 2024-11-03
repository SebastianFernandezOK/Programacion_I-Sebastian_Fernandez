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
