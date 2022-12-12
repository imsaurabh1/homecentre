from django.contrib import admin

from .models import Category, Product

#Adding Category and Product to Django Admin Interface
admin.site.register(Category)
admin.site.register(Product)