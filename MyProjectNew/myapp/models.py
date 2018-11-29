from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    email = models.CharField(max_length=60)

    def __str__(self):

        return self.title