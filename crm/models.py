from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom user model
class User(AbstractUser):
    role = models.CharField(max_length=20)

    class Meta:
        app_label = 'crm'


# Agent model
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def email(self):
        return self.user.email

    def __str__(self):
        return self.email