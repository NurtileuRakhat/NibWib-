import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';
import { ICategory } from '../../models/category';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrl: './category.component.css'
})
export class CategoriesComponent {
  @Input() category: ICategory | undefined;

  constructor(private router: Router) {}
  
  viewCategory(category: ICategory) {
    this.router.navigate(['/categories', category.id]);
  }
}

