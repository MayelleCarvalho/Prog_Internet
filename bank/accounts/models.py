from django.db import models

# Create your models here.
from rest_framework import serializers


class Account(models.Model):
    owner = models.CharField(max_length=200, blank=True, default='')
    balance = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True)

