from django.db import models

class Users(models.Model):

    ADDRESS_CHOICE = (
        ('STREET', 'Street'),
        ('SUITE', 'Suite'),
        ('CITY','City'),
        ('ZIPCODE', 'Zipcode'),
    )
    name = models.CharField(max_length=100, blank=False, default='')
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=7, choices=ADDRESS_CHOICE, default='STREET')


class Comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    postId = models.ForeignKey(Users, on_delete=models.CASCADE)

