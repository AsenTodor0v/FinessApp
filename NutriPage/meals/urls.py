from django.urls import path

from NutriPage.meals.views import CreateMealsView

urlpatterns = [
    path('create-meal/', CreateMealsView.as_view(), name='create-meal'),

]
