from django.contrib import admin

# Register your models here.
from .models import Purchases, Sales, Firm, Brand, Category, Product
admin.site.register(Purchases)
admin.site.register(Sales)
admin.site.register(Firm)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)