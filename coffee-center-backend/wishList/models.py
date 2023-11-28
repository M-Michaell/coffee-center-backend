
from django.db import models
from accounts.models import CustomUser
from product.models import Product




class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="wishlist")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user}'s Wishlist"


class WishListItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name="wishlist_item")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlist_item")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
