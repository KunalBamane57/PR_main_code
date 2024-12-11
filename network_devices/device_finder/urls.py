from django.urls import path
from . import views

urlpatterns = [
    path('', views.scan_devices, name='scan_devices'),
    path('next-page/', views.next_page, name='next_page'),
    path('attacks-page/', views.attacks_page, name='attacks_page'),
        path('attack1/', views.attack1, name='attack1'),  # URL for Attack 1
    path('attack2/', views.attack2, name='attack2'),  # URL for Attack 2
    path('attack3/', views.attack3, name='attack3'),  # URL for Attack 3
    path('attack4/', views.attack4, name='attack4'),  # URL for Attack 4
]
