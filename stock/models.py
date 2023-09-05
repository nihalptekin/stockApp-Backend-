from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Firm(models.Model):
    name=models.CharField(max_length=30)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=200)
    image=models.TextField()
    
    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Brand(models.Model):
    name=models.CharField(max_length=30)
    image=models.TextField()

    def __str__(self):
        return f"{self.name}"
     
class Product(models.Model):
    name=models.CharField(max_length=30)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categorys")
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE,related_name="brands")
    stock=models.SmallIntegerField()
    created=models.DateTimeField(auto_created=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.brand}"
    
class Purchase(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE,related_name="firms")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # max_digits ve decimal_places değerlerini gerektiğine göre ayarlayın
    price_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # max_digits ve decimal_places değerlerini gerektiğine göre ayarlayın

    def __str__(self):
        return f"{self.firm} - {self.brand} - {self.product}"

    def save(self, *args, **kwargs):
        # price_total hesaplamasını burada yapabilirsiniz
        self.price_total = self.quantity * self.price
        super(Purchase, self).save(*args, **kwargs)

class Sale(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.product}"
    
    def save(self, *args, **kwargs):
        # price_total hesaplamasını burada yapabilirsiniz
        self.price_total = self.quantity * self.price
        print(self.price_total)
        super(Sale, self).save(*args, **kwargs)




    


