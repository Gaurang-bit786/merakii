from django.shortcuts import render
from .models import *


def gallery(request):
    collect = MyCollection.objects.all()
    return render(request,'gallery.html',{'image':collect})