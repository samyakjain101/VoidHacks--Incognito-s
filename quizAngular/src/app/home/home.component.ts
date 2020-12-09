import { UnauthorizedAcessError } from './../common/unauthorized-access-error';
import { AppError } from './../common/app-error';
import { AuthService } from './../services/auth.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {

  constructor(
    private authService: AuthService,
    private router: Router) { }

  logout() {
    this.authService.logout()
      .subscribe(
        result => {
          
          if (result) {
            this.router.navigate(['/']);
          }
          else
            console.log('Something Went Wrong');
        },
        (error: AppError) => {
          if (error instanceof UnauthorizedAcessError) {
            this.router.navigate(['login']);
          }
          else{
            throw error;
          } 
        }
      );
  }

  isLoggedIn() {
    return this.authService.isLoggedIn()
  }

  get getCurrentUser() {
    return this.authService.currentUser();
  }
  
}
