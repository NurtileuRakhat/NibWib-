import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CategoryService } from '../../service/category.service';
import { ProductService } from '../../service/product.service';
import { ICategory } from '../../models/category';
import { IProduct } from '../../models/product';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoriesComponent implements OnInit {
  category: ICategory | undefined;
  products: IProduct[] = [];
  loading = false;

  constructor(
    private route: ActivatedRoute,
    private categoryService: CategoryService,
    private productService: ProductService
  ) {}

  ngOnInit(): void {
    console.log('Component initialized');

    this.route.paramMap.subscribe(params => {
      console.log('Params changed:', params);

      const strId = params.get('categoryId');
      if (strId) {
        console.log('Category ID:', strId);

        const id = +strId;
        this.loading = true;

        this.categoryService.getCategory(id).subscribe({
          next: category => {
            console.log('Category:', category);
            this.category = category;
            this.loading = false;
          },
          error: error => {
            console.error('Error loading category:', error);
            this.loading = false;
          }
        });
        
        this.productService.getProductsByCategoryId(id).subscribe({
          next: products => {
            console.log('Products:', products);
            this.products = products;
          },
          error: error => {
            console.error('Error loading products:', error);
          }
        });
        
      }
    });
  }
}
