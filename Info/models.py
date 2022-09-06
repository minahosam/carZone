from django.db import models

# Create your models here.
class Info(models.Model):
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField()
    work_days = models.CharField(max_length=200)
    work_hours = models.CharField(max_length=200)
    facebook_link = models.CharField(max_length=200)
    twitter_link = models.CharField(max_length=200)
    google_link = models.CharField(max_length=200)
    linkedin_link = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)