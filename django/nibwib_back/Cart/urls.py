from django.urls import path
from .views import CartViewSet, CartItemViewSet

urlpatterns = [
    path('<int:pk>/', CartViewSet.as_view({'get': 'retrieve'})),
    path('<int:cart_id>/cart_item/', CartItemViewSet.as_view({'post': 'create'}))
]
