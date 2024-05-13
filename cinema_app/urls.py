from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('movie/', views.movie, name='movies'),
    path('cinema/', views.cinema, name='cinema'),
    path('', views.main, name='main page'),
    
]
