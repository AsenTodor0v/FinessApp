from django.db import models

from NutriPage.users.models import Profile


# Create your models here.

class MealPlan(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='meal_pics', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ingredients = models.TextField(help_text="List the ingredients of the recipe separated by commas.")
    steps = models.TextField(help_text="List the preparation steps of the recipe.")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def get_ingredient_list(self):
        """Return a list of ingredients split by commas."""
        return [ingredient.strip() for ingredient in self.ingredients.split(',')]

    def get_step_list(self):
        """Return a list of preparation steps split by periods."""
        return [step.strip() for step in self.steps.split('.')]

    def __str__(self):
        return self.title

class Comment(models.Model):
    mealplan = models.ForeignKey(MealPlan,related_name="comments",on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author}"