from django.contrib import admin
from accounts.models import CustomUser
from accounts.models import User_Address
from accounts.models import User_Payment
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(User_Address)
admin.site.register(User_Payment)