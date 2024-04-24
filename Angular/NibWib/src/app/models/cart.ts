import { IProduct } from "./product";
export interface Cart {
    products: CartItem[];
    total_price: number;
    total_count: number;
  }
  
  export interface CartItem {
    id: number;
    product: IProduct[];
    cart: Cart;
    count: number;
    price: number;
  }
  