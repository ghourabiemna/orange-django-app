from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.interface_resource , name='interface_resource'),
    path('reservation/', views.reservation_porte , name='reservation_porte'),
   ]
