from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import *
from django.forms.models import inlineformset_factory

class AuhenticatePerson(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = '__all__'