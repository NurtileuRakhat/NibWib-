import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../service/auth.service';
@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  userProfile: any;
  updatedUserProfile: any = {};
  isLogged!: boolean;

  constructor(private userService: AuthService) { }

  ngOnInit(): void {
    this.getUserProfile();
  }

  getUserProfile(): void {
    this.userService.getUserProfile().subscribe(
      (data) => {
        this.userProfile = data;
        this.updatedUserProfile = { ...this.userProfile };
      },
      (error) => {
        console.log('Error fetching user profile:', error);
      }
    );
  }

  updateUserProfile(): void {
    alert("in the development")
  }

  logout() {
    this.isLogged = false;
    localStorage.removeItem('token');
  }

}
