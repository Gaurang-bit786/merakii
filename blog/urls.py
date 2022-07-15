from django.urls import path
from .views import *

urlpatterns = [
    path('blog/',blog,name="blog"),
    path('blog/<int:id>/detail/',blog_detail,name="blog_detail"),
]