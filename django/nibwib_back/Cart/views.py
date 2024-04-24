from decimal import Decimal
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import permissions
from rest_framework import viewsets, status, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import get_object_or_404

class IsCartOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user

class IsCartOwnerForCartItems(permissions.BasePermission):
    def has_permission(self, request, view):
        id = view.kwargs.get('id')
        cart = get_object_or_404(Cart, id=id)
        return cart.customer == request.user
    
class CartViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    permission_classes = (IsCartOwner,)
    serializer_class = CartSerializer
    lookup_field = 'id'  # Используем 'id' в качестве поля первичного ключа

    def clear_cart(self, request, *args, **kwargs):
        cart_instance = self.get_object()
        cart_items = cart_instance.cart_items.all()
        cart_items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CartItemViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = CartItemSerializer
    permission_classes = (IsCartOwnerForCartItems,)
    lookup_field = 'id'  # Используем 'id' в качестве поля первичного ключа

    def get_queryset(self):
        cart = get_object_or_404(Cart, id=self.kwargs.get('id'))
        queryset = cart.cart_items.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(id=self.kwargs.get('id'))

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy() 
        mutable_data['cart'] = self.kwargs.get('id')
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        cart_id = self.kwargs.get('id')
        item_id = self.kwargs.get('pk')
    
        try:
            cart = Cart.objects.get(id=cart_id)
            item = CartItem.objects.get(id=item_id, cart=cart)
            count = Decimal(request.data.get('count', str(item.count)))
            item.count = count
            item.price = item.product.price * count

            if count <= 0:
                item.delete()
            else:
                item.save()
            serializer = self.get_serializer(item)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except CartItem.DoesNotExist:
            return Response({"detail": "CartItem does not exist in the specified Cart."}, status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, *args, **kwargs):
        cart_id = self.kwargs.get('id')
        item_id = self.kwargs.get('pk')
        
        try:
            cart = Cart.objects.get(id=cart_id)
            item = CartItem.objects.get(id=item_id, cart=cart)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except CartItem.DoesNotExist:
            return Response({"detail": "CartItem does not exist in the specified Cart."}, status=status.HTTP_404_NOT_FOUND)