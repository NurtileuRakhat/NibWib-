from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'total_count')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'count', 'price')