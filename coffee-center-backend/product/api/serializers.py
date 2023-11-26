from rest_framework import serializers
from product.models import Product, Creator, Caffeine, CoffeeType, RoastingDegree, Origin,Rate

class ProductSerializer(serializers.ModelSerializer):
    caffeine_name = serializers.CharField(source='caffeine.name', read_only=True)
    discount_percentage = serializers.CharField(source='discount.percentage', read_only=True)
    coffee_type = serializers.CharField(source='coffee_type.name', read_only=True)
    creator_name = serializers.CharField(source='creator.name', read_only=True)
    origin_name = serializers.CharField(source='origin.name', read_only=True)
    roasting_degree_name = serializers.CharField(source='roasting_degree.name', read_only=True)
    # image = serializers.FileField(max_length=1000000, allow_empty_file=False, write_only=True)
    avg_rate = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'desc', 'image', 'quantity', 'price' ,'caffeine_name', 'discount_percentage', 'coffee_type',
                  'creator_name', 'origin_name',"deleted" ,'roasting_degree_name', 'created_at', 'updated_at',"deleted_at","avg_rate")



        
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

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rate
        fields = "__all__"


