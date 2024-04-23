from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:category_id>', get_category),
    path('categories/<int:category_id>/products', Category_products.as_view()),
    path('products/',  ProductList.as_view()),
    path('products/<int:product_id>', get_product),
]