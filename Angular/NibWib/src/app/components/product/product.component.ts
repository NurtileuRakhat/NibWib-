import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { IProduct } from '../../models/product';
import { ProductService } from '../../service/product.service';
import { RouterModule } from '@angular/router';
import { CartService } from '../../service/cart.service';
import { AuthService } from '../../service/auth.service';
@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {
  productId: number = 0;
  product: IProduct;
  user_id!: number;
  errorMessage: string = '';

  constructor(
    private route: ActivatedRoute,
    private productService: ProductService,
    private cartService: CartService,
    private authService: AuthService
  ) {
    this.product = {} as IProduct;
  }

  ngOnInit(): void {
    const idParam = this.route.snapshot.paramMap.get('id');
    if (idParam !== null) {
      this.productId = +idParam;
      this.getProduct();
    }
  }

  getProduct(): void {
    this.productService.getProduct(this.productId)
      .subscribe(product => this.product = product);
  }

  addToCart(product: IProduct): void {
    this.authService.getUserId()
      .subscribe(
        (user_id) => {
          this.user_id = user_id;
          // Предположим, что у вас есть свойство product_id в объекте IProduct
          this.cartService.addToCart(user_id, product)
            .subscribe(
              () => {
                console.log('Product added to cart successfully.');
                // Возможно, здесь вы хотите обновить данные о корзине
              },
              (error) => {
                this.errorMessage = 'Failed to add product to cart: ' + error.message;
              }
            );
        },
        (error) => {
          this.errorMessage = 'Failed to get user ID: ' + error.message;
        }
      );
  }
  
}
