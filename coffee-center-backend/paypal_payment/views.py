from django.views.generic import FormView
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render


# class PaypalFormView(FormView):
#     template_name = 'paypal.html'
#     form_class = PayPalPaymentsForm

#     def get_initial(self):
#         return {
#             'business': 'sb-543tra28222103@business.example.com',
#             'amount': 50,
#             'currency_code': 'USD',
#             'item_name': 'Coffee1',
#             'invoice': 1234,
#             'notify_url': self.request.build_absolute_uri(reverse('paypal-ipn')),
#             'return_url': self.request.build_absolute_uri(reverse('paypal-return')),
#             'cancel_return': self.request.build_absolute_uri(reverse('paypal-cancel')),
#             'lc': 'EN',
#             'no_shipping': '1',
#         }
    

    
def home(request):
    paypalDict = {
        'business': 'sb-47azdz27300353@business.example.com',
        'amount': 50,
        'currency_code': 'EUR',
        'item_name': 'Coffee1',
        'invoice': 1234,
        'notify_url': request.build_absolute_uri(reverse('paypal-ipn')),
        'return_url': 'https://89be-102-185-0-52.ngrok-free.app',
        'cancel_return': request.build_absolute_uri(reverse('cancelled')),
        'lc': 'EN',
        # 'no_shipping': '1',
    }

    form = PayPalPaymentsForm(initial=paypalDict)
    context = {'form':form}
    return render(request,'paypal.html',context)

def successful(request):
    return render(request,'successful.html')

def cancelled(request):
    return render(request,'cancelled.html')
    