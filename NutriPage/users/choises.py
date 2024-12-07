from django.db import models

class ProfileRoleChoices(models.TextChoices):
    USER = 'User', 'User'
    NUTRITIONIST = 'Nutritionist', 'Nutritionist'
    COACH = 'Coach', 'Coach'

class AdminRoleChoices(models.TextChoices):
    MODERATOR = 'Moderator', 'Moderator'  # Can manage users and moderate content
    STAFF = 'Staff', 'Staff'  # For staff-level admin privileges
    SUPERUSER = 'Superuser', 'Superuser' # Superusers with full system control