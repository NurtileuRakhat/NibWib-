import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthToken } from '../models/authToken';
import { ICategory } from '../models/category';

@Injectable({
  providedIn: 'root',
})
export class CategoryService {
    URL = 'http://127.0.0.1:8000/api';
    constructor(private http: HttpClient) {}

    login(username: string, password: string): Observable<AuthToken> {
        return this.http.post<AuthToken>(`${this.URL}/login/`, {
        username,
        password,
        });
    }

    getCategories(): Observable<ICategory[]> {
        return this.http.get<ICategory[]>(`${this.URL}/categories`);
    }

    getCategory(category_id: number): Observable<ICategory[]>{
        return this.http.get<ICategory[]>(`${this.URL}/categories/${category_id}`);
    }

}