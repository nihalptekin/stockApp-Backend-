from django.contrib import admin

# Register your models here.
from .models import Purchase, Sale, Firm, Brand, Category, Product
admin.site.register(Purchase)
admin.site.register(Sale)
admin.site.register(Firm)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)