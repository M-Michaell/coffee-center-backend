from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import CustomUser, User_Address, User_Payment
from accounts.api.serializers import CustomUserSerializer, UserAddressSerializer, UserPaymentSerializer
from accounts.models import Wishlist
from accounts.api.serializers import WishlistSerializer


@api_view(['GET', 'POST'])
def userIndex(request):
    if request.method == 'POST':
        customUser = CustomUserSerializer(data=request.data)
        if customUser.is_valid():
            customUser.save()
            return Response({'message': 'User added via API', 'User': customUser.data}, status=201)
        return Response(customUser.errors, status=400)

    elif request.method == 'GET':
        customUsers = CustomUser.objects.get_all_users()
        serialized_users = CustomUserSerializer(customUsers, many=True)
        return Response({'message': 'Users data received via API', 'Users': serialized_users.data}, status=200)

@api_view(['GET', 'DELETE', 'PUT'])
def customUser_resource(request, id):
  customUser = CustomUser.objects.filter(id=id).first()

  if request.method == 'GET':
    serialized_user = CustomUserSerializer(customUser)
    return Response({'message': 'User data received via api', 'User': serialized_user.data}, status=200)
  
  elif request.method == 'PUT':
    serialized_user = CustomUserSerializer(instance=customUser, data=request.data)
    if serialized_user.is_valid():
      serialized_user.save()
      return Response({'message': 'User updated via api', 'User': serialized_user.data}, status=201)
    return Response(serialized_user.errors, status=400)
  
  elif request.method == 'DELETE':
    customUser.delete()
    return Response({'message': 'User deleted via api'}, status= 204)
  



@api_view(['GET', 'POST'])
def userAddressIndex(request, user_id):
  if request.method == 'POST':
    userAddress = UserAddressSerializer(data=request.data)
    if userAddress.is_valid():
      userAddress.save()
      return Response({'message': 'User added via api', 'User':userAddress.data}, status=201)
    return Response(userAddress.errors, status=400)
  
  elif request.method == 'GET':
    userAddresses = User_Address.objects.filter(user_id=user_id)    
    serialized_users = UserAddressSerializer(userAddresses, many = True)
    return Response({'message': 'Users data received via apiy', 'Users': serialized_users.data}, status=200)
  
@api_view(['GET', 'DELETE', 'PUT'])
def userAddress_resource(request, user_id, id):
  userAddress = User_Address.objects.filter(id=id, user_id=user_id).first()
  if request.method == 'GET':
    serialized_user = UserAddressSerializer(userAddress)
    return Response({'message': 'User data received via api', 'User': serialized_user.data}, status=200)
  
  elif request.method == 'PUT':
    serialized_user = UserAddressSerializer(instance=userAddress, data=request.data)
    if serialized_user.is_valid():
      serialized_user.save()
      return Response({'message': 'User updated via api', 'User': serialized_user.data}, status=201)
    return Response(serialized_user.errors, status=400)
  
  elif request.method == 'DELETE':
    userAddress.delete()
    return Response({'message': 'User deleted via api'}, status= 204)
  


@api_view(['GET', 'POST'])
def userPaymentIndex(request):
  if request.method == 'POST':
    userPayment = UserPaymentSerializer(data=request.data)
    if userPayment.is_valid():
      userPayment.save()
      return Response({'message': 'User added via api', 'User':userPayment.data}, status=201)
    return Response(userPayment.errors, status=400)
  
  elif request.method == 'GET':
    userPayments = User_Payment.get_all_payments()
    serialized_users = UserPaymentSerializer(userPayments, many = True)
    return Response({'message': 'Users data received via apiy', 'Users': serialized_users.data}, status=200)
  
@api_view(['GET', 'DELETE', 'PUT'])
def userPayment_resource(request, id):
  userPayment = User_Payment.objects.filter(id=id).first()

  if request.method == 'GET':
    serialized_user = UserPaymentSerializer(userPayment)
    return Response({'message': 'User data received via api', 'User': serialized_user.data}, status=200)
  
  elif request.method == 'PUT':
    serialized_user = UserPaymentSerializer(instance=userPayment, data=request.data)
    if serialized_user.is_valid():
      serialized_user.save()
      return Response({'message': 'User updated via api', 'User': serialized_user.data}, status=201)
    return Response(serialized_user.errors, status=400)
  
  elif request.method == 'DELETE':
    userPayment.delete()
    return Response({'message': 'User deleted via api'}, status= 204)
  
@api_view(['GET', 'POST'])
def wishlist_index(request):
    if request.method == 'POST':
        wishlist_serializer = WishlistSerializer(data=request.data)
        if wishlist_serializer.is_valid():
            wishlist_serializer.save()
            return Response({'message': 'Wishlist item added via API', 'Wishlist': wishlist_serializer.data}, status=201)
        return Response(wishlist_serializer.errors, status=400)

    elif request.method == 'GET':
        wishlists = Wishlist.objects.all()
        serialized_wishlists = WishlistSerializer(wishlists, many=True)
        return Response({'message': 'Wishlist data received via API', 'Wishlists': serialized_wishlists.data}, status=200)

@api_view(['GET', 'DELETE', 'PUT'])
def wishlist_detail(request, id):
    wishlist_item = Wishlist.objects.filter(id=id).first()

    if request.method == 'GET':
        serialized_wishlist_item = WishlistSerializer(wishlist_item)
        return Response({'message': 'Wishlist item data received via API', 'WishlistItem': serialized_wishlist_item.data}, status=200)

    elif request.method == 'PUT':
        serialized_wishlist_item = WishlistSerializer(instance=wishlist_item, data=request.data)
        if serialized_wishlist_item.is_valid():
            serialized_wishlist_item.save()
            return Response({'message': 'Wishlist item updated via API', 'WishlistItem': serialized_wishlist_item.data}, status=201)
        return Response(serialized_wishlist_item.errors, status=400)

    elif request.method == 'DELETE':
        wishlist_item.delete()
        return Response({'message': 'Wishlist item deleted via API'}, status=204)
    