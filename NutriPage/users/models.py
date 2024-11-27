from idlelib.query import CustomRun

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from NutriPage.users.choises import ProfileRoleChoices
from NutriPage.users.managers import AppUserManager

CustomUser = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=20,
        choices=ProfileRoleChoices.choices,
        default=ProfileRoleChoices.USER,
    )
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"