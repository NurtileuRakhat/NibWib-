from django.urls import path
from .views import *
from .authentication import CustomAuthToken, logout_user

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('logout/', logout_user, name='logout'),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:category_id>', get_category),
    path('categories/products/',  ProductList.as_view()),
    path('categories/products/<int:product_id>', get_product)
]
