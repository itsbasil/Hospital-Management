from django.db import models

# Create your models here.
class Patient(models.Model):
    pname=models.CharField(max_length=150)
    dob=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    contactnum=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    password=models.CharField(max_length=150)
    password1=models.CharField(max_length=150)
    def __str__(self):
        return self.pname