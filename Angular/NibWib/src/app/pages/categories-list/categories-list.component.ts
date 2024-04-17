import { Component } from '@angular/core';
import { ICategory } from '../../models/category';
import { CategoryService } from '../../service/category.service';
@Component({
  selector: 'app-categories-list',
  templateUrl: './categories-list.component.html',
  styleUrl: './categories-list.component.css'
})
// export class CategoriesListComponent {
//   categories: ICategory[] = [];
//   loading = false;

//   constructor(private categoryService: CategoryService) {}

//   ngOnInit(): void {
//     this.loading = true;
//     this.categoryService.getCategories().subscribe((data) => {
//       this.loading = false;
//       this.categories = data;
//     });
//   }
// }
export class CategoriesListComponent {
  newCategory: ICategory;
  categories: ICategory[] = [];


  constructor(private categoryService: CategoryService) {
    this.newCategory = {} as ICategory;
  }

  ngOnInit() {
    this.categoryService.getCategories().subscribe((categories) => {
      this.categories = categories;
    });
  }
}