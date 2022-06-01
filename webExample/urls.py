import imp
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.index, name='home'),
    path('about/', views.about, name='about'), 
    path('users/', views.users, name='users'),
    path('add/', views.addUser, name='addUser'),
]
