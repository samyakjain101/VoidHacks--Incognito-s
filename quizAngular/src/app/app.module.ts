import { CreateQuizService } from './services/create-quiz.service';
import { DataService } from './services/data.service';
import { AppErrorHandler } from './common/app-error-handler';
import { AdminAuthGuard } from './services/admin-auth-guard.service';
import { AuthGuard } from './services/auth-guard.service';
import { RouterModule } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule, ErrorHandler } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { HomeComponent } from './home/home.component';
import { AdminComponent } from './admin/admin.component';
import { NoAccessComponent } from './no-access/no-access.component';
import { RegisterComponent } from './register/register.component';
import { CreateQuizComponent } from './create-quiz/create-quiz.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    AdminComponent,
    NoAccessComponent,
    RegisterComponent,
    CreateQuizComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      {
        path: '',
        component: HomeComponent
      },
      {
        path: 'login',
        component: LoginComponent
      },
      {
        path: 'register',
        component: RegisterComponent
      },
      {
        path: 'no-access',
        component: NoAccessComponent
      },
      {
        path: 'admin',
        component: AdminComponent,
        canActivate: [AuthGuard, AdminAuthGuard]
      },
      {
        path: 'create-quiz',
        component: CreateQuizComponent,
        canActivate: [AuthGuard, AdminAuthGuard]
      },
    ])
  ],
  providers: [
    CreateQuizService,
    AuthGuard,
    AdminAuthGuard,
    { provide: ErrorHandler, useClass: AppErrorHandler }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
