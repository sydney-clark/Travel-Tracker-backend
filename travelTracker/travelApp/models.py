from django.db import models

# Create your models here.
class Travel(models.Model):
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    date = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=100)
    def __str__(self): return self.location
    def __str__(self): return self.type
    def __str__(self): return self.date
    def __str__(self): return self.address
    def __str__(self): return self.contact

class Marker(models.Model):
    address = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    def __str__(self): return self.address
    def __str__(self): return self.latitude
    def __str__(self): return self.longitude