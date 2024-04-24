import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthToken } from '../models/authToken';
import { ICategory } from '../models/category';
import { IProduct } from '../models/product';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class CategoryService {
    URL = 'http://127.0.0.1:8000/api';
    constructor(private http: HttpClient) {}
    private selectedCategorySubject = new BehaviorSubject<ICategory | null>(null);
    selectedCategory$ = this.selectedCategorySubject.asObservable();
  
    login(username: string, password: string): Observable<AuthToken> {
        return this.http.post<AuthToken>(`${this.URL}/login/`, {
        username,
        password,
        });
    }

    getCategories(): Observable<ICategory[]> {
        return this.http.get<ICategory[]>(`${this.URL}/categories/`);
    }

    getCategory(category_id: number): Observable<ICategory>{
        return this.http.get<ICategory>(`${this.URL}/categories/${category_id}`);
    }

    getCategoryProducts(category_id: number): Observable<IProduct[]> {
        return this.http.get<IProduct[]>(`${this.URL}/categories/${category_id}/products`)
    }

    toggleCategory(category: ICategory) {
        this.selectedCategorySubject.next(category);
      }
}