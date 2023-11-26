from django.shortcuts import render
from . import views
from django.urls import path


# Views
urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('add_lead', views.add_lead, name='add_lead'),
]
