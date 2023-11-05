from rest_framework import serializers
from product.models import Product, Creator, Caffeine, CoffeeType, RoastingDegree, Origin

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = '__all__'
        
class CaffeineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caffeine
        fields = '__all__'



class CoffeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeType
        fields = '__all__'

class RoastingDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoastingDegree
        fields = '__all__'


class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = '__all__'
