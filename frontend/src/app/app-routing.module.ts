import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BasePageComponent } from './base-page/base-page.component';
import { DashboardPageComponent } from './dashboard-page/dashboard-page.component';
import { LoginComponent } from './login/login.component';
import { ProfilePageComponent } from './profile-page/profile-page.component';
import { RegisterComponent } from './register/register.component';

const routes: Routes = [
  { path: 'login', 
    component: LoginComponent
  },
  { path: 'register', 
    component: RegisterComponent
  },
  { path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full',
  },
  { path: '',
    component: BasePageComponent,
    children: [
      { path: 'dashboard', 
        component: DashboardPageComponent,
      },
      { path: 'profile', 
        component: ProfilePageComponent
      },
    ]
  },   
  { path: '**',
    redirectTo: 'dashboard'
  } 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
