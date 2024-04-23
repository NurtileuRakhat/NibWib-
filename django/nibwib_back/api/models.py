from django.conf import settings
from django.db import models
from rest_framework.authtoken.models import Token

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
    price = models.DecimalField(max_digits=8, decimal_places=2)
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