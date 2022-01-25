from django.db import models

class City(models.Model):
    Mahalle = models.CharField(max_length=50)
    Ilce = models.CharField(max_length=50)
    Numara = models.IntegerField()
    Ev = models.IntegerField(null=True)
    Tarih = models.DateField()