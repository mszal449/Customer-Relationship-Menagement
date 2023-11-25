from django.shortcuts import render
from . import views
from django.urls import path


# Views
urlpatterns = [
    path('', views.home, name='home'),
]