from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   path(r'calendar', views.CalendarView.as_view(), name='calendar')
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)