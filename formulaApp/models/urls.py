from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('circuit_list/', views.circuit_list, name='circuit_list'),
    path('constructor_list/', views.constructor_list, name='constructor_list'),
    path('driver_list/', views.driver_list, name='driver_list'),
]