from django.db import models
from api.models import Product
from UserApp.models import ModelUser
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

class Favorite(models.Model):
    user = models.ForeignKey(ModelUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

@receiver(post_save, sender=ModelUser)
def create_favorite(sender, **kwargs):
    user = kwargs['instance']
    if not Favorite.objects.filter(user=user).exists():
        Favorite.objects.create(user=user)
        