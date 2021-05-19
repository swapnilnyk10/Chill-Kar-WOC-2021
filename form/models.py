from django.db import models

# Create your models here.
class collect(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    Email = models.EmailField(default="Default@gmail.com")
    Key = models.CharField(max_length=5,default="1")
    phone = models.CharField(max_length=10)
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
        return self.firstname+ " "+self.lastname


