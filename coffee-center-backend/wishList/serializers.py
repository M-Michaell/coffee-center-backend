
from .models import Wishlist
from rest_framework import serializers

from .models import CustomUser,Product,Wishlist,WishListItem
from product.api.serializers import ProductSerializer


class WishListItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = WishListItem
        fields = ['product']


class WishlistSerializer(serializers.ModelSerializer):
    wishlist_item = WishListItemSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = "__all__"
