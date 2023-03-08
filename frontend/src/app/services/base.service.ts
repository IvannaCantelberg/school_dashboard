import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class BaseService {

  constructor() { }
  private _hostUrl: string  ='http://localhost:8000/'
  private _apiSignUp: string = 'signup'
  private _apiLogin: string = 'login'

  public urlLogin = this._hostUrl + this._apiLogin
  public urlSignUp = this._hostUrl + this._apiSignUp
}
