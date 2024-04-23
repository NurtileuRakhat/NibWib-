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
        cart = Cart.objects.get(id=view.kwargs.get('cart_id'))
        return cart.customer == request.user
    
class CartViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    permission_classes = (IsCartOwner,)
    serializer_class = CartSerializer

class CartItemViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, viewsets.GenericViewSet
):
    """Добавить продукт в корзину, изменить количество,
    отчистить корзину полностью.
    """
    serializer_class = CartItemSerializer
    permission_classes = (IsCartOwnerForCartItems,)

    def get_queryset(self):
        cart = get_object_or_404(Cart, id=self.kwargs.get('cart_id'))
        queryset = cart.cart_items.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            cart_id=self.kwargs.get('cart_id')
        )

    def create(self, request, *args, **kwargs):
        """Добавить продукты в корзину"""
        mutable_data = request.data.copy() 
        mutable_data['cart'] = self.kwargs.get('cart_id')
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        """Изменить количество продукта в корзине"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if instance.id is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """Отчистить корзину полностью."""
        instance = self.get_queryset()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
