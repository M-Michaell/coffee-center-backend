# from rest_framework import serializers
# from order.models import OrderDetail,OrderItem,PaymentDetail






# class OrderDetailSerializer(serializers.ModelSerializer):
    
#     category_name = serializers.StringRelatedField(source="category", read_only=True)
#     owner_name = serializers.StringRelatedField(source="owner", read_only=True)


#     class Meta:
#         model = OrderDetail

#         fields = '__all__'




#     # def create(self, data):
#     #     book_name = data.get('name', None)
#     #     if book_name and Book.objects.filter(name=book_name).exists():
#     #         raise ValidationError("A book with this name already exists.")
#     #     return super().create(data)
