from django.urls import path, include
from order.views import OrderDetailViewSet, OrderItemViewSet, PaymentDetailViewSet ,order_detail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'orders', OrderDetailViewSet, basename='order_detail')
router.register(r'items', OrderItemViewSet, basename='order_item')
router.register(r'payments', PaymentDetailViewSet, basename='payment_detail')

urlpatterns = [
    path('', include(router.urls)),
    path("data/",order_detail)
]
