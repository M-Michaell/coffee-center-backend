from django.db import models
# Create your models here.


class CoffeeType(models.Model):
    name = models.CharField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Caffeine(models.Model):
    name = models.CharField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Creator(models.Model):
    name = models.CharField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Origin(models.Model):
    name = models.CharField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class RoastingDegree(models.Model):
    name = models.CharField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Discount(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    percentage = models.FloatField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'



class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField(max_length=90)
    image = models.ImageField(upload_to='product/images')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=1)
    discount = models.ForeignKey(Discount, on_delete=models.SET_DEFAULT,default=0, related_name="product_discount")
    coffee_type = models.ForeignKey(CoffeeType, on_delete=models.CASCADE, related_name="product_coffe_type")
    caffeine = models.ForeignKey(Caffeine, on_delete=models.CASCADE, related_name="product_caffeine")
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name="product_creator")
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, related_name="product_origin")
    roasting_degree = models.ForeignKey(RoastingDegree, on_delete=models.CASCADE, related_name="product_roasting_degree")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    def price_after_discount(self):
        if self.discount.active:
            new_price=float(self.price)*((100-self.discount.percentage)/100)
        else:
            new_price=self.price
        return new_price

