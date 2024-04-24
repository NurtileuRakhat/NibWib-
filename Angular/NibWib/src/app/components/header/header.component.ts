import { Component } from '@angular/core';
import { ProductService } from '../../service/product.service';
import { IProduct } from '../../models/product';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  searchQuery!: string;
  searchResults!: Observable<IProduct[]>;
  showSearchResults: boolean = false; 

  constructor(private router: Router, private productService: ProductService) { }

  search() {
    if (!this.searchQuery) {
      return;
    }
    this.searchResults = this.productService.searchProducts(this.searchQuery);
    this.showSearchResults = true; 
  }

  navigateToProduct(productId: number) {
    this.showSearchResults = false; 
    this.router.navigate(['/products', productId]);
  }
}
