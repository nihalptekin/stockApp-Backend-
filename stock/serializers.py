from rest_framework import serializers
from .models import *

class FixSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False)
    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)


class PurchasesSerializer(FixSerializer):
    firm=serializers.StringRelatedField()
    firm_id=serializers.IntegerField()
    brand=serializers.StringRelatedField()
    brand_id=serializers.IntegerField()
    product=serializers.StringRelatedField()
    product_id=serializers.IntegerField()
    class Meta:
        model=Purchases
        fields= "__all__"
            
        read_only_fields=('price_total', 'user_id')

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model=Firm
        fields="__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields="__all__"

class SalesSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    
    category = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Sales
        fields = (
            "id",
            "user",
            "brand",
            "brand_id",
            "product",
            "product_id",
            "category",
            "quantity",
            "price",
            "price_total",
            "created",
            "updated",
            
        )
        
        read_only_fields = ('user', "price_total")
        
    def get_category(self,obj):
        return obj.product.category.name
    
     #!modelde tanimladigimiz price totali yoruma aldigim icin read only olmasini istedigim kodu da purchases kismina yazdim. buna artik gerek.   
    # price_total=serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2,)

class CategorySerializer(serializers.ModelSerializer):
    #categoride yer alanlarin kac tane ürünü ildugunu say. mesela electronik kategorisinde kac tane ürün var onu saymasi icn get_product_count'u kullandik.
    product_count=serializers.SerializerMethodField()
    
    class Meta:
        model=Category
        fields=(
            "id",
            "name",
            "product_count",
            )
        
    def get_product_count(self, obj):
        return obj.product.count()
       #  return Product.objects.filter(category_id=obj_id).count()


class ProductSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    brand=serializers.StringRelatedField()
    category_id=serializers.IntegerField()
    brand_id=serializers.IntegerField()

    class Meta:
        model=Product
        fields=("id",
            "name",
            "stock",
            "category",
            "category_id",
            "brand",
            "brand_id",
        )


class CategoryProductSerializer(serializers.ModelSerializer):
    product_count=serializers.SerializerMethodField()
    #many true demezsek yanlis olur. 
    products=ProductSerializer(many=True)
    class Meta:
        model=Category
        fields=(
            "id",
            "name",
            "product_count",
            "products",
            )

    def get_product_count(self, obj):
        return obj.products.count()
        # return Product.objects.filter(category_id=obj_id).count()




