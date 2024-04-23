import { ICategory } from "./category";

export interface IProduct{
    id: number;
    name: string;
    description: string;
    price: number;
    image: string;
    category: ICategory;
    is_available: boolean;
    created_at: Date;
    modified_at: Date;
}