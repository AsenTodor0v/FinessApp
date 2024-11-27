from django.db import models

from NutriPage.users.models import Profile


# Create your models here.

class MealPlan(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='meal_pics', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    mealplan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.mealplan.title}"