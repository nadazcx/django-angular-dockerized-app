from django.db import models
from django.contrib.auth.models import AbstractUser



class Employee(models.Model): 
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
