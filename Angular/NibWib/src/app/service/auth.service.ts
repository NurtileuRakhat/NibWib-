import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { AuthToken, Register } from '../models/authToken';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

    private BASE_URL = "http://localhost:8000/user";

    constructor(private httpClient: HttpClient) { }

    getUserId(): Observable<number> {
      return this.httpClient.get<any>(`${this.BASE_URL}/get_id/`).pipe(
        map(response => response.user_id)
      );
    }

    login(username: string, password: string): Observable<AuthToken> {
        return this.httpClient.post<AuthToken>(`${this.BASE_URL}/token/`, { username, password })
        .pipe(
            catchError(error => throwError(() => error))
        );
    }

    register(username: string, password: string, password2: string, email: string, first_name: string, last_name: string): Observable<Register> {
      return this.httpClient.post<Register>(`${this.BASE_URL}/register/`, { username, password, password2, email, first_name, last_name })
      .pipe(
          catchError(error => throwError(() => error))
      );
  }
  
    updateUser(userData: any): Observable<any> {
        return this.httpClient.put<any>(`${this.BASE_URL}/profile/update/`, userData);
      }
    
      getUserProfile(): Observable<any> {
        return this.httpClient.get<any>(`${this.BASE_URL}/profile/`);
      }

    isLoggedIn(): boolean {
        const token = localStorage.getItem('token');
        return !!token;
    }

    logout(): void {
        localStorage.removeItem('token');
        localStorage.removeItem('userData');
    }
}
