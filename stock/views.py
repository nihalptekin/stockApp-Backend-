from django.shortcuts import render
from .models import *
from .serializers import PurchaseSerializer, SaleSerializer, FirmSerializer, BrandSerializer, ProductSerializer, CategorySerializer, CategoryProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters, status
from rest_framework.permissions import IsAdminUser,IsAuthenticated, DjangoModelPermissions
# from .permissions import IsAdminOrReadOnly
from datetime import datetime,date
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class PurchasesView(viewsets.ModelViewSet):
    queryset=Purchase.objects.all()
    serializer_class= PurchaseSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ## add quantity to product stock field
        purchase=request.data
        product=Product.objects.get(id=pruchase["procudt_id"])
        product.stock+=purchase["quantity"]
        product.save()

        ###########*
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()

    
class SalesView(viewsets.ModelViewSet):
    queryset=Sale.objects.all()
    serializer_class=SaleSerializer
    # permission_classes= [IsAdminUser]  
    # permission_classes= [IsAdminOrReadOnly] 
    # 
    def sales(request):
        sales=Sale.objects.all()
        context={
        'sales':sales
    }
        return render(request, context)
    

    
class FirmView(viewsets.ModelViewSet):
    queryset=Firm.objects.all()
    serializer_class=FirmSerializer
    #permission_classes=[DjangoModelPermissions] 
    filter_backends=[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields=['name']
    search_fields=['name']
    # permission_classes= [IsAdminUser]  
    # permission_classes= [IsAdminOrReadOnly] 

    
class BrandView(viewsets.ModelViewSet):
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer
    #permission_classes=[DjangoModelPermissions] 
    filter_backends=[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields=['name']
    search_fields=['name']
   
    
class ProductView(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #permission_classes=[DjangoModelPermissions]
    filter_backends=[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields=['name']
    search_fields=['name']
    #? Hangi serializer kulanilacagini sec
   
    def get_serializer_class(self):
        if self.request.query_params.get("name"):
          #?parametre vermirsek istenen categoriye ait ürünler gelir
          return CategoryProductSerializer
         #?parametre vermezsek categoriler gelir
        return super().get_serializer_class()

# class CategoryProductView(viewsets.ModelViewSet):
#     queryset=Category.objects.all()
#     serializer_class=CategoryProductSerializer
  
#     filter_backends=[DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields=['name']
#     search_fields=['name']
    
class CategoryView(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    # permission_classes=[DjangoModelPermissions]
    filter_backends=[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields=['name']
    search_fields=['name']



    