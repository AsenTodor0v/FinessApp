from django.urls import path

from NutriPage.meals.views import CreateMealsView, EditMealsView, UserMealsView

urlpatterns = [
    path('create-meal/', CreateMealsView.as_view(), name='create-meal'),
    path('edit-meal/<int:pk>/', EditMealsView.as_view(), name='edit-meal'),
    path('my-meals/', UserMealsView.as_view(), name='my-meals'),
    path('details-meal/<int:pk>/', EditMealsView.as_view(), name='details-meal'),
]
