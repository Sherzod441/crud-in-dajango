import imp
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.index, name='home'),
    path('about/', views.about, name='about'), 
    path('users/', views.users, name='users'),
    path('add/', views.addUser, name='addUser'),
    path('users/<int:pk>/update', views.updateUserView.as_view(), name='updateUser'),
    path('users/<int:pk>/delete', views.deleteUserView.as_view(), name='deleteUser'),
]
