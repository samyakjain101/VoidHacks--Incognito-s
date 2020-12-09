import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuizdetailComponent } from './quizdetail.component';

describe('QuizdetailComponent', () => {
  let component: QuizdetailComponent;
  let fixture: ComponentFixture<QuizdetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ QuizdetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(QuizdetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
