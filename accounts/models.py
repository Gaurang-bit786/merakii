from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User,related_name='client', on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='media/profile_pic/',blank=True)
    first_name = models.CharField(max_length=150,blank=True)
    last_name = models.CharField(max_length=150,blank=True)
    email = models.EmailField(max_length=250,blank=True)
    phone = models.CharField(max_length=12,blank=True)
    address = models.TextField(blank=True)
    pincode = models.CharField(max_length=6,blank=True)
    
    def __str__(self):
        return self.first_name
    
    
