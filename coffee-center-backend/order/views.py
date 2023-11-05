from rest_framework.viewsets import ModelViewSet
from order.models import OrderDetail, OrderItem, PaymentDetail
from order.serializer import OrderDetailSerializer, OrderItemSerializer, PaymentDetailSerializer

class OrderDetailViewSet(ModelViewSet):
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return OrderDetail.objects.all()

class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return OrderItem.objects.all()

class PaymentDetailViewSet(ModelViewSet):
    serializer_class = PaymentDetailSerializer

    def get_queryset(self):
        return PaymentDetail.objects.all()
