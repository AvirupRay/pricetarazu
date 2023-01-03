from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class User(AbstractUser):
    username = None
    uemail = models.EmailField(null = True, unique = True)
    uphn = models.CharField(max_length = 11, null = True)

    objects = UserManager()

    USERNAME_FIELD = 'uemail'
    REQUIRED_FIELDS = []