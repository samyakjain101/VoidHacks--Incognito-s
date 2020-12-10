import { TestBed } from '@angular/core/testing';

import { CreateAnswerService } from './create-answer.service';

describe('CreateAnswerService', () => {
  let service: CreateAnswerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CreateAnswerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
