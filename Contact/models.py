from django.db import models
from Cars.models import *
from django.contrib.auth.models import User

# Create your models here.
class contact(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    car_id = models.IntegerField(blank=True, null=True)
    message_title = models.CharField(max_length=300, blank=True, null=True)
    car_title = models.ForeignKey(cars,related_name='car',on_delete=models.CASCADE, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    user_id = models.IntegerField( blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)