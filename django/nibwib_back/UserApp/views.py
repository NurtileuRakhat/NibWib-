from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.validators import UniqueValidator
from .serializers import *
from .models import ModelUser

class UserProfileRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UserProfileUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateUserSerializer

    def get_object(self):
        return self.request.user

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_id(request):
    user_id = request.user.id
    return JsonResponse({'user_id': user_id}, status=status.HTTP_200_OK)

class RegisterUserView(CreateAPIView):
    queryset = ModelUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer


# class CreateAddressView(CreateAPIView):
#     queryset = ModelAddress.objects.all()
#     serializer_class = AddressSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
