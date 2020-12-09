import { ManageQuizService } from './../services/manage-quiz.service';
import { CreateQuizService } from './../services/create-quiz.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-manage-quiz',
  templateUrl: './manage-quiz.component.html',
  styleUrls: ['./manage-quiz.component.css']
})
export class ManageQuizComponent {
  quizzes: any;

  constructor(private service: ManageQuizService) { }
  ngOnInit(): void {
    this.service.getAll()
      .subscribe(quizzes => this.quizzes = quizzes);
  }

}
