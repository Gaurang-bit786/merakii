from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ['first_name','last_name','email','phone']
    list_filter = ['first_name','last_name','email','phone']

    search_fields =  ['first_name','last_name','email','phone']

admin.site.register(Client,ClientAdmin)