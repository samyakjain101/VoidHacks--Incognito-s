import { BadRequest } from './../common/bad-request';
import { AppError } from './../common/app-error';
import { CreateAnswerService } from './../services/create-answer.service';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-create-answer',
  templateUrl: './create-answer.component.html',
  styleUrls: ['./create-answer.component.css']
})
export class CreateAnswerComponent implements OnInit{
  form: FormGroup;
  quizId:any;
  quizName:any;

  constructor(fb: FormBuilder,
    private CreateAnswerService: CreateAnswerService,
    private router: Router,
    private route: ActivatedRoute) {
    this.form = fb.group({
      question: ['', Validators.required],
    
      choice1: ['', Validators.required],
      choice2: ['', Validators.required],
      choice3: ['', Validators.required],
      choice4: ['', Validators.required],

      choice: ['', Validators.required],
      quiz_id: ['',]
    })
  }
  ngOnInit(): void {
    this.quizId = this.route.snapshot.params.quizId;
    this.quizName = this.route.snapshot.params.name;
  }


  get question() { return this.form.get('question'); }
  get choice1() { return this.form.get('choice1'); }
  get choice2() { return this.form.get('choice2'); }
  get choice3() { return this.form.get('choice3'); }
  get choice4() { return this.form.get('choice4'); }

  addQuestion() {
    this.form.value.quiz_id=this.quizId;
    
    if (this.form.valid) {
      this.CreateAnswerService.create(this.form.value)
        .subscribe(result => {
          if (result) {
            this.router.navigate(['add-question',this.quizId, this.quizName]);
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
