import { AppError } from './../common/app-error';
import { BadRequest } from './../common/bad-request';
import { AuthService } from '../services/auth.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent { 
  invalidLogin: boolean = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private authService: AuthService) { }

  login(credentials: HTMLInputElement) {
    
    this.authService.login(credentials)
      .subscribe(result => {
        if (result) {
          let returnUrl = this.route.snapshot.queryParamMap.get('returnUrl');
          this.router.navigate([returnUrl || '/']);
        }
        else
          this.invalidLogin = true;
      },
        (error: AppError) => {
          
          if (error instanceof BadRequest) {
            this.invalidLogin = true;
          }
          else {
            throw error;
          }
        });
  }

}
