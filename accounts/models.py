from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=250, unique=True)

    def __str__(self):
        return self.username