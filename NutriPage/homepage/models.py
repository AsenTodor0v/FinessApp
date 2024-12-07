from django.db import models

# Create your models here.
class MissionStatement(models.Model):
    title = models.CharField(max_length=200, default="Our Mission")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactInformation(models.Model):
    contact_type = models.CharField(max_length=50)  # E.g., Phone, Email, Address
    details = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contact_type}: {self.details}"
