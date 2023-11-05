from django.urls import path, include
from product.views import hello


urlpatterns = [
    path("hello/", hello),
    path("api/", include('product.api.urls'))

]