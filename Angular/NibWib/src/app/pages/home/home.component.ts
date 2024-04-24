import { Component, OnInit } from '@angular/core';
import { ProductService } from '../../service/product.service';
import { IProduct } from '../../models/product';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  searchQuery!: string;
  searchResults$!: Observable<IProduct[]>; // здесь используется Observable

  constructor(private productService: ProductService) { }

  ngOnInit() {
    this.search();
  }

  search() {
    if (!this.searchQuery) {
      return;
    }
    this.searchResults$ = this.productService.searchProducts(this.searchQuery);
  }
}
