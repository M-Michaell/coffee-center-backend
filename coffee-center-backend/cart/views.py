# cart/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import ShoppingSession, CartItem, Product
from .serializers import ShoppingSessionSerializer, CartItemSerializer
from django.db import transaction
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
import json

class ShoppingSessionViewSet(viewsets.ModelViewSet):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer

    # @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    @action(detail=True, methods=['get'])
    def get_cart_data(self, request, pk=None):
        # user = request.user
        shopping_session = get_object_or_404(ShoppingSession, id=pk)

        cart_items = CartItem.objects.filter(session=shopping_session)
        serializer = CartItemSerializer(cart_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def empty_cart_items(self, request, pk=None):
        shopping_session = get_object_or_404(ShoppingSession, user=request.user, id=pk)

        with transaction.atomic():
            total = CartItem.objects.filter(session=shopping_session).aggregate(Sum('product__price_after_discount'))['product__price_after_discount__sum'] or 0

            CartItem.objects.filter(session=shopping_session).delete()

            shopping_session.total = 0
            shopping_session.save()

        return Response({'detail': 'Cart items have been emptied.', 'total': total}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        session_id = pk
        shopping_session = get_object_or_404(ShoppingSession, id=session_id)
        data=request.data
        if data:
            product_id = data['product']["id"]
            quantity = data['quantity'] or 1
            product = get_object_or_404(Product, id=product_id)

            with transaction.atomic():
                cart_item, created = CartItem.objects.get_or_create(
                    session=shopping_session,
                    product=product,
                    defaults={'quantity': quantity}
                )

                if not created:
                    # note this need som fix 
                    cart_item.quantity += quantity
                    cart_item.save()

                cart_items = CartItem.objects.filter(session=shopping_session)
                total = sum(cart_item.product.price_after_discount() * cart_item.quantity for cart_item in cart_items)

                shopping_session.total = total
                shopping_session.save()

                serializer = CartItemSerializer(cart_item)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"error": "No valid data in the request"}, status=status.HTTP_400_BAD_REQUEST)
        

    @action(detail=True, methods=['put'])
    def update_cart_item(self, request, pk=None):
        
        for data1 in request.data:

            if data1:
                data = json.loads(data1)
                session_id = pk
                product_id = data['product']["id"]
                quantity = data['quantity']
                shopping_session = get_object_or_404(ShoppingSession, id=session_id)
                cart_item = get_object_or_404(CartItem, session=shopping_session, product_id=product_id)

                with transaction.atomic():
                    cart_item.quantity = quantity
                    cart_item.save()

                    # Recalculate total
                    cart_items = CartItem.objects.filter(session=shopping_session)
                    total = sum(cart_item.product.price_after_discount() * cart_item.quantity for cart_item in cart_items)

                    shopping_session.total = total
                    shopping_session.save()

                    serializer = CartItemSerializer(cart_item)
                    return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"error": "Product data is missing in the request"}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['delete'])
    def delete_cart_item(self, request, pk=None):
        session_id = pk
        product=request.data["product"]
        product_id = json.loads(product)["id"]
        
        shopping_session = get_object_or_404(ShoppingSession, id=session_id)
        cart_item = get_object_or_404(CartItem, session=shopping_session, product_id=product_id)

        with transaction.atomic():
            cart_item.delete()

            # Recalculate total
            cart_items = CartItem.objects.filter(session=shopping_session)
            total = sum(cart_item.product.price_after_discount() * cart_item.quantity for cart_item in cart_items)

            shopping_session.total = total
            shopping_session.save()

        return Response({'detail': 'Cart item deleted successfully.', 'total': total}, status=status.HTTP_204_NO_CONTENT)
    


    