from django.contrib import admin
from .models import Gallery, Contact, Cart,Order
from django.contrib.auth.models import Group
# Register your models here.



class GalleryAdmin(admin.ModelAdmin):

    list_display = ('painting_name','description','price','date')
    list_filter = ('painting_name','description','price','date')
    search_fields = ('painting_name','description','price','date')


class ContactAdmin(admin.ModelAdmin):

    list_display = ('name','email','gender','phone','address','date')
    list_filter = ('name','email','gender','phone','address','date')
    search_fields = ('name','email','gender','phone','address','date')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product','customer','price','quantity','date')
    list_filter = ('product','customer','price','quantity','date')
    search_fields = ['product','customer','price','quantity','date']
    ordering = ('product','customer','price','quantity','date')


admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.unregister(Group)

