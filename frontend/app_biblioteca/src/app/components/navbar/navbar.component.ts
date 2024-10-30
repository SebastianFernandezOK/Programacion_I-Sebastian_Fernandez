import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service'

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {
  ver = true;
  isDropdownOpen = false;

  constructor(private authService: AuthService) {}

  get isToken() {
    return localStorage.getItem("token");
  }

  cerrarSesion() {
    this.authService.logout();
  }

  toggleDropdown() {
    this.isDropdownOpen = !this.isDropdownOpen;
  }
}

