from django.urls import path,include
from .views import *
from rest_framework import routers
  # 'PurchaseView' adını doğru şekilde içe aktardığınızdan emin olun


router=routers.DefaultRouter()
router.register("purchases",PurchaseView)
router.register("firms",FirmView)
router.register("categorys",CategoryView)
router.register("sales",SalesView)
router.register("brands",BrandView)
router.register("products",ProductView)

urlpatterns = [
    path('', include(router.urls)),
    # path('purchases/<int:pk>/update/', PurchaseView.as_view({'put': 'update_purchase'}), name='purchase-update'),
]