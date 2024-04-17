from django.urls import path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:category_id>', get_category),
    path('categories/products/',  ProductList.as_view()),
    path('categories/products/<int:product_id>', get_product)
]
