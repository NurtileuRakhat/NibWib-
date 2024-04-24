from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('get_id/', get_user_id),
    path('profile/', UserProfileRetrieveAPIView.as_view(), name='user-profile'),
    path('profile/update/', UserProfileUpdateAPIView.as_view(), name='user-profile-update'),
]
