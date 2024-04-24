// favorite.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Favorite, FavoriteItem } from '../models/favorite';

@Injectable({
  providedIn: 'root'
})
export class FavoriteService {
  private apiUrl = 'http://127.0.0.1:8000/favorite/'; 

  constructor(private http: HttpClient) { }

  addToFavorites(id: number, productId: number): Observable<FavoriteItem> {
    return this.http.post<FavoriteItem>(`${this.apiUrl}${id}/add_to_favorites/`, { product: productId });
  }

  removeFromFavorites(id: number, itemId: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}${id}/remove_from_favorites/${itemId}/`);
  }

  getFavorites(id: number): Observable<Favorite> {
    return this.http.get<Favorite>(`${this.apiUrl}${id}/`);
  }

  clearFavorites(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}${id}/`);
  }
}
