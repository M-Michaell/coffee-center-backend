from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Wishlist)
admin.site.register(models.WishListItem)