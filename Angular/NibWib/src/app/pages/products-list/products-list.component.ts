import { Component } from '@angular/core';
import { ProductService } from '../../service/product.service';
import { IProduct } from '../../models/product';
import { RouterModule } from '@angular/router'; 

@Component({
  selector: 'app-products-list',
  templateUrl: './products-list.component.html',
  styleUrl: './products-list.component.css'
})
export class ProductsListComponent {
  products: IProduct[] = [];

  constructor(private productService: ProductService) {
  }

  ngOnInit() {
    this.productService.getProducts().subscribe((p) => {
      this.products = p;
    });
  }
}
