import { BadRequest } from './../common/bad-request';
import { AppError } from './../common/app-error';
import { CreateQuizService } from './../services/create-quiz.service';
import { DataService } from './../services/data.service';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'create-quiz',
  templateUrl: './create-quiz.component.html',
  styleUrls: ['./create-quiz.component.css']
})
export class CreateQuizComponent {
  form: FormGroup;
  
  constructor(fb: FormBuilder,
    private createQuizService: CreateQuizService,
    private router: Router) {
    this.form = fb.group({
      title: ['', Validators.required],
      startDate: ['', Validators.required],
      endDate: ['', Validators.required],
      duration: ['', Validators.required],
    })
  }

  get title() { return this.form.get('title'); }
  get startDate() { return this.form.get('startDate'); }
  get endDate() { return this.form.get('endDate'); }
  get duration() { return this.form.get('duration'); }

  createQuiz() {
    console.log(this.form.value);
    if (this.form.valid) {
      this.createQuizService.create(this.form.value)
        .subscribe(result => {
          if (result) {
            // this.router.navigate(['login']);
            console.log('success');
          }
          else
            console.log('else hit');

        },
          (error: AppError) => {
            if (error instanceof BadRequest) {
              alert("Bad Request")
            }
            else {
              throw error;
            }
          });
    }
  }

}
