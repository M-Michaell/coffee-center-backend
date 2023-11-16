from django.urls import path,include
from paypal_payment.views import successful, cancelled, home

urlpatterns = [
    path('',home,name='home'),
    path('successful',successful,name='successful'),
    path('cancelled',cancelled,name='cancelled'),
    path('paypal/',include('paypal.standard.ipn.urls')),
]