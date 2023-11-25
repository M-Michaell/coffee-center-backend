from django.urls import path, include
from product.api import views


urlpatterns = [
    path('products/', views.product_list),
    path('product/<int:pk>/', views.product_detail),

    path('creators/', views.creator_list),
    path('creator/<int:pk>/', views.creator_detail),


    path('caffeines/', views.caffeine_list),
    path('caffeine/<int:pk>/', views.caffeine_detail),



    path('coffeeTypes/', views.coffeeType_list),
    path('coffeeType/<int:pk>/', views.coffeeType_detail),


    path('roastingDegrees/', views.roastingDegree_list),
    path('roastingDegree/<int:pk>/', views.roastingDegree_detail),

    path('origins/', views.origin_list),
    path('origin/<int:pk>/', views.origin_detail),

    path('search/', views.search, name='search'),
    path('create-rate/', views.create_rate, name='rate'),
    path('get_samilar/', views.get_samilar, name='samilar'),
    path('get_rating/', views.get_rating, name='product-rates'),
    path('get_rating/<int:pk>/', views.get_rating, name='product-rates'),



]