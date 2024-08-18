from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    major=models.CharField(max_length=100)
    age=models.CharField(max_length=2)

def __str__(self):
    return f"{self.fullname}"

class ContactInfo(models.Model):
    fullname=models.CharField(max_length=100)
    emailaddress=models.CharField(max_length=100)
    messege=models.CharField(max_length=100)

def __str__(self):
    return f"{self.fullname}"


    
