import { Component, OnInit } from '@angular/core';
import { CategoryService } from './service/category.service';
import { AuthService } from './service/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  title = 'NibWib';
  isLogged!: boolean;
  username!: string;
  password!: string;
  password2: string = ''
  email!: string;
  first_name!:string;
  last_name!:string;
  isRegister!: Boolean;
  constructor(private authService: AuthService) {}
  
  ngOnInit(): void {
    this.isLogged = this.authService.isLoggedIn();
  }

  login(): void {
    this.authService.login(this.username, this.password).subscribe((data) => {      
      localStorage.setItem('token', data.access);
      localStorage.setItem('username', this.username);
      this.isLogged = true;
    })
  }

  register(): void {
    this.authService.register(this.username, this.password, this.password2, this.email, this.first_name, this.last_name).subscribe(() => {  
      this.isLogged = true;
      this.isRegister = false;
    });
  }
  
  logout() {
    this.isLogged = false;
    localStorage.removeItem('token');
  }

}