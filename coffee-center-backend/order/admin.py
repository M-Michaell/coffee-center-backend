from django.contrib import admin
from order.models import OrderDetail, OrderItem, PaymentDetail
# Register your models here.




admin.site.register(OrderItem)
admin.site.register(OrderDetail)
admin.site.register(PaymentDetail)