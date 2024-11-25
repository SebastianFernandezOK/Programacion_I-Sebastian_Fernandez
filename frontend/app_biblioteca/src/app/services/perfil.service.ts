import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PerfilService {
  url = '/api';

  constructor(private httpClient: HttpClient) {}

  // Obtener los datos del perfil del usuario por su ID
  getUserProfileById(usuarioID: number): Observable<any> {
    const token = sessionStorage.getItem('token');
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);
    
    return this.httpClient.get(`${this.url}/usuario/${usuarioID}`, { headers });
  }

  // Actualizar el perfil del usuario
  updateUser(usuarioID: number, userData: any): Observable<any> {
    const token = sessionStorage.getItem('token');
    const headers = new HttpHeaders()
      .set('Authorization', `Bearer ${token}`)
      .set('Content-Type', 'application/json');

    return this.httpClient.put(`${this.url}/usuario/${usuarioID}`, userData, { headers });
  }
}
