from django.urls import path
from . import views

urlpatterns = [
    path('', views.scan_devices, name='scan_devices'),
    path('next-page/', views.next_page, name='next_page'),
    path('attacks-page/', views.attacks_page, name='attacks_page'),
]
