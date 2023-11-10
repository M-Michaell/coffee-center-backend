from django.urls import path, include
from product.views import hello


urlpatterns = [
    path("hello/", hello),
    path("", include('product.api.urls'))

]