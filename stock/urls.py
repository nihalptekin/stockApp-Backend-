from django.urls import path,include
from .views import *
from rest_framework import routers
  # 'PurchaseView' adını doğru şekilde içe aktardığınızdan emin olun


router=routers.DefaultRouter()
router.register("purchase",PurchaseView)
router.register("firms/<int:pk>",FirmView)
router.register("categorys",CategoryView)
router.register("sales",SalesView)
router.register("brands",BrandView)
router.register("products",ProductView)

urlpatterns = [
    path('', include(router.urls)),

]