import { EditQuizService } from './../services/edit-quiz.service';
import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-edit-quiz',
  templateUrl: './edit-quiz.component.html',
  styleUrls: ['./edit-quiz.component.css']
})
export class EditQuizComponent implements OnInit {
  quizId: any; 
  questions: any;
  constructor(
    private route: ActivatedRoute,
    private service: EditQuizService) { }

  ngOnInit(): void {
    this.quizId = this.route.snapshot.params.quizId;
    this.service.getAll(this.quizId)
      .subscribe(questions => this.questions = questions);
  }

}