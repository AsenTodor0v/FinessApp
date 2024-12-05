from django import template

from NutriPage.meals.models import SavedMeals

register = template.Library()

@register.filter
def is_saved_by_user(mealplan, user):
    # Check if the meal plan has been saved by the given user
    return SavedMeals.objects.filter(mealplan=mealplan, user=user.profile).exists()
