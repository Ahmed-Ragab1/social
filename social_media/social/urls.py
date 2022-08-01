from django.urls import path
from .views import home,aboutus



urlpatterns = [
    path('home/',home,name="home"),
    path('aboutus/',aboutus,name="aboutus"),
]