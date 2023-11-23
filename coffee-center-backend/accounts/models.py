from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone ,password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(username=username, first_name=first_name, last_name=last_name, email=email, phone=phone ,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']

    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email
    

class User_Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="addresses")
    address_line1 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    telephone = models.CharField(max_length=12,null=True, blank=True)
    mobile = models.CharField(max_length=12,null=True, blank=True)

    @classmethod
    def get_all_addresses(cls):
        return cls.objects.all()
    
class User_Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="payments")
    payment_type = models.CharField(max_length=200) #another model
    provider = models.CharField(max_length=200) #another model
    account_no = models.CharField(max_length=16)
    expiry = models.DateField()

    @classmethod
    def get_all_payments(cls):
        return cls.objects.all()
    
# payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
# provider = models.ForeignKey(PaymentProvider, on_delete=models.CASCADE)
# class PaymentType(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)

# class PaymentProvider(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
