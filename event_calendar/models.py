from django.db import models


# Event model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

