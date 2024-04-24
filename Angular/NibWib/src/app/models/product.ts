import { ICategory } from "./category";

export interface IProduct{
    id: number;
    name: string;
    description: string;
    price: number;
    image: string;
    category: ICategory;
     products: any;
}