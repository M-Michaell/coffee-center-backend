from django.urls import path
from accounts.api.views import userIndex, userPaymentIndex, userAddressIndex, customUser_resource, userPayment_resource, userAddress_resource

urlpatterns = [
  path('', userIndex, name='api.index'),
  path('<int:id>', customUser_resource, name='api.customUser_resource'),
  path('address/', userAddressIndex, name='api.address.index'),
  path('address/<int:id>', userAddress_resource, name='api.userAddress_resource'),
  path('payment/', userPaymentIndex, name='api.payment.index'),
  path('payment/<int:id>', userPayment_resource, name='api.userPayment_resource'),
]