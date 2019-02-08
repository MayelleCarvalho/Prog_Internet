from django.db import models

# Create your models here.

class Artigo(models.Model):
    artigo_id = models.AutoField(primary_key=True)
    artigo_titulo = models.CharField(max_length=250)
    artigo_corpo = models.TextField()