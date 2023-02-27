import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BasePageComponent } from './base-page/base-page.component';
import { DashboardPageComponent } from './dashboard-page/dashboard-page.component';
import { LoginComponent } from './login/login.component';
import { ProfilePageComponent } from './profile-page/profile-page.component';

const routes: Routes = [
  { path: 'login', 
    component: LoginComponent
  },
  { path: '',
    component: BasePageComponent,
    children:[
      { path: 'dashboard', 
       component: DashboardPageComponent
      },
      { path: 'profile', 
        component: ProfilePageComponent
      }
    ]
  }  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
