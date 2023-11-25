from django.db import models
from django.db.models import Avg
from accounts.models import CustomUser
from product.softDeletionModel import SoftDeletionModel



class CoffeeType(SoftDeletionModel):
    name = models.CharField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Caffeine(SoftDeletionModel):
    name = models.CharField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Creator(SoftDeletionModel):
    name = models.CharField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Origin(SoftDeletionModel):
    name = models.CharField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class RoastingDegree(SoftDeletionModel):
    name = models.CharField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Discount(SoftDeletionModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    percentage = models.FloatField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Product(SoftDeletionModel):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField(max_length=90)
    image = models.ImageField(upload_to='product/images')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=1)
    discount = models.ForeignKey(Discount, on_delete=models.SET_DEFAULT, default=0, related_name="product_discount", null=True)
    coffee_type = models.ForeignKey(CoffeeType, on_delete=models.CASCADE, related_name="product_coffee_type", null=True, default=None)
    caffeine = models.ForeignKey(Caffeine, on_delete=models.CASCADE, related_name="product_caffeine", null=True, default=None)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name="product_creator", null=True, default=None)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, related_name="product_origin", null=True, default=None)
    roasting_degree = models.ForeignKey(RoastingDegree, on_delete=models.CASCADE, related_name="product_roasting_degree", null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    def price_after_discount(self):
        if self.discount.active:
            new_price = float(self.price) * ((100 - self.discount.percentage) / 100)
        else:
            new_price = self.price
        return new_price
    
    @property
    def avg_rate(self):
        return Rate.objects.filter(product=self).aggregate(avg_rate=Avg('rate'))['avg_rate'] or ('0.0')


from django.core.validators import MinValueValidator, MaxValueValidator
class Rate(SoftDeletionModel):
    rate = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])   
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='rate')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rate')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} rated {self.product.name} with {self.rate}"
