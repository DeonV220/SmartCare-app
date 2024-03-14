
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model

from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

    
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
         ('staff', 'Staff',),
         ('patient', 'Patient'),
         ('owner', 'Owner'), # this is the admin role
     ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='owner')

    
  

    def __str__(self):
        return self.username
    

# set permissions in data migration

# ownerprofile inherits super

# choices 
OCCUPATION =[
    ('nuse', 'Nurse'),
    ('doctor','Doctor'),
]

   


class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    birth_date = models.DateField()
    #password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# make person appear in the admin (user part)

   

class Prescriptions(models.Model):
    first_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    prescription_qty = models.IntegerField()
    description = models.CharField(max_length=255)
  

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.descriptiom}"

# prescription