from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(models.Product)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'category']
