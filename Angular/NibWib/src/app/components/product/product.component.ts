import { Component,Input } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { IProduct } from '../../models/product';
import { ProductService } from '../../service/product.service';
import { RouterModule } from '@angular/router'; 

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrl: './product.component.css'
})
export class ProductComponent {
  product: IProduct;
  constructor( private route: ActivatedRoute, private service: ProductService) {
    this.product = {} as IProduct;
  }
  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      let strid = params.get('id');
      if (strid) {
        let id = +strid;
        this.service.getProduct(id).subscribe((value) => {
          console.log(value)
          this.product = value;
        })
      }
    });
  }
}
