from django.db import models

# Create your models here.


class OrderDetail(models.Model):
    total = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    # foreign keys:
    user_id = models.IntegerField()

    #You can use fields order_items and payment_details in view and html






class OrderItem(models.Model):
    quantity = models.IntegerField()


    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    # foreign keys:
    order_id = models.ForeignKey(OrderDetail,null=True,blank=True,on_delete=models.CASCADE,related_name='order_items')
    product_id = models.IntegerField()





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




