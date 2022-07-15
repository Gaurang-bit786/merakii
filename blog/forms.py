from django import  forms
from django.forms import widgets
from .models import *

class Comment(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment']
        widgets = {
            'comment' : forms.TextInput(attrs={'class':'form-control'})
        }