from django.urls import path
from .views import *

app_name = 'main'


urlpatterns = [
    path('',HomePage,name='home'),
    path('about/',aboutPage,name='about'),
    path('contact/',contactPage,name='contact'),
    path('services/',servicesPage,name='services'),
]