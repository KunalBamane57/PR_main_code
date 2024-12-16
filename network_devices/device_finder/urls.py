from django.urls import path
from . import views

urlpatterns = [
    path('', views.scan_devices, name='scan_devices'),
    path('next_page/', views.next_page, name='next_page'),
    path('attacks/', views.attacks_page, name='attacks_page'),
    path('attack1/', views.attack1, name='attack1'),
    path('attack2/', views.attack2, name='attack2'),
    path('attack3/', views.attack3, name='attack3'),
    path('attack4/', views.attack4, name='attack4'),
    path('inviteflood_attack/', views.inviteflood_attack, name='inviteflood_attack'),
]
