from django.urls import path
from .views import FavoriteListAPIView, FavoriteItemViewSet

urlpatterns = [
    path('<int:id>/add_to_favorites/', FavoriteItemViewSet.as_view({'post': 'create'})),
    path('<int:id>/remove_from_favorites/<int:pk>/', FavoriteItemViewSet.as_view({'delete': 'destroy'})),
    path('<int:id>/', FavoriteListAPIView.as_view({'get': 'retrieve','delete': 'clear_favorite'})),
]
