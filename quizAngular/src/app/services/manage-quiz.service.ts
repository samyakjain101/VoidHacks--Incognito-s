import { HttpClient } from '@angular/common/http';
import { DataService } from './data.service';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ManageQuizService extends DataService{

  create_quiz_url = 'http://192.168.225.24:8000/api/manage-quiz/'
  // private create_quiz_url = 'http://127.0.0.1:8000/api/manage-quiz'

  constructor(http: HttpClient) {
    super('http://192.168.225.24:8000/api/manage-quiz/', http);
  }

}
