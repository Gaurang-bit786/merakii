from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model):
    title =  models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
	#body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    snippet = models.CharField(max_length=255)
	
    def __str__(self):
        return self.title + ' | ' + str(self.author)


class PostImage(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='media/post/')
    
    def __str__(self):
        return self.name
        

class PostComment(models.Model):
    post = models.ForeignKey('Post', related_name='comment',  on_delete=models.CASCADE)
    name = models.CharField(max_length = 150,default=None)
    comment = models.CharField(max_length = 150)
    

    def __str__(self):
        return self.post.title + ' | ' + str(self.post.id)
    
    