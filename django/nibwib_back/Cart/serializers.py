from rest_framework import serializers
from .models import *
from api.serializers import ProductSerializer
from rest_framework.exceptions import ValidationError

class CartItemProductSerializer(serializers.ModelSerializer):
    """
    Формирует список товаров, находящихся к корзине, с указанием
    количества и общей стоимости конкретного товара.
    """
    product = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('product', 'count', 'price')

    def get_product(self, obj):
        return ProductSerializer(
            Product.objects.filter(
                id=obj.product.id
            ), context=self.context, many=True
        ).data


class CartItemSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(
        queryset=Cart.objects.all(), required=False
    )

    class Meta:
        model = CartItem
        fields = ('cart', 'product', 'count', 'price')

    def validate(self, data):
        if self.context.get('request').method == 'POST':
            if data.get('count') <= 0:
                raise ValidationError(
                    'Количество добавляемого в корзину '
                    'товара не может быть меньше или равно 0'
                )
        return data

    def create(self, validated_data):
        cart = validated_data.get('cart')
        product = validated_data.get('product')
        count = validated_data.get('count')
        existing_item = CartItem.objects.filter(cart=cart, product=product).first()
        
        if existing_item:
            existing_item.count += count
            existing_item.price += product.price * count
            existing_item.save()
            return existing_item
        else:
            price = product.price * count
            cart_item = CartItem.objects.create(
                cart=cart, product=product, count=count, price=price
            )
            return cart_item
        
    def update(self, instance, validated_data):
        count = validated_data.get('count')
        product = Product.objects.get(id=instance.product.id)
        instance.count = count + instance.count
        instance.price = product.price * instance.count
        if instance.count <= 0:
            instance.delete()
        else:
            instance.save()
        return instance


class CartSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('products', 'total_price', 'total_count')

    def get_products(self, obj):
        return CartItemProductSerializer(
            CartItem.objects.filter(cart=obj),
            context=self.context,
            many=True
        ).data
