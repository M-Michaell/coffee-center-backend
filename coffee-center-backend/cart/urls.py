from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShoppingSessionViewSet ,user_data

router = DefaultRouter()
router.register(r'shopping-sessions', ShoppingSessionViewSet, basename='shopping-session')

urlpatterns = [
    path('', include(router.urls)),
    path('cart/shopping-sessions/<int:pk>/delete_cart_item/', ShoppingSessionViewSet.as_view({'delete': 'delete_cart_item'}), name='shopping-session-delete-cart-item'),
    path('user-data/<int:pk>', user_data, name='api.userData'),
]