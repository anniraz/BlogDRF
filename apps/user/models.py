from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    last_action = models.DateTimeField(default=timezone.now, blank=True, null=True)
    is_online = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ("id",)


class UserImage(models.Model):
    ''' 
    user's  profile photo 
    '''
    user = models.ForeignKey(User, related_name='user_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/',blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    