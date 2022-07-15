from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('store/',Store.as_view(),name='store'),
    path('cart/',Cart.as_view(),name='cart'),
    path('checkout/',Checkout.as_view(),name='checkout'),
    path('order/',Order_view.as_view(),name='order'),
]

