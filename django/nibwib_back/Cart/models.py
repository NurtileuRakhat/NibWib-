from django.db import models
from UserApp.models import ModelUser
from api.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

class Cart(models.Model):
    customer = models.ForeignKey(
        ModelUser, related_name='cart',
        on_delete=models.CASCADE
    )
    total_price = models.DecimalField(
        max_digits=8, decimal_places=2, default=0
    )
    total_count = models.IntegerField(default=0)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, related_name='cart_items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.DecimalField(
        max_digits=8, decimal_places=2, default=0
    )

@receiver(post_save, sender=ModelUser)
def get_cart_price(sender, **kwargs):
    user = kwargs['instance']
    if not Cart.objects.filter(customer=user).exists():
        Cart.objects.create(customer=user)
        
@receiver([post_save, post_delete], sender=CartItem)
def update_cart_total_price_and_count(sender, **kwargs):
    cart_item = kwargs['instance']
    cart = Cart.objects.get(id=cart_item.cart.id)
    result = CartItem.objects.filter(cart=cart).aggregate(
        total_price=Sum('price'), total_count=Sum('count'))
    cart.total_price = result['total_price']
    cart.total_count = result['total_count']
    if not result['total_count'] and not result['total_price']:
        cart.total_price = 0
        cart.total_count = 0
    cart.save() 
