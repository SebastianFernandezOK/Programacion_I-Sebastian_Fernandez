import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './page/home/home.component';
import { ErrorPageComponent } from './page/error-page/error-page.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { FooterComponent } from './components/footer/footer.component';
import { LoginComponent } from './page/login/login.component';
import { NotificationsComponent } from './page/notifications/notifications.component';
import { ProfileComponent } from './page/profile/profile.component';
import { RegisterComponent } from './page/register/register.component';
import { UsersComponent } from './page/users/users.component';
import { LibrarianRentsComponent } from './page/librarian-rents/librarian-rents.component';
import { ConfigurationComponent } from './page/configuration/configuration.component';
import { ForgotPasswordComponent } from './page/forgot-password/forgot-password.component';
import { HeaderComponent } from './components/header/header.component';
import { SeeUserComponent } from './components/users/see-user/see-user.component';
import { SeeRentsComponent } from './components/rents/see-rents/see-rents.component';
import { HttpClientModule } from '@angular/common/http';
import { BookComponent } from './components/book/book.component';
import { PaginateComponent } from './components/paginate/paginate.component';
import { NgClass } from '@angular/common';
import { BookDetailsComponent } from './page/book-details/book-details.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ErrorPageComponent,
    NavbarComponent,
    FooterComponent,
    LoginComponent,
    NotificationsComponent,
    ProfileComponent,
    RegisterComponent,
    UsersComponent,
    LibrarianRentsComponent,
    ConfigurationComponent,
    ForgotPasswordComponent,
    HeaderComponent,
    SeeUserComponent,
    SeeRentsComponent,
    PaginateComponent,
    BookComponent,
    BookDetailsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule,
    NgClass,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

