from django.contrib import admin
from .models import *

# Register your models here.

class contactAdmin(admin.ModelAdmin):
    list_display= ('id','first_name','last_name','email','car_title','city','created_at')
    list_display_links= ('id','first_name','last_name')
    search_fields= ('id','first_name','last_name','email','car_title')
    list_per_page=20

admin.site.register(contact,contactAdmin)