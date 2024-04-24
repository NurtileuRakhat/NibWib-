import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IProduct } from '../models/product';

@Injectable({
  providedIn: 'root',
})
export class ProductService {
  private URL = 'http://127.0.0.1:8000/api';
  
  constructor(private http: HttpClient) {}

  getProducts(): Observable<IProduct[]> {
    return this.http.get<IProduct[]>(`${this.URL}/products/`);
  } 

  getProduct(product_id: number): Observable<IProduct> {
    return this.http.get<IProduct>(`${this.URL}/products/${product_id}`);
  }

  searchProducts(query: string): Observable<IProduct[]> {
    const params = new HttpParams().set('search', query);
    return this.http.get<IProduct[]>(`${this.URL}/products/`, { params });
  }
}
