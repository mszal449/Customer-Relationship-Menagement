from django.db import models
from django.urls import reverse


# Event model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title}</a>'

