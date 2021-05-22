from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
class collect(models.Model):
    username = models.CharField(max_length=40,default="")
    Email = models.EmailField(default="Default@gmail.com")
    phone = models.CharField(max_length=10,default="")
    BloodSugar = models.CharField(max_length=4)
    BloodPressureSystolic = models.CharField(max_length=4,default="Default")
    BloodPressureDiastolic = models.CharField(max_length=4,default="Default")
    Pulse = models.CharField(max_length=3)
    SpO2 = models.CharField(max_length=3)
    Fever=models.BooleanField(default=False)
    Cough=models.BooleanField(default=False)
    Headache=models.BooleanField(default=False)
    InaCrowdedPlace=models.BooleanField(default=False)
    # the code below is for customizing objects name
    def __str__(self):
        return self.username


