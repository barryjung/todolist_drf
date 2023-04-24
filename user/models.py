from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, blank=True)
    genders = (("M", "male"), ("F", "female"),)
    gender = models.CharField(choices=genders, max_length=1, blank=True)
    age = models.IntegerField(blank=True, null=True)
    introduction = models.TextField(blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
