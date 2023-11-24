from rest_framework import serializers
from accounts.models import CustomUser, User_Address, User_Payment
from rest_framework.validators import UniqueValidator
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "username", "phone", "first_name", "last_name", "password", "is_staff")

class CustomUserSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  username = serializers.CharField(max_length=100,validators=[UniqueValidator(queryset=CustomUser.objects.all())])
  first_name = serializers.CharField(max_length=100)
  last_name = serializers.CharField(max_length=100, required=False)
  password = serializers.CharField(max_length=100)
  email = serializers.EmailField()
  phone = serializers.CharField(max_length=13, default=0)
  created_at = serializers.DateTimeField(read_only=True)
  modified_at = serializers.DateTimeField(read_only=True)

  def create(self, validate_data):
    return CustomUser.objects.create(**validate_data)
  
  def update(self, instance, validated_data):
    instance.username = validated_data.get('username')
    instance.first_name = validated_data.get('first_name')
    instance.last_name = validated_data.get('last_name')
    instance.password = validated_data.get('password')
    instance.email = validated_data.get('email')
    instance.phone = validated_data.get('phone')
    instance.save()
    return instance


class UserAddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=True)
    address_line1 = serializers.CharField(max_length=200)
    address_line2 = serializers.CharField(max_length=200, required=False, allow_blank=True)
    city = serializers.CharField(max_length=100, required=True)
    postal_code = serializers.CharField(max_length=100, required=True)
    country = serializers.CharField(max_length=100, required=True)
    telephone = serializers.CharField(max_length=12, required=False, allow_blank=True)
    mobile = serializers.CharField(max_length=12, required=False, allow_blank=True)

    def create(self, validate_data):
      return User_Address.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
      instance.address_line1 = validated_data.get('address_line1')
      instance.address_line2 = validated_data.get('address_line2')
      instance.city = validated_data.get('city')
      instance.postal_code = validated_data.get('postal_code')
      instance.country = validated_data.get('country')
      instance.telephone = validated_data.get('telephone')
      instance.mobile = validated_data.get('mobile')
      instance.save()
      return instance

class UserPaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=True)
    payment_type = serializers.CharField(max_length=200, required=True)
    provider = serializers.CharField(max_length=200, required=True)
    account_no = serializers.CharField(max_length=16, required=True)
    expiry = serializers.DateField(required=True)


    def create(self, validate_data):
      return User_Payment.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
      instance.payment_type = validated_data.get('payment_type')
      instance.provider = validated_data.get('provider')
      instance.account_no = validated_data.get('account_no')
      instance.expiry = validated_data.get('expiry')
      instance.save()
      return instance
