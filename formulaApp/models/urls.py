from django.urls import path
from . import views

urlpatterns = [
    path('', views.circuit_list, name='circuit_list'),
]