from django.urls import path
from . import views


urlpatterns = [
   path('calendar/<int:year>/<str:month>', views.calendar_view, name='calendar_view')
]
