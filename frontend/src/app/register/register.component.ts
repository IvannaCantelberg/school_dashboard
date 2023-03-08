import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { catchError, of, Subscription } from 'rxjs';
import { AuthenticationService } from '../services/authentication.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit, OnDestroy {

  constructor(private router: Router,
              private _authSerivice: AuthenticationService) { }

  private subscription!: Subscription;

  visible: boolean = false;
  registerFormControl = new FormGroup({
    userName: new FormControl('', [Validators.required]),
    userEmail: new FormControl('', [Validators.email, Validators.required]),
    userPassword: new FormControl('', [Validators.required])
  })
  errorMsg: string = '';

  ngOnInit(): void {
  }
  get userName() { return this.registerFormControl.get('userName'); }


  onSubmit(): void {
    let formData = {'email': this.registerFormControl.controls['userEmail'].value,
                    'password': this.registerFormControl.controls['userPassword'].value,
                    'username': this.registerFormControl.controls['userName'].value
                  };

    this.subscription = this._authSerivice.signup(formData)
                                .pipe(
                                  catchError(error => {
                                    if (error.error) {
                                        this.errorMsg = error.error.detail.email;
                                        this.validateRegisterationForm(this.errorMsg);
                                    } 
                                    return of({});
                                }))
                                .subscribe((resp) => {
                                  console.log(resp);
                                }) 
    // this.router.navigate(['/dashboard'])
  }

  private validateRegisterationForm(message: string){
    this.registerFormControl.controls['userEmail'].setErrors({valid: false})
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe()
  }
}
