import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './page/home/home.component';
import { ErrorPageComponent } from './page/error-page/error-page.component';
import { ConfigurationComponent } from './page/configuration/configuration.component';
import { ForgotPasswordComponent } from './page/forgot-password/forgot-password.component';
import { LibrarianRentsComponent } from './page/librarian-rents/librarian-rents.component';
import { LoginComponent } from './page/login/login.component';
import { NotificationsComponent } from './page/notifications/notifications.component';
import { ProfileComponent } from './page/profile/profile.component';
import { RegisterComponent } from './page/register/register.component';
import { RentsComponent } from './page/rents/rents.component';
import { UsersComponent } from './page/users/users.component';

const routes: Routes = [
  {path: 'configuration', component: ConfigurationComponent},
  {path: 'error_page', component: ErrorPageComponent},
  {path: 'forgot-password', component: ForgotPasswordComponent},
  {path: 'home', component: HomeComponent},
  {path: 'librarian-rents', component: LibrarianRentsComponent},
  {path: 'login', component: LoginComponent},
  {path: 'notifications', component: NotificationsComponent},
  {path: 'profile', component: ProfileComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'rents', component: RentsComponent},
  {path: 'users', component: UsersComponent},


  {path: '', redirectTo: 'home', pathMatch:'full'},
  {path: '**', redirectTo: 'error_page'}  

];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
