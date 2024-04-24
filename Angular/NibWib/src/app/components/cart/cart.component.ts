import { Component, OnInit } from '@angular/core';
import { CartService } from '../../service/cart.service';
import { FormsModule } from '@angular/forms'; // Убедитесь, что это импорт
import { Cart } from '../../models/cart';
import { AuthService } from '../../service/auth.service';
@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {
  cart: Cart; 
  errorMessage: string = '';
  user_id!: number;
  item_id!: number;
  constructor(private cartService: CartService, private authService: AuthService) {
    this.cart = {} as Cart;
   }

  ngOnInit(): void {
    this.getCartData();
  }

  getCartData() {
    this.authService.getUserId()
      .subscribe(
        (user_id) => {
          this.user_id = user_id;
          console.log(user_id);
          this.cartService.getCart(this.user_id) 
            .subscribe(
              (data) => {
                this.cart = data; 
                console.log(data);
              }
            );
        }
    );
  }
  

  deleteCartItem(itemId: number) {
    this.cartService.deleteCartItem(this.user_id, itemId)
      .subscribe(
        () => {
          this.getCartData();
          this.errorMessage = ''; 
        },
        (error) => {
          this.errorMessage = 'Ошибка при удалении товара из корзины: ' + error.message; 
        }
      );
  }

  updateCartItem(itemId: number, count: number) {
    this.cartService.updateCartItem(this.user_id, itemId, count)
      .subscribe(
        () => {
          this.getCartData();
          this.errorMessage = ''; 
        },
        (error) => {
          this.errorMessage = 'Ошибка при обновлении товара в корзине: ' + error.message; 
        }
      );
  }
}