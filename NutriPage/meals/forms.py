from django import forms

from NutriPage.meals.models import MealPlan, Comment


class MealsCreateForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['title', 'description', 'picture']

class MealsDeleteForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = '__all__'


class MealsEditForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['title', 'description', 'picture']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']