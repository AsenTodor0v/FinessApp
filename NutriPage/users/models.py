from django.contrib.auth import get_user_model
from django.db import models

from NutriPage.users.choises import ProfileRoleChoices, AdminRoleChoices


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

class Role(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=AdminRoleChoices.choices
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"