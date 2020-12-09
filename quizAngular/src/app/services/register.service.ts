import { UnauthorizedAcessError } from './../common/unauthorized-access-error';
import { BadRequest } from './../common/bad-request';
import { AppError } from './../common/app-error';
import { catchError, map } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RegisterService {

  private register_url = 'http://192.168.225.24:8000/api/register/'

  constructor(private http: HttpClient) { }

  register(credentials: any) {
    return this.http.post(this.register_url, credentials)
      .pipe(
        catchError(this.handleError),
        map(response => {
          let result: any = response;
          console.log(response);

          if (result.success) {
            return true;
          }
          return false
        })
      )
  }

  private handleError(error: any) {
    console.log(error);
    
    if (error.status === 401) {
      return throwError(new UnauthorizedAcessError(error));
    }
    if (error.status === 400) {
      return throwError(new BadRequest(error));
    }
    return throwError(new AppError(error));
  }
}
 