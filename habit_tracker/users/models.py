from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique = True)

class Profile(models.Model):
    user      = models.OneToOneField(User, on_delete=models.CASCADE)
    dark_mode = models.BooleanField(default=False)
    avatar    = models.ImageField(upload_to='profile_avatars/', blank=True, null=True)
    headline  = models.CharField(max_length=120, blank=True)
    bio       = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return self.user.username
