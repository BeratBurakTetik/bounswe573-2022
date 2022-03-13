from django.db import models

# Create your models here.
from copyreg import constructor
from pyexpat import model
from statistics import mode

class Driver(models.Model):
    driverRef = models.CharField(max_length=50, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    code = models.CharField(max_length=10, null=True, blank=True)
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dob = models.DateField()
    nationality = models.CharField(max_length=40)
    url = models.CharField(max_length=100)

class Constructor(models.Model):
    constructorRef = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    url = models.CharField(max_length=100)

class Circuit(models.Model):
    circuitRef = models.CharField(max_length=50 ,null=True)
    name = models.CharField(max_length=80)
    location = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    lat = models.DecimalField(decimal_places=5 , max_digits=10,null=True, blank=True)
    lng = models.DecimalField(decimal_places=5 , max_digits=10,null=True, blank=True)
    alt = models.DecimalField(decimal_places=5 , max_digits=10,null=True, blank=True)
    url = models.CharField(max_length=100)


