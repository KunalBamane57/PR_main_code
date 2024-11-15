from django.urls import path
from . import views

urlpatterns = [
    path('', views.scan_devices, name='scan_devices'),
]
