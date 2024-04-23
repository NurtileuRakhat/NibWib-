import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { IProduct } from '../../models/product';
import { ProductService } from '../../service/product.service';
import { RouterModule } from '@angular/router';
import { CartService } from '../../service/cart.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {
  productId: number = 0;
  product: IProduct;

  constructor(
    private route: ActivatedRoute,
    private productService: ProductService,
    private cartService: CartService
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

  // addToCart(productId: number): void {
  //   this.cartService.addToCart(productId)
  //     .subscribe(() => console.log('Product added to cart')); // Handle success or display a message
  // }
  
}
