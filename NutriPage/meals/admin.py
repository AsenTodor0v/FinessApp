from django.contrib import admin

from NutriPage.meals.models import MealPlan, Comment


# Register your models here.
@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('mealplan', 'author', 'created_at')
