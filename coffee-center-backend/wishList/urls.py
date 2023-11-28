
from django.urls import path
from .views import wishlist_detail



urlpatterns = [

    path('wishlist_details/<int:id>', wishlist_detail, name='wishlist'),

]