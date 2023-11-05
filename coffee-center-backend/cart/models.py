from django.db import models
from product.models import Product
from accounts.models import CustomUser

class ShoppingSession(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="shopping_sessions")
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Discount(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    discount_percent = models.FloatField()
    active = models.BooleanField(default=False)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_discounts")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
