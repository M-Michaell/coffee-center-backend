from django.db import models
from accounts.models import CustomUser
from product.models import Product

class OrderDetail(models.Model):
    total = models.IntegerField()
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE, related_name='order_details')
    payment_method = models.OneToOneField('PaymentDetail', null=True, blank=True, on_delete=models.CASCADE, related_name='order_detail')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_all_data(cls):
        return cls.objects.all()

class OrderItem(models.Model):
    quantity = models.IntegerField()
    order = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_all_data(cls):
        return cls.objects.all()

class PaymentDetail(models.Model):
    status_choices = [
        ('P', 'paid'),
        ('NP', 'unpaid')
    ]
    amount = models.IntegerField()
    provider = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=status_choices, default='NP')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_all_data(cls):
        return cls.objects.all()
