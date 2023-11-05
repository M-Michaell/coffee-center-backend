from django.urls import path, re_path,include
from rest_framework.routers import DefaultRouter

# Import your viewset
from .views import ShoppingSessionViewSet

router = DefaultRouter()
router.register(r'shopping-sessions', ShoppingSessionViewSet)

urlpatterns = [
    # Add the URL patterns from the router
    re_path(r'^', include(router.urls)),
    
    # Add a custom URL for deleting a cart item
    path('shopping-sessions/<int:pk>/cart-items/<int:cart_item_pk>/', ShoppingSessionViewSet.as_view({'delete': 'destroy_cart_item'}), name='shopping-session-delete-cart-item'),
    path('shopping-sessions/<int:pk>/empty-cart-items/', ShoppingSessionViewSet.as_view({'post': 'empty_cart_items'}), name='shopping-session-empty-cart-items'),
    path('shopping-sessions/<int:pk>/delete-session/', ShoppingSessionViewSet.as_view({'delete': 'delete_session'}), name='shopping-session-delete-session')

]




