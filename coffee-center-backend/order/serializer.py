from rest_framework import serializers
from order.models import OrderDetail, OrderItem, PaymentDetail
from product.models import Product
from accounts.models import CustomUser

class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    payment_method = PaymentDetailSerializer(read_only=True)
    payment_method_id = serializers.PrimaryKeyRelatedField(
        queryset=PaymentDetail.objects.all(),
        source='payment_method',
        write_only=True
    )
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = OrderDetail
        fields = '__all__'
