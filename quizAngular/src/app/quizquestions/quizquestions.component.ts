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
  constructor(
    private route: ActivatedRoute,
    private service: AttemptQuizService) { }

  ngOnInit(): void {
    if (true) {
      this.todo = true
    }
    this.quizId = this.route.snapshot.params.quizId;
    this.token = this.route.snapshot.params.token;
    this.service.create({
      quiz_id: this.quizId,
      todo: this.todo,
      ques_id: this.question?.id,
      choice_id: this.choiceId
    })
      .subscribe(question => this.question = question);
  }

} 
