// favorites.component.ts

import { Component, OnInit } from '@angular/core';
import { FavoriteService } from '../../service/favorite.service';
import { Favorite } from '../../models/favorite';
import { AuthService } from '../../service/auth.service';

@Component({
  selector: 'app-favorites',
  templateUrl: './favorites.component.html',
  styleUrls: ['./favorites.component.css']
})
export class FavoritesComponent implements OnInit {
  favorite!: Favorite;
  errorMessage: string = '';
  user_id!: number;
  item_id!: number;
  
  constructor(private favoriteService: FavoriteService,private authService: AuthService) { }

  ngOnInit(): void {
    this.getFavorites();
  }

  getFavorites(): void {
    this.authService.getUserId()
    .subscribe(
      (user_id) => {
        this.user_id = user_id;
        console.log(user_id);
        this.favoriteService.getFavorites(this.user_id)
        .subscribe(
          (data) => {
            this.favorite = data; 
            console.log(data);
          }
        );
      }
    );
  }

  removeFromFavorites(itemId: number): void {
    this.favoriteService.removeFromFavorites(this.user_id, itemId).subscribe(
      response => {
        console.log('Removed from favorites:', response);
        this.getFavorites();
      },
      error => {
        console.error('Error removing from favorites:', error);
      }
    );
  }
}
