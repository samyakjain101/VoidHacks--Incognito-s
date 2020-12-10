import { BadRequest } from './../common/bad-request';
import { AppError } from './../common/app-error';
import { CreateAnswerService } from './../services/create-answer.service';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-create-answer',
  templateUrl: './create-answer.component.html',
  styleUrls: ['./create-answer.component.css']
})
export class CreateAnswerComponent {
  form: FormGroup;

  constructor(fb: FormBuilder,
    private CreateAnswerService: CreateAnswerService,
    private router: Router) {
    this.form = fb.group({
      question: ['', Validators.required],
      
      choice1bool: ['',],
      choice1: ['', Validators.required],

      choice2bool: ['',],
      choice2: ['', Validators.required],

      choice3bool: ['',],
      choice3: ['', Validators.required],

      choice4bool: ['',],
      choice4: ['', Validators.required],
    })
  }

  get question() { return this.form.get('question'); }

  get choice1bool() { return this.form.get('choice1bool'); }
  get choice1() { return this.form.get('choice1'); }

  get choice2bool() { return this.form.get('choice2bool'); }
  get choice2() { return this.form.get('choice2'); }

  get choice3bool() { return this.form.get('choice3bool'); }
  get choice3() { return this.form.get('choice3'); }

  get choice4bool() { return this.form.get('choice4bool'); }
  get choice4() { return this.form.get('choice4'); }

  addQuestion() {
    if (this.form.valid) {
      console.log(this.form.value);
      this.CreateAnswerService.create(this.form.value)
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
