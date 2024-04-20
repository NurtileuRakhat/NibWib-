from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Product)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'category']

admin.site.register(Cart)
admin.site.register(User)
admin.site.register(Wishlist)
