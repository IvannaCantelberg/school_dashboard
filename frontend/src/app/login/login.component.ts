import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { catchError, Observable, of, Subscriber, Subscription } from 'rxjs';
import { AuthenticationService } from '../services/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit, OnDestroy{
  constructor(
    private router: Router,
    private _authSerivice: AuthenticationService) { }

  hide = true;
  loginFormControl = new FormGroup({
    userEmail: new FormControl('', [Validators.email, Validators.required]),
    userPassword: new FormControl('', [Validators.required])
  })

  private subscription!: Subscription;
  errorMsg: string = ''

  ngOnInit(): void {
  }

  onSubmit(): void {
    let formData = {'username': this.loginFormControl.controls['userEmail'].value,
                    'password': this.loginFormControl.controls['userPassword'].value}
    this.subscription = this._authSerivice.login(formData)
                        .pipe(
                          catchError(error => {
                            if (error instanceof ErrorEvent) {
                                this.errorMsg = error.message;
                            } 
                            return of([]);
                        })
                        )
                        .subscribe((resp) => {
                          console.log(resp);
                        })

    // this.router.navigate(['/dashboard']);
  }

  ngOnDestroy(){
    this.subscription.unsubscribe();
  }

}
