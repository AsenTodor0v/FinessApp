from django import forms

from NutriPage.meals.models import MealPlan, Comment


class MealsCreateForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['title', 'description', 'ingredients', 'steps', 'picture']
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 3, 'placeholder': 'List ingredients separated by commas'}),
            'steps': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describe the preparation steps here'}),
        }

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