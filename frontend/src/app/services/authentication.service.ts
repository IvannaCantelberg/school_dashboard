import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor(
    private http: HttpClient, 
    private _baseService: BaseService) { }

  
  signup(data: {}) {
    return this.http.post(this._baseService.urlSignUp, data)
  }
  
  login(data: {}){
    return this.http.post(this._baseService.urlLogin, data)
  }
}
