import { GetAllUsersService } from './../services/get-all-users.service';
import { Component, OnInit } from '@angular/core';
import { filter, map } from 'rxjs/operators';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent implements OnInit {
  users: any;
  userIds: any;
  constructor(private service: GetAllUsersService) { }

  ngOnInit(): void {
    this.service.getAll()
      .subscribe(users => this.users = users);
  }
<<<<<<< HEAD
  
  get selectedOptions() { 
    return this.users.filter((x:any) => x.checked === true);
  }

  sendInvitation(){
    console.log(this.selectedOptions);
    
  }

=======
>>>>>>> d4d12bfd3f749253cfcbdbd659b16dc6a7781689
}
