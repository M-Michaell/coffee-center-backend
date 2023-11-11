from rest_framework import serializers
from .models import ShoppingSession, CartItem, CustomUser, Product
from product.api.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = ['id','product', 'quantity']


class ShoppingSessionSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)

    class Meta:
        model = ShoppingSession
        fields = '__all__'