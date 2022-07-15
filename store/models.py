from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Gallery(models.Model):
    painting_name = models.CharField(max_length = 150)
    image1 = models.ImageField(upload_to='media/',blank=False)
    image2 = models.ImageField(upload_to='media/',blank=True)
    image3 = models.ImageField(upload_to='media/',blank=True)
    image4 = models.ImageField(upload_to='media/',blank=True)
    image5 = models.ImageField(upload_to='media/',blank=True)
    image6 = models.ImageField(upload_to='media/',blank=True)
    image7 = models.ImageField(upload_to='media/',blank=True)
    image8 = models.ImageField(upload_to='media/',blank=True)
    description = models.TextField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    

    

class Contact(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length = 11)
    gender = models.CharField(max_length = 150)
    address = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    name = models.CharField(max_length = 150)
    painting_name = models.CharField(max_length = 150)
    image1 = models.ImageField(upload_to='media/',blank=False)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name



class Order(models.Model):
    product = models.ForeignKey('Gallery', on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length = 150,default="")
    phone = models.CharField(max_length = 150,default="")
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    