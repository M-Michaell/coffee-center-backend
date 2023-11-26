from rest_framework.viewsets import ModelViewSet
from order.models import OrderDetail, OrderItem, PaymentDetail
from order.serializer import OrderDetailSerializer, OrderItemSerializer, PaymentDetailSerializer
from accounts.models import CustomUser
from product.models import Product
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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



@api_view(['POST'])
def order_detail(request):
    data = request.data
    
    payment = PaymentDetail()
    payment.amount = data['toPay']
    payment.total_price = data['totalPrice']
    payment.total_discount = data['totalDiscount']
    payment.provider = data['payment']['payment']
    payment.address_to_send = data['address']['Address']
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
        product.productStaticPrice = product_obj.price
        product.productStaticDiscount = product_obj.discount.percentage
        product.save()

        

    
    return Response({"order_id":order.id}, status=status.HTTP_200_OK)



@api_view(['POST'])
def order_paid(request):
    data = request.data
    order = OrderDetail.objects.get(id=data['order_id'])
    payment_method = order.payment_method.id
    payment_method = PaymentDetail.objects.get(id=payment_method)
    payment_method.status = 'P'
    payment_method.save()
    
    return Response({"status":'successfully updated!'}, status=status.HTTP_200_OK)



def user_orders(request, id):
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')

    user_orders = OrderDetail.objects.filter(user=id)
    
    if startDate and endDate:
        start_date = timezone.datetime.strptime(startDate, '%Y-%m-%d').date()
        end_date = timezone.datetime.strptime(endDate, '%Y-%m-%d').date()
        end_date += timedelta(days=1)
        print(start_date,endDate)
        user_orders = user_orders.filter(created_at__range=(start_date, end_date))

    orders_data = [{'id': order.id, 'price': order.payment_method.amount, 'created_at': order.created_at} for order in user_orders]
    return JsonResponse({'orders': orders_data})




@api_view(['POST'])
def order_tracing(request):
    data = request.data
    print('data: ',data)
    order = OrderDetail.objects.get(id=data['order_id'])
    payment_method = order.payment_method.id
    print(payment_method)
    payment_method = PaymentDetail.objects.get(id=payment_method)
    print(payment_method)
    payment_method.tracing = data['order_tracing']
    payment_method.save()
    
    return Response({"status":'successfully updated!'}, status=status.HTTP_200_OK)
