from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view ,action
from rest_framework import viewsets
from .models import ShoppingSession, CartItem ,Product
from cart.serializers import ShoppingSessionSerializer, CartItemSerializer
from django.db.models import F, Sum

class ShoppingSessionViewSet(viewsets.ModelViewSet):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer

    def create(self, request, *args, **kwargs):
        cart_items_data = request.data.pop('cart_items', [])
        shopping_session = ShoppingSession.objects.create(**request.data)

        total = 0  # Initialize the total to zero

        for cart_item_data in cart_items_data:
            product_id = cart_item_data.get('product_id', None)
            if product_id:
                try:
                    product = Product.objects.get(id=product_id)
                    new_cart_item = CartItem.objects.create(session=shopping_session, product=product, quantity=cart_item_data.get('quantity', 0))
                    total += new_cart_item.product.price_after_discount() * new_cart_item.quantity
                except Product.DoesNotExist:
                    pass

        shopping_session.total = total  # Set the calculated total
        shopping_session.save()

        serializer = self.serializer_class(shopping_session)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        cart_items_data = request.data.get('cart_items', [])
        updated_cart_items = []

        total = instance.total  # Initialize the total to zero
        total = float(total)

        for cart_item_data in cart_items_data:
            product_id = cart_item_data.get('product_id', None)

            if product_id:
                try:
                    cart_item = CartItem.objects.get(session=instance, product=product_id)
                    
                    # Update the cart item details
                    cart_item.quantity += cart_item_data.get('quantity', cart_item.quantity)
                    cart_item.save()
                    updated_cart_items.append(cart_item)

                    # Calculate the total for this cart item
                    
                    print(cart_item.product.price_after_discount() )
                    print(cart_item.product.price_after_discount() )
                    total =float(total)+ float(cart_item.product.price_after_discount() * cart_item.quantity)
                except CartItem.DoesNotExist:
                    new_cart_item = CartItem.objects.create(session=instance, product_id=product_id, quantity=cart_item_data.get('quantity', 0))
                    updated_cart_items.append(new_cart_item)

                    # Calculate the total for this new cart item
                    total =float(total) + float(new_cart_item.product.price_after_discount() * new_cart_item.quantity)

        instance.user_id = request.data.get('user_id', instance.user_id)
        instance.total = total  # Set the calculated total
        instance.save()

        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def destroy_cart_item(self, request, *args, **kwargs):
        cart_item_id = kwargs.get('cart_item_pk')
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart_item.delete()

            # Recalculate the total after removing the cart item
            shopping_session = cart_item.session
            cart_items = CartItem.objects.filter(session=shopping_session)

            total = sum(cart_item.product.price_after_discount() * cart_item.quantity for cart_item in cart_items)

            shopping_session.total = total
            shopping_session.save()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({'detail': 'Cart item not found.'}, status=status.HTTP_404_NOT_FOUND)

        
    def delete_session(self, request, *args, **kwargs):
        session_id = kwargs.get('pk')
        try:
            shopping_session = ShoppingSession.objects.get(id=session_id)
            shopping_session.delete()
            return Response({'detail': 'Shopping session deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except ShoppingSession.DoesNotExist:
            return Response({'detail': 'Shopping session not found.'}, status=status.HTTP_404_NOT_FOUND)

        
    @action(detail=True, methods=['post'])
    def empty_cart_items(self, request, pk=None):
        # Get the shopping session
        shopping_session = self.get_object()

        # Calculate the total before emptying the cart items
        cart_items = CartItem.objects.filter(session=shopping_session)
        total = sum(cart_item.product.price_after_discount() * cart_item.quantity for cart_item in cart_items)

        # Delete all cart items associated with the shopping session
        CartItem.objects.filter(session=shopping_session).delete()

        # Update the total to zero
        shopping_session.total = 0
        shopping_session.save()

        return Response({'detail': 'Cart items have been emptied.', 'total': 0}, status=status.HTTP_200_OK)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer