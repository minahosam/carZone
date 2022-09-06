from django.urls import path
from .views import *

app_name = 'cars'

urlpatterns = [
    path('cars/',carsPage,name='cars'),
    path('search/',searchPage,name='search'),
    path('<slug>/',carDetailsPage,name='carDetails'),
]