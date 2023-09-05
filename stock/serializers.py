from rest_framework import serializers
from .models import *

class PurschaseSerializer(serializers.ModelSerializer):   
    class Meta:
        model=Purchase
        fields="__all__"

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model=Firm
        fields="__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields="__all__"

class SaleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Sale
        fields="__all__"
        
    price_total=serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2,)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"


