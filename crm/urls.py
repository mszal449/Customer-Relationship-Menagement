from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.default, name='default'),
    path('home/', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('', include('leads.urls')),
    path('', include('event_calendar.urls'))
]


