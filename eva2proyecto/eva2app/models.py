from django.db import models

class DBproyecto(models.Model):
    nombre = models.CharField(max_length=10)
    edad = models.IntegerField()    

# Create your models here.
