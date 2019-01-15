from django.db import models

# Create your models here.


class Account(models.Model):
    owner = models.CharField(max_length=200, blank=True, default='')
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    creation_date = models.DateTimeField(auto_now_add=True)