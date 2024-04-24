import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CategoryService } from '../../service/category.service';
import { ICategory } from '../../models/category';
import { IProduct } from '../../models/product';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {
  category: ICategory;
  products: IProduct[] = [];
  errorMessage: string = ''; 
  selectedCategory: ICategory | null = null;
  
  constructor(private route: ActivatedRoute, private service: CategoryService) {
    this.category = {} as ICategory;
  }

  // ngOnInit(): void {
    // this.route.paramMap.subscribe(params => {
    //   const strId = params.get('id');
    //   if (strId) {
    //     const id = +strId;  
    //     this.service.getCategory(id).subscribe(
    //       (category) => {
    //         this.category = category;
    //       },
    //       (error) => {
    //         this.errorMessage = 'Failed to load category data.';
    //         console.error('Error fetching category:', error);
    //       }
    //     );
    //     this.service.getCategoryProducts(id).subscribe(
    //       (products) => {
    //         this.products = products;
    //       },
    //       (error) => {
    //         this.errorMessage = 'Failed to load products data.';
    //         console.error('Error fetching products:', error);
    //       }
    //     );
    //   }
    // });
  // }

  ngOnInit() {
    this.service.selectedCategory$.subscribe((category) => {
      this.selectedCategory = category;
    });
  }
}
