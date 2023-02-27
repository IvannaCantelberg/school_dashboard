import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  hide = true;
  loginFormControl = new FormGroup({
    userEmail: new FormControl('', [Validators.email, Validators.required]),
    userPassword: new FormControl('', [Validators.required])
  })
  

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  onSubmit (): void {
    this.router.navigate(['/dashboard'])
  }

}
