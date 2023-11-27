from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
