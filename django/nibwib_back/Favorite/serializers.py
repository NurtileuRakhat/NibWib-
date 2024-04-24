# serializers.py
from rest_framework import serializers
from .models import *
from api.serializers import ProductSerializer
from api.serializers import ProductSerializer

class FavoriteItemProductSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = FavoriteItem
        fields = "__all__"

    def get_product(self, obj):
        return ProductSerializer(
            Product.objects.filter(
                id=obj.product.id
            ), context=self.context, many=True
        ).data
    
class FavoriteItemSerializer(serializers.Serializer):
    favorite = serializers.PrimaryKeyRelatedField(queryset=Favorite.objects.all(), required=False)
    id = serializers.IntegerField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    def create(self, validated_data):
        return FavoriteItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.favorite = validated_data.get('favorite', instance.favorite)
        instance.product = validated_data.get('product', instance.product)
        instance.save()
        return instance
    
class FavoriteSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Favorite
        fields = "__all__"

    def get_products(self, obj):
        return FavoriteItemProductSerializer(
            FavoriteItem.objects.filter(favorite=obj),
            context=self.context,
            many=True
        ).data
