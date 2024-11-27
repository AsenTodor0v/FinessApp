from django import forms

from NutriPage.meals.models import MealPlan


class MealsCreateForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['title', 'description', 'picture']