from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('place1', views.place1, name='place1'),
    path('place2', views.place2, name='place2'),
    path('place3', views.place3, name='place3'),
    path('place4', views.place4, name='place4'),
    path('k1p1', views.k1p1, name='k1p1'),
    path('k2p1', views.k2p1, name='k2p1'),
    path('k3p1', views.k3p1, name='k3p1'),
    path('k4p1', views.k4p1, name='k4p1'),
    path('k1p2', views.k1p2, name='k1p2'),
    path('k2p2', views.k2p2, name='k2p2'),
    path('k3p2', views.k3p2, name='k3p2'),
    path('k4p2', views.k4p2, name='k4p2'),
    path('k1p3', views.k1p3, name='k1p3'),
    path('k2p3', views.k2p3, name='k2p3'),
    path('k3p3', views.k3p3, name='k3p3'),
    path('k4p3', views.k4p3, name='k4p3'),
    path('k1p4', views.k1p4, name='k1p4'),
    path('k2p4', views.k2p4, name='k2p4'),
    path('k3p4', views.k3p4, name='k3p4'),
    path('k4p4', views.k4p4, name='k4p4'),
]
