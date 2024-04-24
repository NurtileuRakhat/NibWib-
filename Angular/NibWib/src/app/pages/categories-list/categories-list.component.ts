import { Component, OnInit } from '@angular/core';
import { ICategory } from '../../models/category';
import { CategoryService } from '../../service/category.service';
import { RouterModule } from '@angular/router'; 

@Component({
  selector: 'app-categories-list',
  templateUrl: './categories-list.component.html',
  styleUrls: ['./categories-list.component.css'] 
})
export class CategoriesListComponent implements OnInit {
  loading = false;

  newCategory: ICategory;
  categories: ICategory[] = [];
  
  constructor(private categoryService: CategoryService) {
    this.newCategory = {} as ICategory;
  }

  ngOnInit() {
    this.categoryService.getCategories().subscribe((categories) => {
      console.log(categories);
      this.categories = categories;
    });
  }

  toggleCategory(category: ICategory) {
    this.categoryService.toggleCategory(category);
  }
}
