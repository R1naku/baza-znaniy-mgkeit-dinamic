from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('place1', views.place1, name='place1'),
    path('place2', views.place2, name='place2'),
    path('place3', views.place3, name='place3'),
    path('place4', views.place4, name='place4')
]
