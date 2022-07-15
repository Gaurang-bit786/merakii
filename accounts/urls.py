from django.urls import path 
from .views import *

urlpatterns = [
    path('login/',login_user,name='loginuser'),
    path('logout/',logout_user,name='logoutuser'),
    path('sign-up/',register,name='signup'),
    path('dashboard/',dashboard,name='dashboard'),
]