from django.contrib import admin
from .models import *
from django.utils.html import format_html


# Register your models here.
class car_images(admin.StackedInline):
    model = carImage
class AdminCar(admin.ModelAdmin):
    def Thumbnail(self,obj):
        return format_html("<img src='{}' width='40px' style='border-radius:50px;'/>".format(obj.car_photo.url))
    Thumbnail.short_description = 'car_image'
    list_display = ('id','Thumbnail','car_title','city','condition','year','price','is_featured')
    list_display_links = ('car_title','Thumbnail','price')
    list_editable = ['is_featured']
    search_fields = ('car_title','year','price')
    filter_fields = ('year','condition','price')
    inlines = (car_images,)
    prepopulated_fields={'slug':['car_title']}
admin.site.register(cars,AdminCar)