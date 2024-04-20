from django.db import models
from rest_framework.authtoken.models import Token

class User (models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatar/', blank=True, default='1640528661_1-abrakadabra-fun-p-serii-chelovek-na-avu-1.png')

    def __str__(self):
        return self.username
    
    def to_json(self):
        return {
            'id': self.id,
            'username': self.user_id,
            'password': self.address,
            'avatar': self.avatar
        }

class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='product ID')
    address = models.CharField(max_length=200)

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'address': self.address,
        }

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='catgory/', blank=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.id}: {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
        }

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='products/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
    def __str__(self):
        return f'{self.id}: {self.name}, {self.category}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image': self.image,
            'category': self.category.name
        }
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.user}, {self.products}'

    def to_json(self):
        return {
            'id': self.id,
            'user': self.user.username,
            'products': self.products,
            'total_price': self.total_price,
            'created_at': self.created_at
        }

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.product}, {self.user}'

    def to_json(self):
        return {
            'id': self.id,
            'product': self.product,
            'user': self.user.username,
            'text': self.text,
            'created_at': self.created_at
        }
    
class Wishlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user ID')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product ID')
