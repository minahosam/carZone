from django.db import models

# Create your models here.
class TeamMember(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='team/')
    facebook_link = models.URLField(max_length=500)
    google_link = models.URLField(max_length=500)
    twitter_link = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name