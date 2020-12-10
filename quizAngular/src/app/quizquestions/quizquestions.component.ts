import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { AttemptQuizService } from './../services/attempt-quiz.service';
import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-quizquestions',
  templateUrl: './quizquestions.component.html',
  styleUrls: ['./quizquestions.component.css']
})
export class QuizquestionsComponent implements OnInit {
  quizId: any;
  token: any;
  question: any;
  choiceId: any;
  todo: any = false;
  timeLeft: any;
  form: FormGroup;

  constructor(fb: FormBuilder,
    private route: ActivatedRoute,
    private service: AttemptQuizService) {
    this.form = fb.group({
      ques_id: ['',],
      choice_id: ['', Validators.required],
      quiz_id: ['',],
      todo: ['',]
    })
    }

  ngOnInit(): void {
    this.quizId = this.route.snapshot.params.quiz_id;
    this.token = this.route.snapshot.params.token;
    this.service.create({
      quiz_id: this.quizId,
      todo: this.todo,
      ques_id: this.question?.id,
      choice_id: this.choiceId
    })
      .subscribe(question => {
        this.question = question;
        this.timeLeft = this.question[0].timeLeftInSec;
        
      });
      
    }
    nextQuestion() {
      if(this.form.valid) {
        if (this.form.value.choice_id) {
          
          this.form.value.todo = true
          this.form.value.ques_id = this.question[1].ques_id
          this.form.value.quiz_id = this.quizId
        }
        this.service.create(this.form.value)
          .subscribe(question => {
            this.question = question;
            this.timeLeft = this.question[0].timeLeftInSec;
          });
      }
    }
} 
