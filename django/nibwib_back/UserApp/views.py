from django.http import JsonResponse
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import *
from rest_framework.generics import CreateAPIView
from UserApp.models import ModelUser
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_id(request):
    try:
        user_id = request.user.id
    except user_id.DoesNotExist as error:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        return JsonResponse({'user_id': user_id},status=status.HTTP_200_OK)

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