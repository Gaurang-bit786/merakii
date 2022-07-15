from django.shortcuts import render, redirect
from django.http import HttpResponse
from collection.models import Image
from django.views import View
from accounts.models import *
from .models import  Gallery,Contact,Order
# Create your views here.

def home(request):
    if request.method=='POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        contact = Contact(name=name,email=email,phone=phone,gender=gender,address=address)
        contact.save()

        return redirect('home')
    else:
        gal = Gallery.objects.all().order_by('-date')
        img = Image.objects.all().order_by('-id')
        return render(request,'home.html',{'gallery':gal,'image':img})

def  store(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            print(request.POST.get('id'))
            gallery = Gallery.objects.all()
            return redirect('store')
        else:
            gallery = Gallery.objects.all()
        return render(request,'store.html',{'gallery':gallery})
    else:
        return redirect('loginuser')

class Cart(View):

    def get(self,request):
        if request.user.is_authenticated:
            gal = Gallery.objects.filter(id__in=request.session.get('cart').keys())
            print(gal)
            print(request.session.get('cart').keys())
            return render(request,'cart.html',{'product':gal})


class Store(View):

    def post(self,request):
        if request.user.is_authenticated:
            if request.method == 'POST':

                print(request.POST.get('id'))
                product = request.POST.get('id')
                remove = request.POST.get('remove')
                cart = request.session.get('cart')
                print(cart)
                if cart:
                    quantity = cart.get(product)
                    if quantity:
                        if remove:
                            if quantity<=1:
                                cart.pop(product)
                            else:
                                cart[product] = quantity - 1
                        else:
                                cart[product] = quantity + 1

                    else:
                        cart[product] = 1
                else:
                    cart = {}
                    cart[product] = 1
                request.session['cart'] = cart
                print(cart)
                return redirect('store')
        else:
            return redirect('loginuser')


    def get(self,request):
        if request.user.is_authenticated:
            cart =  request.session.get('cart')
            if not cart:
                request.session['cart'] = {}
            gallery = Gallery.objects.all()
            return render(request,'store.html',{'gallery':gallery})
        else:
            return redirect('loginuser')

class Checkout(View):
    def post(self,request):
        if request.user.is_authenticated:
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            customer = request.user.id
            cart = request.session.get('cart')
            product = Gallery.objects.filter(id__in=list(cart.keys()))
            print(address,phone,customer,product,cart)

            for product in product:
                order = Order(customer=User(id=customer),
                            product=product,
                            address=address,
                            price=product.price,
                            phone=phone,
                            quantity=cart.get(str(product.id)))
                order.save()
            request.session['cart'] = {}
            return redirect('cart')
        else:
            return redirect('loginuser')

    def placeorder(self):
        self.save()


class Order_view(View):
    def get(self,request):
        customer = request.user.id
        orders = Order.objects.filter(customer=customer).order_by('-date')
        print(str(orders))
        return render(request,'orders.html',{'order':orders})


