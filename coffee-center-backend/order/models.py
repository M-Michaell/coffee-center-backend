from django.db import models
from accounts.models import CustomUser
from product.models import Product

# Create your models here.


class OrderDetail(models.Model):
    total = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    # foreign keys:
    user_id = models.ForeignKey(CustomUser,null=True,blank=True,on_delete=models.CASCADE,related_name='order_details')
    







class OrderItem(models.Model):
    quantity = models.IntegerField()


    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    # foreign keys:
    order_id = models.ForeignKey(OrderDetail,null=True,blank=True,on_delete=models.CASCADE,related_name='order_items')
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_items')





class PaymentDetail(models.Model):

    status_choices = [
        ('P','paid'),
        ('NP','unpaid')
    ]

    amount = models.IntegerField()
    provider = models.CharField(max_length=50)
    status = models.CharField(max_length=2,choices=status_choices,default='NP')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # foreign keys:
    order_id = models.OneToOneField(OrderDetail,null=True,blank=True,on_delete=models.CASCADE,related_name='payment_details')




