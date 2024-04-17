import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IProduct } from '../models/product';

@Injectable({
  providedIn: 'root',
})
export class ProductService {
  private URL = 'http://127.0.0.1:8000/api';
  constructor(private http: HttpClient) {}

  getProduct(product_id: number): Observable<IProduct> {
    return this.http.get<IProduct>(`${this.URL}/categories/products/${product_id}/`);
  }

  getProducts(): Observable<IProduct[]> {
    return this.http.get<IProduct[]>(`${this.URL}/categories/products/`);
  }
}