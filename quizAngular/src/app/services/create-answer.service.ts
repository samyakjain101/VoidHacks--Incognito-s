import { DataService } from './data.service';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CreateAnswerService extends DataService{

  create_answer_url = 'http://192.168.225.24:8000/api/add-question/'
  // private create_answer_url = 'http://127.0.0.1:8000/api/add-question'

  constructor(http: HttpClient) {
    super('http://192.168.225.24:8000/api/add-question/', http);
  }

}