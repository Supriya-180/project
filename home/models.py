import email
from email.message import Message
from django.db import models
from django.forms import CharField

# Create your models here.
class contact(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Subject = models.CharField(max_length=200)
    Message = models.CharField(max_length=200)

class component(models.Model):
    Email = models.EmailField(max_length=200)
    Numbers = models.IntegerField()
    Option = models.BooleanField()
    Message = models.CharField(max_length=200)

    