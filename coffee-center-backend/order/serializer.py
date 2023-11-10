from rest_framework import serializers
from order.models import OrderDetail, OrderItem, PaymentDetail
from product.models import Product
from accounts.models import CustomUser
from product.api.serializers import ProductSerializer
from product.models import Product

class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    product_details = PaymentDetailSerializer(read_only=True)
    product_details_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='payment_method',
        write_only=True
    )

    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    payment_method = ProductSerializer(read_only=True)
    payment_method_id = serializers.PrimaryKeyRelatedField(
        queryset=PaymentDetail.objects.all(),
        source='payment_method',
        write_only=True
    )
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = OrderDetail
        fields = '__all__'
