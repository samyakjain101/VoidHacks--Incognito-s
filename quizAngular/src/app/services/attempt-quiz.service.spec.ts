import { TestBed } from '@angular/core/testing';

import { AttemptQuizService } from './attempt-quiz.service';

describe('AttemptQuizService', () => {
  let service: AttemptQuizService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AttemptQuizService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
