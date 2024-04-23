import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthToken, SignUpToken } from '../models/authToken';
@Injectable({
  providedIn: 'root'
})
export class AuthService {

  BASE_URL = "http://localhost:8000/user"

  constructor(private client: HttpClient) { }

  login(username: string, password: string): Observable<AuthToken> {
    return this.client.post<AuthToken>(`${this.BASE_URL}/token/`, { username, password });
  }

  register(username: string,password: string, password2: string, email: string, first_name: string, last_name: string): Observable<SignUpToken> {
    return this.client.post<SignUpToken>(`${this.BASE_URL}/register/`, { username, password, password2 , email, first_name, last_name });
  }

  isLoggedIn(): boolean {
    const token = localStorage.getItem('token');
    return !!token;
  }
}