import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class RentService {
  url = '/api';

  constructor(private httpClient: HttpClient) {}

  getRent(id: Number) {
    const auth_token = localStorage.getItem('token');
  
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
  
    const requestOptions = { headers: headers };
  
    // Si 'id' representa una página o un identificador, agrega el '/' correctamente
    return this.httpClient.get(`${this.url}/prestamo/${id}`, requestOptions).pipe(
      catchError((error) => {
        console.error('Error fetching rents:', error);
        return throwError(error);
      })
    );
  }  
}
