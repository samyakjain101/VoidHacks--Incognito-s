import { GetAllUsersService } from './../services/get-all-users.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-invite-users',
  templateUrl: './invite-users.component.html',
  styleUrls: ['./invite-users.component.css']
})
export class InviteUsersComponent implements OnInit {

  users: any;
  constructor(private service: GetAllUsersService) { }

  ngOnInit(): void {
    this.service.getAll()
      .subscribe(users => this.users = users);
  }
}
