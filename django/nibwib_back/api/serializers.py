from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    products = ProductSerializer(source='product_set',many=True, required=False)
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


# User = get_user_model()


# class Userserializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password',
#                   'first_name', 'last_name', 'email',)
#         extra_kwargs = {'password': {"write_only": True, 'required': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         Token.objects.create(user=user)
#         return user

