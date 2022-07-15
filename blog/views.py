from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Post, PostComment
from .forms import *
# Create your views here.

def blog(request):
    post = Post.objects.all()
    return render(request,'blog.html',{'post':post})

def blog_detail(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        comment = request.POST['comment']
        name = request.POST['name']
        print(comment)
        add = PostComment.objects.create(post=post,name=name,comment=comment)
        add.save()
        return HttpResponseRedirect(f'/blog/{id}/detail/')
    else:
        comment = Comment()
        post = Post.objects.filter(id=id)
        return render(request,'post_detail.html',{'post':post})
