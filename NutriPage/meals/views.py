from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from NutriPage.meals.forms import MealsCreateForm, MealsDeleteForm, MealsEditForm, CommentForm
from NutriPage.meals.models import MealPlan


# Create your views here.

class CreateMealsView(CreateView):
    template_name = 'meals/create_meals.html'
    model = MealPlan
    form_class = MealsCreateForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class EditMealsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MealPlan
    template_name = 'meals/edit_meals.html'
    form_class = MealsEditForm
    success_url = reverse_lazy('my-meals')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def test_func(self):
        mealplan = self.get_object()
        return self.request.user.profile == mealplan.author

class UserMealsView(ListView):
    model = MealPlan
    template_name = 'meals/user_meals.html'
    context_object_name = 'mealplans'

class DetailMealView(DetailView):
    model = MealPlan
    template_name = 'meals/detail_meals.html'
    context_object_name = 'mealplan'

    def get_context_data(self, **kwargs):
        # Fetch the default context
        context = super().get_context_data(**kwargs)

        # Add the comment form to the context
        context['form'] = CommentForm()

        # Preprocess ingredients and steps for the template
        mealplan = self.get_object()  # Get the current MealPlan object

        # Split the ingredients and steps and remove any empty strings
        context['ingredients'] = [ingredient.strip() for ingredient in mealplan.ingredients.split(',') if ingredient.strip()] if mealplan.ingredients else []
        context['steps'] = [step.strip() for step in mealplan.steps.split('.') if step.strip()] if mealplan.steps else []

        return context

    def post(self, request, pk, *args, **kwargs):
        mealplan = get_object_or_404(MealPlan, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.mealplan = mealplan
            comment.author = request.user.username
            comment.save()
        return redirect('details-meal', pk=pk)

    def clean(self):
        if not self.ingredients:
            raise ValidationError("Please provide at least one ingredient.")
        if not self.steps:
            raise ValidationError("Please provide at least one step.")

class DeleteMealsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MealPlan
    template_name = 'meals/delete_meals.html'
    success_url = reverse_lazy('my-meals')  # Redirect to the user's meals page after deletion

    def test_func(self):
        mealplan = self.get_object()
        return self.request.user.profile == mealplan.author