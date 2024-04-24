from decimal import Decimal
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import permissions
from rest_framework import viewsets, status, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import get_object_or_404

class IsFavoriteOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsFavoriteOwnerForFavoriteItems(permissions.BasePermission):
    def has_permission(self, request, view):
        id = view.kwargs.get('id')
        favorite = get_object_or_404(Favorite, id=id)
        return favorite.user == request.user
    
class FavoriteListAPIView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Favorite.objects.all()
    permission_classes = (IsFavoriteOwner,)
    serializer_class = FavoriteSerializer
    lookup_field = 'id'  

    def clear_favorite(self, request, *args, **kwargs):
        instance = self.get_object()
        favorite_items = instance.favorite_items.all()
        favorite_items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class FavoriteItemViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = FavoriteItemSerializer
    permission_classes = (IsFavoriteOwnerForFavoriteItems,)
    lookup_field = 'id' 
    
    def get_queryset(self):
        favorite = get_object_or_404(Favorite, id=self.kwargs.get('id'))
        queryset = favorite.items.all()
        return queryset

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save(favorite_id=self.kwargs.get('id'))  
        
    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy() 
        favorite_id = self.kwargs.get('id')
        product_id = mutable_data.get('product')
        
        if FavoriteItem.objects.filter(favorite_id=favorite_id, product_id=product_id).exists():
            return Response({"detail": "This product is already in the favorite items."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)  # Validate the serializer
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def destroy(self, request, *args, **kwargs):
        favorite_id = self.kwargs.get('id')
        item_id = self.kwargs.get('pk')
        
        try:
            favorite = Favorite.objects.get(id=favorite_id)
            item = FavoriteItem.objects.get(id=item_id, favorite=favorite)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Favorite.DoesNotExist:
            return Response({"detail": "Favorite does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except FavoriteItem.DoesNotExist:
            return Response({"detail": "FavoriteItem does not exist in the specified Favorite."}, status=status.HTTP_404_NOT_FOUND)