from django.urls import path
from .views import home,aboutus
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('home/',home,name="home"),
    path('aboutus/',aboutus,name="aboutus"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)