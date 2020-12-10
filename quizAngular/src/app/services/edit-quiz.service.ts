import { AppError } from './../common/app-error';
import { NotFoundError } from './../common/not-found-error';
import { BadInput } from './../common/bad-input';
import { catchError } from 'rxjs/operators';
import { DataService } from './data.service';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EditQuizService{

  create_quiz_url = 'http://192.168.225.24:8000/api/edit-quiz/'
  // private create_quiz_url = 'http://127.0.0.1:8000/api/edit-quiz'

  constructor(private http: HttpClient) {
  }

  private getHeader(quiz_id:any) {
    let customHeaders = { Authorization: "Token " + localStorage.getItem("token") };
    let params = { quiz_id: quiz_id };
    return { headers: customHeaders, params: params };
  }

  getAll(quiz_id:any) {
    return this.http.get(this.create_quiz_url, this.getHeader(quiz_id))
      .pipe(catchError(this.handleError));
  }
  private handleError(error: Response) {
    if (error.status === 400)
      return throwError(new BadInput(error));
    if (error.status === 404)
      return throwError(new NotFoundError());
    return throwError(new AppError(error));
  }
}
