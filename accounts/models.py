from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import Office


class User(AbstractUser):
    offices = models.ManyToManyField(Office)
