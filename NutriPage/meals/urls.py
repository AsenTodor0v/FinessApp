from django.urls import path

from NutriPage.meals import views
from NutriPage.meals.views import CreateMealsView, EditMealsView, UserMealsView, DetailMealView, DeleteMealsView

urlpatterns = [
    path('create-meal/', CreateMealsView.as_view(), name='create-meal'),
    path('edit-meal/<int:pk>/', EditMealsView.as_view(), name='edit-meal'),
    path('my-meals/', UserMealsView.as_view(), name='my-meals'),
    path('details-meal/<int:pk>/', DetailMealView.as_view(), name='details-meal'),
    path('delete-meal/<int:pk>/delete/', DeleteMealsView.as_view(), name='delete-meal'),
    path('post/<int:pk>/save/', views.save_mealplan, name='save_mealplan'),
    path('saved-mealplans/', views.saved_mealplans, name='saved_mealplans'),
    path('post/<int:pk>/unsave/', views.unsave_mealplan, name='unsave_mealplan'),
    path('api/mealplans/', views.MealPlanListView.as_view(), name='api-mealplan-list'),
    path('api/mealplans/<int:pk>/', views.MealPlanDetailView.as_view(), name='api-mealplan-detail'),
    path('api/comments/', views.CommentListView.as_view(), name='api-comment-list'),
    path('api/comments/<int:pk>/', views.CommentDetailView.as_view(), name='api-comment-detail'),

]
