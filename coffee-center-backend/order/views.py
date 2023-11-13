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

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def order_detail(request):
    print("details",request.data)
    return Response({"order_id":"successfully posted"}, status=status.HTTP_200_OK)