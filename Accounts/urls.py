from django.urls import path
from .views import *

app_name = 'account'

urlpatterns=[
    path('login/',loginPage,name='login'),
    path('register/',registerPage,name='register'),
    path('logout/',logoutPage,name='logout'),
    path('dashboard/',dashboardPage,name='dashboard'),
]