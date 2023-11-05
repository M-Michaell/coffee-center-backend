from rest_framework import serializers
from .models import ShoppingSession, CartItem,CustomUser



from .models import Product  # Import your Product model


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class ShoppingSessionSerializer(serializers.ModelSerializer):
    # Replace 'user' and 'product' fields with 'user_id' and 'product_id'
    user_id= serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),  write_only=True)
    product_id= serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingSession
        fields = '__all__'
