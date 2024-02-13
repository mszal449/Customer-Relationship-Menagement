import calendar

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import *
from datetime import datetime, date, timedelta
from .utils import Calendar
from django.utils.safestring import mark_safe
from .forms import EventForm


# Override generic list view to display calendar
class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    # Add functionality to create a calendar to the get_context_data method
    def get_context_data(self, **kwargs):
        # Use default functionality to get context
        context = super().get_context_data(**kwargs)

        # Use today's date for the calendar if it is not provided
        data = get_date(self.request.GET.get('month', None))

        # Instantiate Calendar class with the given date
        cal = Calendar(data.year, data.month)


        # Add month navigation to context
        month = get_date(self.request.GET.get('month', None))
        context['prev_month'] = previous_month(month)
        context['next_month'] = next_month(month)

        # Retrieve calendar as a HTML table
        html_cal = cal.formatmonth(withyear=True)

        # Add calendar to context
        context['calendar'] = mark_safe(html_cal)


        return context


# Event view
def event(request, id=None):
    instance = Event()
    if id:
        instance = get_object_or_404(Event, pk=id)
    else:
        instance = Event()

    if request.method == 'POST':
        form = EventForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('calendar'))
    else:
        form = EventForm(instance=instance)

    return render(request, 'event_form.html', {'form': form, 'id': id})


def event_delete(request, id):
    event = get_object_or_404(Event, pk=id)
    if event:
        event.delete()
    return HttpResponseRedirect(reverse('calendar'))


# Retrieve a date from a string or return today's date
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


# Return date string with next month
def next_month(date):
    # Calculate first day of the next month
    days_in_month = calendar.monthrange(date.year, date.month)[1]
    last = date.replace(day=days_in_month)
    next = last + timedelta(days=1)

    # Create a new date string with new month
    month = 'month=' + str(next.year) + '-' + str(next.month)
    return month


# Return date string with previous month
def previous_month(date):
    # Calculate previous month
    first = date.replace(day=1)
    prev = first - timedelta(days=1)

    # Create a new date string with new month
    month = 'month=' + str(prev.year) + '-' + str(prev.month)
    return month