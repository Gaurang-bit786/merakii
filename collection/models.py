from django.db import models

# Create your models here.

class MyCollection(models.Model):
    name = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.ForeignKey('MyCollection',related_name='collection', on_delete=models.CASCADE)
    collection = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name.name
    
    