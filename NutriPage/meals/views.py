from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from NutriPage.meals.forms import MealsCreateForm
from NutriPage.meals.models import MealPlan, Comment


# Create your views here.

class CreateMealsView(CreateView):
    template_name = 'meals/create_meals.html'
    model = MealPlan
    form_class = MealsCreateForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class EditMealsView(UpdateView):
    model = MealPlan
    template_name = 'meals/edit_meals.html'
    form_class = MealsCreateForm
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_meals'] = MealPlan.objects.all()
        return context

class UserMealsView(ListView):
    model = MealPlan
    template_name = 'meals/user_meals.html'
    context_object_name = 'mealplans'
