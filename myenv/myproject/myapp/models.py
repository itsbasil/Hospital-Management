from django.db import models

# Create your models here.

    #patient Registration
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
    
    #appointment 
class Appointment(models.Model):
    patientname=models.CharField(max_length=150)
    age=models.CharField(max_length=100)
    contactnum=models.CharField(max_length=100)
    doctorname=models.CharField(max_length=150,null=True,blank=True)
    date=models.CharField(max_length=150)
    address1=models.CharField(max_length=150)
    address2=models.CharField(max_length=150)
    address3=models.CharField(max_length=150)
    pin=models.CharField(max_length=150)

    def __str__(self):
        return self.patientname
    
    #doctor and patient login
class Login(models.Model):
      username=models.CharField(max_length=150)
      password=models.CharField(max_length=150)
      def __str__(self):
        return self.username
    
    #doctor Registration
class Doctor(models.Model):
    doctorname=models.CharField(max_length=150)
    dob=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    contactnum=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    password=models.CharField(max_length=150)
    password1=models.CharField(max_length=150)
    def __str__(self):
        return self.doctorname
    

   #contact 
class Contact(models.Model):
    patientname=models.CharField(max_length=150)
    number=models.CharField(max_length=100)
    description=models.CharField(max_length=150)
    
    def __str__(self):
        return self.patientname