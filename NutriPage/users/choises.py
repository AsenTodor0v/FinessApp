from django.db import models

class ProfileRoleChoices(models.TextChoices):
    NUTRITIONIST = 'Nutritionist', 'Nutritionist'
    COUCH = 'Couch', 'Couch'
    USER = 'User', 'User'

class AdminRoleChoices(models.TextChoices):
    STAFF = 'Staff', 'Staff'
    SUPERUSER = 'Superuser', 'Superuser'