import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CategoryService } from '../../service/category.service';
import { ProductService } from '../../service/product.service';
import { ICategory } from '../../models/category';
import { IProduct } from '../../models/product';
import { RouterModule } from '@angular/router'; 


@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {
  category: ICategory;
  products: IProduct[] = [];

  constructor( private route: ActivatedRoute, private service: CategoryService) {
    this.category = {} as ICategory;
  }
  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      let strid = params.get('id');
      if (strid) {
        let id = +strid;  
        this.service.getCategory(id).subscribe((category) => {
          this.category = category;
        })
        this.service.getCategoryProducts(id).subscribe((p) => {
          this.products = p;
        })
      }
    });
  }
}
