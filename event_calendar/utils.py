from calendar import HTMLCalendar
from event_calendar.models import Event


# Calendar implementation
class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # Format a day as a td and filters events by day
    def formatday(self, day, events):
        # Filter data by given day
        events_for_day = events.filter(start_time__day=day)

        # Create a html list of events
        data = ''
        for event in events_for_day:
            data += f'<li class="event-list-item"> {event.get_html_url} </li>'


        if day != 0:
            return f"<td><span class='date'>{day}</span><ul class='event-list'> {data} </ul>"
        return '<td></td>'

    # Formats week as a table tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # Formats month as a td
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'

        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}'
        return cal
