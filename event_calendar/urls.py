from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   path('calendar', views.CalendarView.as_view(), name='calendar'),
   path('event/new', views.event, name='event_new'),
   path('event/edit/<int:id>', views.event, name='event_edit'),
   path('event/delete/<int:id>', views.event_delete, name='event_delete')
]
