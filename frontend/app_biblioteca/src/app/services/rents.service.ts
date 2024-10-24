import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, take } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class RentsService {
  url = '/api';
  
  constructor(private httpClient: HttpClient) {}

  // Obtener préstamos
  getRents(): Observable<any> {
    const auth_token = localStorage.getItem('token');

    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    const requestOptions = { headers: headers };

    return this.httpClient.get(this.url + '/prestamos', requestOptions).pipe(
      take(1),
      catchError((error) => {
        console.error('Error fetching rents:', error);
        return throwError(error);
      })
    );
  }

  // Renovar préstamo
  renewLoan(loanId: number): Observable<any> {
    const auth_token = localStorage.getItem('token');

    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.put(`${this.url}/prestamos/${loanId}/renew`, {}, { headers }).pipe(
      take(1),
      catchError((error) => {
        console.error('Error renewing loan:', error);
        return throwError(error);
      })
    );
  }

  // Eliminar préstamo
  deleteLoan(loanId: number): Observable<any> {
    const auth_token = localStorage.getItem('token');

    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.delete(`${this.url}/prestamos/${loanId}`, { headers }).pipe(
      take(1),
      catchError((error) => {
        console.error('Error deleting loan:', error);
        return throwError(error);
      })
    );
  }
}
