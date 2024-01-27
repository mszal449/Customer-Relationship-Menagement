from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from crm.models import Agent

# Lead model
class Lead(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = PhoneNumberField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'


