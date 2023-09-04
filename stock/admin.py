from django.contrib import admin

# Register your models here.
from .models import Purchases, Sales, Firms, Brand, Category, Product
admin.site.register(Purchases)
admin.site.register(Sales)
admin.site.register(Firms)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)