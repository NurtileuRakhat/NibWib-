import { Component,Input } from '@angular/core';
import { Router } from '@angular/router';
import { IProduct } from '../../models/product';
@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrl: './product.component.css'
})
export class ProductComponent {
  @Input() product: IProduct | undefined;

  constructor(private router: Router) {}
  
  viewProduct(product: IProduct) {
    this.router.navigate(['/product', product.id]);
  }
}
