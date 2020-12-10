import { GetAllUsersService } from './../services/get-all-users.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent implements OnInit {
  users: any;
  constructor(private service: GetAllUsersService) { }

  ngOnInit(): void {
    this.service.getAll()
      .subscribe(users => this.users = users);
  }
}
