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
      start_date: ['', Validators.required],
      end_date: ['', Validators.required],
      duration: ['', Validators.required],
    })
  }

  get title() { return this.form.get('title'); }
  get start_date() { return this.form.get('start_date'); }
  get end_date() { return this.form.get('end_date'); }
  get duration() { return this.form.get('duration'); }

  createQuiz() {
    if (this.form.valid) {
      let totalMinutes: any = this.form.value.duration
      let hours = String(Math.floor(totalMinutes / 60))
      let minutes = String(totalMinutes % 60)
      console.log(hours);
      console.log(minutes);
      
      this.form.value.duration = "0 " + hours + ':' + minutes + ':00';
      console.log(this.form.value);
      
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
