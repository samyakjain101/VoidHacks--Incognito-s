import { BadRequest } from './../common/bad-request';
import { AppError } from './../common/app-error';
import { Router } from '@angular/router';
import { RegisterService } from './../services/register.service';
import { PasswordValidators } from './password.validators';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  form: FormGroup;
  registrationError: boolean = false;
  uniqueUsername: boolean = true;
  validEmail: boolean = true;
  
  constructor(fb: FormBuilder, 
    private registerService: RegisterService,
    private router: Router) {
    this.form = fb.group({
      username: ['', Validators.required],
      firstName: ['', Validators.required],
      lastName: ['', Validators.required],
      email: ['', Validators.required],
      password: ['', Validators.required],
      confirmPassword: ['', Validators.required],
    }, {
      validator: PasswordValidators.passwordShouldMatch
    })
  }

  get username() { return this.form.get('username'); }
  get firstName() { return this.form.get('firstName'); }
  get lastName() { return this.form.get('lastName'); }
  get email() { return this.form.get('email'); }
  get password() { return this.form.get('password'); }
  get confirmPassword() { return this.form.get('confirmPassword'); }

  register() {
    if (this.form.valid) {
      this.registerService.register(this.form.value)
        .subscribe(result => {
          if (result) {
            this.router.navigate(['login']);
          }
          else
            console.log('else hit');
            
        },
          (error: AppError) => {
            if (error instanceof BadRequest) {
              if (error.originalError.error.username) {
                this.registrationError = true;
                this.uniqueUsername = false;
              }
              else if (error.originalError.error.email) {
                this.registrationError = true;
                this.validEmail = false;
              }
            }
            else {
              throw error;
            }
          });
    }

  }
}
