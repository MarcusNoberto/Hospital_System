from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.home_view,name=''),
    path('adminclick', views.admin_click_view),
    path('doctorclick', views.doctorclick_view),
    path('patientclick', views.patientclick_view),
]