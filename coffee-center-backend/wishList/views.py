from django.shortcuts import render
from .models import Wishlist,WishListItem,Product
from .serializers import WishlistSerializer,WishListItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'DELETE', 'POST'])
def wishlist_detail(request, id):

    # print(request.data)
    try:
        wishlist = Wishlist.objects.get(id=id)
    except Wishlist.DoesNotExist:
        return Response({'message': 'Wishlist not found'}, status=404)

    if request.method == 'GET':
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data)

    elif request.method == 'POST':

        product_id = request.data.get("id")
        product=Product.objects.get(id=product_id)


        wishlist_item, created = WishListItem.objects.get_or_create(
            wishlist=wishlist,
            product=product
        )
        serializer = WishListItemSerializer(wishlist_item)

        return Response({'message': 'Wishlist item created/updated via API', 'WishlistItem': serializer.data}, status=200)

    elif request.method == 'DELETE':
        print(request.data)
        try:
            product_id = request.data.get('id')  
            wishlist_item = WishListItem.objects.get(wishlist=wishlist, product__id=product_id)
        except WishListItem.DoesNotExist:
            return Response({'message': 'Wishlist item not found'}, status=404)

        wishlist_item.delete()
        return Response({'message': 'Wishlist item deleted via API'}, status=204)
