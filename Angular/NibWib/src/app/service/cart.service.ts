

    import { Injectable } from '@angular/core';
    import { HttpClient } from '@angular/common/http';
    import { Observable } from 'rxjs';
    import { catchError } from 'rxjs/operators';
    import { Cart,CartItem } from '../models/cart';
    import { IProduct } from '../models/product';
    @Injectable({
      providedIn: 'root'
    })
    export class CartService {
      private baseUrl = 'http://127.0.0.1:8000/cart/'; 

      constructor(private http: HttpClient) { }
    
      getCart(cartId: number): Observable<any> {
        return this.http.get<Cart>(`${this.baseUrl}${cartId}/`);
      }
    
      addToCart(cartId: number, product: IProduct): Observable<CartItem> {
        const url = `${this.baseUrl}${cartId}/cart_item/`;
        const data = {
          product: product.id, 
          count: 1,
          cart: cartId
        };
        return this.http.post<CartItem>(url, data);
      }
      
      
      updateCartItem(cartId: number, itemId: number, newCount: number): Observable<any> {
        const url = `${this.baseUrl}${cartId}/cart_item/${itemId}/`;
        const data = { count: newCount };
        return this.http.put(url, data)
          .pipe(
            catchError((error) => {
              throw error; 
            })
          );
      }
      
      deleteCartItem(cartId: number, itemId: number): Observable<any> {
        return this.http.delete<CartItem>(`${this.baseUrl}${cartId}/cart_item/${itemId}/`);
      }
    
      clearCart(cartId: number): Observable<any> {
        return this.http.delete<Cart>(`${this.baseUrl}${cartId}/`);
      }

    }
    