from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name=  models.CharField(max_length=100)
    last_name=  models.CharField(max_length=100, null=True)
    password= models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class User_Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="addresses") 
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, null=True, blank = True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    telephone = models.CharField(max_length=12,null=True, blank=True)
    mobile = models.CharField(max_length=12,null=True, blank=True)

class User_Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="payments")
    payment_type = models.CharField(max_length=200) #another model
    provider = models.CharField(max_length=200) #another model
    account_no = models.CharField(max_length=16)
    expiry = models.DateField()