import { BadRequest } from './../common/bad-request';
import { UnauthorizedAcessError } from './../common/unauthorized-access-error';
import { AppError } from './../common/app-error';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private login_url = 'http://127.0.0.1:8000/api/login/'
  private logout_url = 'http://127.0.0.1:8000/api/logout/'
  // private login_url = 'http://192.168.225.24:8000/api/login/'
  // private logout_url = 'http://192.168.225.24:8000/api/logout/'

  constructor(private http: HttpClient) { }

  private getHeader() {
    let customHeaders = { Authorization: "Token " + localStorage.getItem("token") };
    return { headers: customHeaders };
  }

  login(credentials: any) {
    return this.http.post(this.login_url, credentials)
      .pipe(
        catchError(this.handleError),
        map(response => {
          let result: any = response;
          
          if (result && result.token) {
            localStorage.setItem('token', result.token);
            localStorage.setItem('expiry', result.expiry);
            localStorage.setItem('user', JSON.stringify(result.user));
            return true;
          }
          return false
        })
      )
  }
  
  logout() {
    return this.http.post(this.logout_url,{},this.getHeader())
      .pipe(
        catchError(this.handleError),
        map(response => {
          if (response === null) {
            localStorage.removeItem('token')
            localStorage.removeItem('expiry')
            localStorage.removeItem('user')
            return true;
          }
          return false
        }
        )
      );
  }

  isLoggedIn() {
    let expiry = localStorage.getItem('expiry');
    if (!expiry) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      return false
    }
    let expiryDate = new Date(expiry);
    let currentDate = new Date();
    if (expiryDate > currentDate && localStorage.getItem('token')) {
      return true
    }
    return false
  }

  currentUser() {
    let user = localStorage.getItem('user');
    if (!user) return null;
    return JSON.parse(user)
  }

  private handleError(error: Response) {
    if (error.status === 401) {
      return throwError(new UnauthorizedAcessError(error));
    }
    if (error.status === 400) {
      return throwError(new BadRequest(error));
    }
    return throwError(new AppError(error));
  }
}