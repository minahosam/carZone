from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class  TeamAdmin(admin.ModelAdmin):
    def Thumbnail(self,obj):
        return format_html("<img src='{}' width='40px' style='border-radius:50px;'/>".format(obj.photo.url))
    list_display=('id','Thumbnail','first_name','last_name','designation','created_at')
    list_display_links=('id','Thumbnail','first_name')
    search_fields = ('first_name','last_name','designation')
    list_filter = ('designation',)
admin.site.register(TeamMember,TeamAdmin)