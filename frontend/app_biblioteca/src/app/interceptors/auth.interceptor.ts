import { Injectable } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from '../services/auth.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor(private authService: AuthService) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    console.log('Intercepting request:', req.url);

    // Verificar si el token está disponible en sessionStorage
    const authToken = sessionStorage.getItem('token');

    if (authToken) {
      // Si el token está presente, lo agregamos a la cabecera de la solicitud
      const authReq = req.clone({
        setHeaders: {
          Authorization: `Bearer ${authToken}`
        }
      });
      console.log('Token agregado:', authToken);
      return next.handle(authReq);
    }

    // Si no hay token, simplemente continuamos con la solicitud sin modificarla
    return next.handle(req);
  }
}
