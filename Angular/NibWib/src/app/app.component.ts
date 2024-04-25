import { Component, OnInit } from '@angular/core';
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
  password2: string = '';
  email!: string;
  first_name!: string;
  last_name!: string;
  isRegister!: boolean;
  constructor(
    private authService: AuthService,
  ) {}

  ngOnInit(): void {
    this.isLogged = this.authService.isLoggedIn();
  }

  login(): void {
    this.authService.login(this.username, this.password).subscribe({
      next: (data) => {
        localStorage.setItem('token', data.access);
        this.isLogged = true;
      },
      error: (error) => {
        alert('Login Failed.Invalid username or password.');
      }
    });
  }

  register(): void {
    this.authService.register(
      this.username,
      this.password,
      this.password2,
      this.email,
      this.first_name,
      this.last_name
    ).subscribe({
      next: () => {
        this.isLogged = true;
        this.isRegister = false;
      },
      error: (error) => {
        console.log(error)
        alert('Registration Failed. Please check your inputs and try again.');
      }
    });
  }

  logout() {
    this.isLogged = false;
    localStorage.removeItem('token');
  }

}