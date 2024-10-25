import { TestBed } from '@angular/core/testing';
import { CanActivateFn } from '@angular/router';

import { pepeGuard } from './pepe.guard';

describe('pepeGuard', () => {
  const executeGuard: CanActivateFn = (...guardParameters) => 
      TestBed.runInInjectionContext(() => pepeGuard(...guardParameters));

  beforeEach(() => {
    TestBed.configureTestingModule({});
  });

  it('should be created', () => {
    expect(executeGuard).toBeTruthy();
  });
});
