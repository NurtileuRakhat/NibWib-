import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CategoriesListComponent } from './pages/categories-list/categories-list.component';
import { CategoryComponent } from './components/category/category.component';
import { ProductComponent } from './components/product/product.component';
import { ProductsListComponent } from './pages/products-list/products-list.component';
import { HomeComponent } from './pages/home/home.component';

const routes: Routes = [
  { path: '', component:  HomeComponent},
  { path: 'categories', component: CategoriesListComponent },
  { path: 'categories/:categoryId', component: CategoryComponent },
  { path: 'products/:productId', component: ProductComponent },
  { path: 'products', component: ProductsListComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
