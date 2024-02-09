from django.shortcuts import render
import calendar
from calendar import HTMLCalendar


# Create your views here.
def calendar_view(request, year, month):
    month_number = list(calendar.month_name).index(month.capitalize())

    # Calendar instance
    cal = HTMLCalendar().formatmonth(year, int(month_number))
    
    return render(request, 'calendar.html',
                  {'year': year,
                   'month': month,
                   'month_number': month_number,
                   'cal': cal,
                   })
