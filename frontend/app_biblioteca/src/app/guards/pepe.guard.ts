import { CanActivateFn } from '@angular/router';

export const pepeGuard: CanActivateFn = (route, state) => {
  return true;
};
