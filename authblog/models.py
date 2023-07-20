from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    phonenumber =models.IntegerField()
    userimage= models.ImageField(null=True, blank=True, upload_to='image/profile')
    address= models.CharField(max_length=100)
    pincode= models.IntegerField()
    bio= models.TextField(max_length=1000)
    
    
    def __str__(self) :
        return str(self.user)
