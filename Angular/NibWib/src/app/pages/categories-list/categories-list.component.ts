import { Component, OnInit } from '@angular/core';
import { ICategory } from '../../models/category';
import { CategoryService } from '../../service/category.service';

@Component({
  selector: 'app-categories-list',
  templateUrl: './categories-list.component.html',
  styleUrls: ['./categories-list.component.css'] 
})
export class CategoriesListComponent implements OnInit {
  categories: ICategory[] = [];
  loading = false;

  constructor(private categoryService: CategoryService) {}

  ngOnInit(): void {
    this.loading = true;
    this.categoryService.getCategories().subscribe((data) => {
      this.loading = false;
      this.categories = data;
    });
  }
}
