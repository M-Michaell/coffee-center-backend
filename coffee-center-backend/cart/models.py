from django.db import models
from accounts.models import CustomUser
from product.models import Product
from accounts.models import CustomUser
from product.softDeletionModel import SoftDeletionModel

class ShoppingSession(SoftDeletionModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="shopping_sessions")
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class CartItem(SoftDeletionModel):
    session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
