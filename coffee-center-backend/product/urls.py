from django.urls import path, include
from product.views import hello
from back_end import settings
from django.conf.urls.static import static

urlpatterns = [
    path("hello/", hello),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)