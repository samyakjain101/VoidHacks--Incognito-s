import { CreateQuizComponent } from './create-quiz/create-quiz.component';
import { CreateQuizService } from './services/create-quiz.service';
import { AppErrorHandler } from './common/app-error-handler';
import { AdminAuthGuard } from './services/admin-auth-guard.service';
import { AuthGuard } from './services/auth-guard.service';
import { RouterModule } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule, ErrorHandler } from '@angular/core';
import { CountdownModule } from 'ngx-countdown';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { HomeComponent } from './home/home.component';
import { AdminComponent } from './admin/admin.component';
import { NoAccessComponent } from './no-access/no-access.component';
import { RegisterComponent } from './register/register.component';
import { QuizdetailComponent } from './quizdetail/quizdetail.component';
import { QuizquestionsComponent } from './quizquestions/quizquestions.component';
import { CreateAnswerComponent } from './create-answer/create-answer.component';
import { ManageQuizComponent } from './manage-quiz/manage-quiz.component';
import { EditQuizComponent } from './edit-quiz/edit-quiz.component';
import { InviteUsersComponent } from './invite-users/invite-users.component';
import { ResultComponent } from './result/result.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    AdminComponent,
    NoAccessComponent,
    RegisterComponent,
    QuizdetailComponent,
    QuizquestionsComponent,
    CreateQuizComponent,
    CreateAnswerComponent,
    ManageQuizComponent,
    EditQuizComponent,
    InviteUsersComponent,
    ResultComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    CountdownModule,
    RouterModule.forRoot([
      {
        path: 'login',
        component: LoginComponent
      },
      {
        path: 'register',
        component: RegisterComponent
      },
      {
        path: 'quiz-details',
        component: QuizdetailComponent
      },
      {
        path: 'attempt-quiz',
        component: QuizquestionsComponent
      },
      {
        path: 'no-access',
        component: NoAccessComponent
      },
      {
        path: 'invite-users',
        component: InviteUsersComponent,
        canActivate: [AuthGuard, AdminAuthGuard]
      },
      {
        path: 'result',
        component: ResultComponent,
        canActivate: [AuthGuard, AdminAuthGuard]
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
      {
        path: 'manage-quiz',
        component: ManageQuizComponent,
        canActivate: [AuthGuard, AdminAuthGuard]
      },
      {
        path: 'create-answer',
        component: CreateAnswerComponent,
        canActivate: [AuthGuard, AdminAuthGuard]
      },
      {
        path: 'edit-quiz/:quizId/:name',
        component: EditQuizComponent,
        canActivate: [AuthGuard, AdminAuthGuard]
      },
      {
        path: 'add-question/:quizId/:name',
        component: CreateAnswerComponent,
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
