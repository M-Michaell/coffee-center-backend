from django.contrib import admin
from cart.models import ShoppingSession, CartItem, Discount

# Register your models here.
admin.site.register(ShoppingSession)
admin.site.register(CartItem)
admin.site.register(Discount)