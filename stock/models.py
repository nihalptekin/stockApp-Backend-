from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone


# Create your models here.
class FixFields(models.Model):
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
     #!  eger abstract =True yazmaysak yeni model olusturur. Bunu istemiyoruz
    class Meta:
        abstract=True

class Brand(models.Model):
    name=models.CharField(max_length=30)
    image=models.TextField()

    def __str__(self):
        return f"{self.name}"
    
class Category(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return f"{self.name}"
     
class Product(FixFields):
    name=models.CharField(max_length=30)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", null=True)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE,related_name="b_products", null=True)
    stock=models.SmallIntegerField(blank=True, default=0)
    # created=models.DateTimeField(auto_created=True)
    # updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.brand}"
    
    
class Firm(models.Model):
    name=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    image=models.TextField()
    
    def __str__(self):
        return f"{self.name}"
    
class Purchases(FixFields):
    #normalde Null daha mantikli. models.SET_NULL
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE,related_name="firm_purchase")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand_purchases", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_purchase")
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, validators=[MinValueValidator(0)], decimal_places=2)  # max_digits ve decimal_places değerlerini gerektiğine göre ayarlayın
    price_total=models.DecimalField(blank=True, max_digits=8,validators=[MinValueValidator(0)],decimal_places=2, null=True) # max_digits ve decimal_places değerlerini gerektiğine göre ayarlayın

    def __str__(self):
        return f"{self.user} - {self.firm} - {self.product}"
  
  #!price total asagidaki gibi hesaplanabilir ama bu kez farkli bir yöntem denemek icin signals.py'de kullandik
    # def save(self, *args, **kwargs):
    #      # price_total hesaplamasını burada yapabilirsiniz
    #      self.price_total = self.quantity * self.price
    #      super(Purchases, self).save(*args, **kwargs)

class Sales(FixFields):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand_sales", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="p_sales")
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.product}"
    
    def save(self, *args, **kwargs):
        # price_total hesaplamasını burada yapabilirsiniz
        self.price_total = self.quantity * self.price
        print(self.price_total)
        super(Sales, self).save(*args, **kwargs)


    


