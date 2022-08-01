from django.urls import path
from .views import UserRegisterView,home



urlpatterns = [
    path('register/',UserRegisterView.as_view(),name="register"),
    path('home/',home,name="home"),
]