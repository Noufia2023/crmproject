
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='gallery/', blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)
    about = models.TextField(blank=True)


class Lead(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=254)
    mobile_number = models.CharField(max_length=15)
    about = models.TextField()

    def __str__(self):
        return self.name
