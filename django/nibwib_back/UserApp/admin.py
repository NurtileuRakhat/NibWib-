from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ModelUser


# Register your models here.
@admin.register(ModelUser)
class CustomUserAdmin(UserAdmin):
    model        = ModelUser
    fieldsets    = UserAdmin.fieldsets +(
        ("Extra",{
            "fields":["avatar"]
        }),
    )