import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CategoriesListComponent } from './pages/categories-list/categories-list.component';
import { CategoriesComponent } from './components/category/category.component';
import { ProductComponent } from './components/product/product.component';

const routes: Routes = [
  { path: '', component: CategoriesListComponent },
  { path: 'categories/:categoryId', component: CategoriesComponent },
  { path: 'categories/:categoryId/products/:productId', component: ProductComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
