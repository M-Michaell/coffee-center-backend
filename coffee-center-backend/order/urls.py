from django.urls import path, include
from order.views import OrderDetailViewSet, OrderItemViewSet, PaymentDetailViewSet ,order_detail,order_paid,user_orders
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'orders', OrderDetailViewSet, basename='order_detail')
router.register(r'items', OrderItemViewSet, basename='order_item')
router.register(r'payments', PaymentDetailViewSet, basename='payment_detail')

urlpatterns = [
    path('', include(router.urls)),
    path("data/",order_detail),
    path("paid/",order_paid),
    path("user/orders/<int:id>/",user_orders),
]
