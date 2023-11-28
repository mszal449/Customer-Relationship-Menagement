from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Custom user model
class User(AbstractUser):
    role = models.CharField(max_length=20)

    class Meta:
        app_label = 'leads'


# Lead model
class Lead(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = PhoneNumberField()
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'


# Agent model
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
