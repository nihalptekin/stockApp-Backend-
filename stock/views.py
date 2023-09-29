from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,DjangoModelPermissions

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters,status
from rest_framework.response import Response

from .models import(
    Category,
    Brand,
    Product,
    Firm,
    Purchases,
    Sales,
    
)
from .serializers import(
    CategorySerializer,
    CategoryProductSerializer,
    BrandSerializer,
    ProductSerializer,
    FirmSerializer,
    PurchasesSerializer,
    SalesSerializer,
    
)
# Create your views here.

class CategoryView(ModelViewSet):
    
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    # permission_classes=[DjangoModelPermissions]

    ## filter ve search 
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['name']
    search_fields=['name']
    # hangi seriazlizer kullanılacağını seç
   
    def get_serializer_class(self):
        if self.request.query_params.get("name"):
             # parametre VERİRSENİZ istenen categorye ait ürünleri verir
            return CategoryProductSerializer
        # parametre vermezseniz category ler gelir
        return super().get_serializer_class()

# class CategoryProductView(ModelViewSet):
    
#     queryset=Category.objects.all()
#     serializer_class=CategoryProductSerializer
    
#     filter_backends=[DjangoFilterBackend,filters.SearchFilter]
#     filterset_fields=['name']
#     search_fields=['name']
  

class BrandView(ModelViewSet):
    
    queryset=Brand.objects.all()
    serializer_class= BrandSerializer
    # permission_classes=[DjangoModelPermissions]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['name']
    search_fields=['name']

class ProductView(ModelViewSet):
    
    queryset=Product.objects.all()
    serializer_class= ProductSerializer
    # permission_classes=[DjangoModelPermissions]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['name']
    search_fields=['name']

class FirmView(ModelViewSet):
    
    queryset=Firm.objects.all()
    serializer_class= FirmSerializer
    # permission_classes=[DjangoModelPermissions]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['name']
    search_fields=['name']

class PurchasesView(ModelViewSet):
    
    queryset=Purchases.objects.all()
    serializer_class= PurchasesSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ## add quantity to product stock field 
        purchase=request.data
        product=Product.objects.get(id=purchase['product_id'])
        product.stock+= int(purchase['quantity'])
        product.save()

        #######
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        ## add quantity to product stock field 
        purchase=request.data
        product=Product.objects.get(id=purchase['product_id'])
        
        # product.stock+=purchase['quantity']
        # buradaki instance son yapılan alım
        # buradaki purchase güncel / olması istenen alıma ait veriler

        product.stock += purchase['quantity']- int(instance.quantity)

        #stock ta 10 vardı += 
        # alım da 10 geldi
        # stock 20 oldu
        # ama alım işlemi 10 edğil 5 ile değiştirilmek isteniyor

        product.save()
        #######
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class SalesView(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    # filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # search_fields = ['brand']
    # filterset_fields = ['product', 'brand']
    # permission_classes = [DjangoModelPermissions]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        ###### Reduce Product Stock #######
        sale = request.data
        product = Product.objects.get(id=sale['product_id'])
        # sq=int(sale['quantity'])
        # # print(type(sale['quantity']))
        # # print(product.stock)
        if sale['quantity'] <= product.stock:
            product.stock -= sale['quantity']
            product.save()
        else:
            data = {
                "message": f"Dont have enough stock. Current stock is {product.stock}"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        ###################################
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        ### update product stock #######
        
        sale = request.data
        product = Product.objects.get(id=sale['product_id'])
        
        if sale['quantity'] <= instance.quantity + product.stock:
            product.stock += instance.quantity - sale['quantity']
            product.save()
        else:
            data = {
                "message": f"Dont have enough stock. Current stock is {product.stock}"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
            
        ################################
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        ### delete product stock  ###
        product = Product.objects.get(id=instance.product_id)    
        product.stock += instance.quantity
        product.save()
        #############################
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
    