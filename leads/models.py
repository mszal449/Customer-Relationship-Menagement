from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom user model
class User(AbstractUser):
    role = models.CharField(max_length=20)


# Lead model
class Lead(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)


# Agent model
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
