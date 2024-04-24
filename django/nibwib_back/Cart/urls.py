from django.urls import path
from .views import CartViewSet, CartItemViewSet

urlpatterns = [
    path('<int:id>/', CartViewSet.as_view({'get': 'retrieve','delete': 'clear_cart'})),
    path('<int:id>/cart_item/', CartItemViewSet.as_view({'post': 'create'})),
    path('<int:id>/cart_item/<int:pk>/', CartItemViewSet.as_view({'delete': 'destroy', 'put': 'update'})),
]
