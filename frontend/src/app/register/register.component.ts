import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  constructor(private router: Router) { }
  visible: boolean = false;
  registerFormControl = new FormGroup({
    userName: new FormControl('', [Validators.required]),
    userSurname: new FormControl('', [Validators.required]),
    userEmail: new FormControl('', [Validators.email, Validators.required]),
    userPassword: new FormControl('', [Validators.required])
  })

  ngOnInit(): void {
  }

  onSubmit(): void {
    this.router.navigate(['/dashboard'])
  }
}
