

from django.shortcuts import render
from django.views.generic import  ListView

from NutriPage.meals.models import MealPlan


# Create your views here.
class HomepageView(ListView):
    template_name = 'index.html'
    model = MealPlan
    context_object_name = 'mealplans'