from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    roll=models.IntegerField(max_length=50)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
