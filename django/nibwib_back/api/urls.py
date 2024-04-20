from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/',  TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:category_id>', CategoryDetailAPIView.as_view()),
    path('categories/<int:category_id>/products', Category_products.as_view()),
    path('products/',  ProductList.as_view()),
    path('products/<int:product_id>', get_product)
]
