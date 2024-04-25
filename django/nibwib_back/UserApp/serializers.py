from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import ModelUser

# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ModelAddress
#         fields = ("unique_id", "name", "city", "street", "address")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelUser
        fields = "__all__"

class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=ModelUser.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = ModelUser
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name','avatar')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'avatar': {'required': False},
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        user = ModelUser.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            avatar = validated_data.get("avatar"),
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

        
class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=ModelUser.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = ModelUser
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'avatar')
        extra_kwargs = {
            'username': {'required': False},  
            'first_name': {'required': True},
            'last_name': {'required': True},
            'avatar': {'required': False},
        }
        
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if value and attr != 'password':
                setattr(instance, attr, value)
        instance.save()
        return instance
