from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from NutriPage.meals.forms import MealsCreateForm, MealsDeleteForm, MealsEditForm, CommentForm
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
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
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

class DeleteMealsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MealPlan
    template_name = 'meals/delete_meals.html'
    success_url = reverse_lazy('my-meals')  # Redirect to the user's meals page after deletion

    def test_func(self):
        mealplan = self.get_object()
        return self.request.user.profile == mealplan.author