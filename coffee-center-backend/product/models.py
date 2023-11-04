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


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='product/images')
    quantity = models.IntegerField()
    coffee_type = models.ForeignKey(CoffeeType, on_delete=models.CASCADE)
    caffeine = models.ForeignKey(Caffeine, on_delete=models.CASCADE)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    roasting_degree = models.ForeignKey(RoastingDegree, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


