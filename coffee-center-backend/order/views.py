from rest_framework.viewsets import ModelViewSet
from order.models import OrderDetail, OrderItem, PaymentDetail
from order.serializer import OrderDetailSerializer, OrderItemSerializer, PaymentDetailSerializer
from accounts.models import CustomUser
from product.models import Product
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
    data = request.data
    payment = PaymentDetail()
    payment.amount = data['toPay']
    payment.total_price = data['totalPrice']
    payment.total_discount = data['totalDiscount']
    payment.provider = data['payment']['payment']
    payment.address_to_send = data['address']['Address']
    # payment.status = ''
    payment.save()

    order = OrderDetail()
    user_obj = CustomUser.objects.get(id=data['user']['id'])
    order.user = user_obj
    order.payment_method = payment
    order.save()

    for item in data['items']:
        product = OrderItem()
        product.order = order
        product.quantity = item['quantity']

        product_obj = Product.objects.get(id=item['product']['id'])
        product.product = product_obj
        product.save()


    
    
    
    print("details",request.data)
    return Response({"order_id":"successfully posted"}, status=status.HTTP_200_OK)