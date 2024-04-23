from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework.generics import CreateAPIView
from UserApp.models import ModelUser
from rest_framework import permissions

# Create your views here.
class InOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user



class RegisterUserView(CreateAPIView):
    queryset = ModelUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

class CreateAddressView(CreateAPIView):
    queryset = ModelAddress.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [InOwner]

    def perform_create(self, serializer):
        serializer.save()