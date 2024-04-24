import { IProduct } from "./product";

export interface Favorite {
    products: FavoriteItem[];
    date: Date;
}

export interface FavoriteItem {
    id: number;
    product: IProduct[];
    favorite: Favorite;
}
