from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    foursquare_id = models.IntegerField()
    foursquare_access_token = models.CharField(max_length=255)
    boxcar_email = models.EmailField(max_length=255)
    notifo_username = models.CharField(max_length=255)
