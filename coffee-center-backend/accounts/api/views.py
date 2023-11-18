from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import CustomUser, User_Address, User_Payment
from accounts.api.serializers import CustomUserSerializer, UserAddressSerializer, UserPaymentSerializer

@api_view(['GET', 'POST'])
def userIndex(request):
  if request.method == 'POST':
    customUser = CustomUserSerializer(data=request.data)
    if customUser.is_valid():
      customUser.save()
      return Response({'message': 'User added via api', 'User':customUser.data}, status=201)
    return Response(customUser.errors, status=400)
  
  elif request.method == 'GET':
    customUsers = CustomUser.get_all_users()
    serialized_users = CustomUserSerializer(customUsers, many = True)
    return Response({'message': 'Users data received via apiy', 'Users': serialized_users.data}, status=200)
  
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
def userAddressIndex(request):
  if request.method == 'POST':
    userAddress = UserAddressSerializer(data=request.data)
    if userAddress.is_valid():
      userAddress.save()
      return Response({'message': 'User added via api', 'User':userAddress.data}, status=201)
    return Response(userAddress.errors, status=400)
  
  elif request.method == 'GET':
    userAddresses = User_Address.get_all_addresses()
    serialized_users = UserAddressSerializer(userAddresses, many = True)
    return Response({'message': 'Users data received via apiy', 'Users': serialized_users.data}, status=200)
  
@api_view(['GET', 'DELETE', 'PUT'])
def userAddress_resource(request, id):
  userAddress = User_Address.objects.filter(id=id).first()

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
  
