from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
import json

# with open('UserApp/data/city.json') as f:
#     cities = json.load(f)
# cities = [(k, v) for k, v in cities.items()]

# class ModelAddress(models.Model):
#     unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,verbose_name="Adres ID")
#     name = models.CharField(max_length=50)
#     city = models.CharField(choices=cities,max_length=50)
#     street = models.CharField(max_length=150)
#     address = models.TextField(max_length=500)  

class ModelUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, default='avatar/default_avatar.png')
    # address = models.ManyToManyField(ModelAddress, blank=True, related_name="user_addresses")
    # reset_password = models.BooleanField(default=False)
