from . import views
from django.urls import path


# Views
urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('leads', views.leads, name='leads'),
    path('add_lead', views.add_lead, name='add_lead'),
    path('lead/<int:pk>', views.lead, name='lead'),
    path('update_lead/<int:pk>', views.update_lead, name='update_lead'),
    path('delete_lead/<int:pk>', views.delete_lead, name='delete_lead')
]

