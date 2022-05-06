from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.home_view,name=''),
]