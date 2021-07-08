from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    college = models.CharField(max_length=20, blank=True)    
    major = models.CharField(max_length=20, blank=True)