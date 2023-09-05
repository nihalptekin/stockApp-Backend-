from django.shortcuts import render
from .models import *
from .serializers import PurschaseSerializer, SaleSerializer, FirmSerializer, BrandSerializer, ProductSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
# from .permissions import IsAdminOrReadOnly
from datetime import datetime,date

# Create your views here.
class PurchaseView(viewsets.ModelViewSet):
    queryset=Purchase.objects.all()
    serializer_class=PurschaseSerializer
    # permission_classes= [IsAdminUser]  
    # permission_classes= [IsAdminOrReadOnly] 
    # 
    def purchases(request):
        purchases=Purchase.objects.all()
        context={
        'purchases':purchases
    }
        return render(request, context) 
   
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
    # permission_classes= [IsAdminUser]  
    # permission_classes= [IsAdminOrReadOnly] 
    # 
    def firms(request, pk):
        firms=Firm.objects.all(id=pk)
        context={
        'firms':firms
    }
        return render(request, context)
    
class BrandView(viewsets.ModelViewSet):
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer
    # permission_classes= [IsAdminUser]  
    # permission_classes= [IsAdminOrReadOnly] 
    # 
    def brands(request):
        brands=Brand.objects.all()
        context={
        'brands':brands
    }
        return render(request, context)
    
class ProductView(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # permission_classes= [IsAdminUser]  
    # permission_classes= [IsAdminOrReadOnly] 
    # 
    def products(request):
        products=Product.objects.all()
        context={
        'products':products
    }
        return render(request, context)
    
class CategoryView(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    # permission_classes= [IsAdminUser]  
    # permission_classes= [IsAdminOrReadOnly] 
    # 
    def categorys(request):
        categorys=Category.objects.all()
        context={
        'categorys':categorys
    }
        return render(request, context)
    

    






    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.user.is_staff:
    #         return queryset
    #     return queryset.filter(user=self.request.user)

    # şu andan onceki uçuşları getirme
    # def get_queryset(self):
    #     queryset = super().get_queryset()

    #     now = datetime.now()
    #     current_time = now.strftime('%H:%M:%S')
    #     today = date.today()
        
    #     if self.request.user.is_staff: 
    #         return queryset
    #     else:
            # print(now) 
            # now o anki tarih ve zamanı alıyor
            # "2023-08-07 13:42:46.564569"
            #__gt great then
           #__gte great then or equal
           #__lt less then 
           #__lte less then or equal
            # queryset = Purchase.objects.filter(date_departure__gt=now)

            # if Flight.objects.filter(date_departure=today):
            #     today_qs = Flight.objects.filter(date_departure=today).filter(estimated_time__gt=current_time)
            #     queryset = queryset.union(today_qs)
                
            # return queryset

# class ReservationView(viewsets.ModelViewSet):

#     queryset=Reservation.objects.all()
#     serializer_class=ReservationSerializer
#     permission_classes=[IsAuthenticated]
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if self.request.user.is_staff:
#             return queryset
#         return queryset.filter(user=self.request.user)

# class PassengerView(viewsets.ModelViewSet):
#     queryset=Passenger.objects.all()
#     serializer_class=PassengerSerializer