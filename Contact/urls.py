from django.urls import path
from .views import *

app_name = 'contact'

urlpatterns = [
    path('inquiry/',inquiry,name='inquiry')
]