from django.contrib import admin
from cart.models import ShoppingSession, CartItem

# Register your models here.
admin.site.register(ShoppingSession)
admin.site.register(CartItem)
