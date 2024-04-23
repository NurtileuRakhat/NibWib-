import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class CartService {
  private apiUrl = 'http://localhost:8000/cart/';

  constructor(private http: HttpClient) { }
 
}