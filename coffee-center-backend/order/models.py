from django.db import models
from accounts.models import CustomUser
from product.models import Product 
from product.softDeletionModel import SoftDeletionModel
from django.utils import timezone

def get_default_expired_at():
    return timezone.now() + timezone.timedelta(days=1)


class OrderDetail(SoftDeletionModel):
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE, related_name='order_details')
    payment_method = models.OneToOneField('PaymentDetail', null=True, blank=True, on_delete=models.CASCADE, related_name='order_detail')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    expired_at = models.DateTimeField(default=get_default_expired_at, null=True)

    def save(self, *args, **kwargs):
        if (self.pk and self.expired_at):
            self.expired_at += timezone.timedelta(days=1)  
        super().save(*args, **kwargs)  


    @classmethod
    def get_all_data(cls):
        return cls.objects.all()
    
    def delete(self):
        self.deleted=True
        self.soft_delete()
        return "done"






# class OrderItem(models.Model):
#     quantity = models.IntegerField()
#     order = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, related_name='order_items')
    
#     product = models.OneToOneField(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='order_item_details')

#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)

#     @classmethod
#     def get_all_data(cls):
#         return cls.objects.all()

class OrderItem(SoftDeletionModel):
    quantity = models.IntegerField()
    order = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='order_items_details')
    productStaticPrice = models.IntegerField(default=0,null=True,blank=True)
    productStaticDiscount = models.IntegerField(default=0,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_all_data(cls):
        return cls.objects.all()


class PaymentDetail(SoftDeletionModel):
    status_choices = [
        ('P', 'paid'),
        ('NP', 'unpaid')
    ]

    tracking_choices = [
        ('o', 'ordered'),
        ('s', 'shipped'),
        ('w', 'onTheWay'),
        ('d', 'delivered'),
    ]

    amount = models.IntegerField()
    total_discount = models.IntegerField()
    total_price = models.IntegerField()
    address_to_send = models.CharField(max_length=100)
    address_phone = models.CharField(max_length=12,null=True,default=None)
    provider = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=status_choices, default='NP')
    tracing = models.CharField(max_length=2, choices=tracking_choices, default='o')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



    @classmethod
    def get_all_data(cls):
        return cls.objects.all()




