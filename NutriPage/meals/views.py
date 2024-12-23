from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.db.models import Q

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

import httpx

from NutriPage.meals.forms import MealsCreateForm, MealsEditForm, CommentForm
from NutriPage.meals.models import MealPlan, SavedMeals, Comment
from NutriPage.meals.serializers import MealPlanSerializer, CommentSerializer

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
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        return queryset

class DetailMealView(DetailView):
    model = MealPlan
    template_name = 'meals/detail_meals.html'
    context_object_name = 'mealplan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        mealplan = self.get_object()

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
    success_url = reverse_lazy('my-meals')

    def test_func(self):
        mealplan = self.get_object()
        return self.request.user.profile == mealplan.author

@login_required
def save_mealplan(request, pk):
    mealplan = get_object_or_404(MealPlan, pk=pk)
    profile = request.user.profile  # Access the Profile instance
    SavedMeals.objects.get_or_create(user=profile, mealplan=mealplan)
    return redirect(reverse('details-meal', kwargs={'pk': mealplan.pk}))

@login_required
def saved_mealplans(request):
    saved = SavedMeals.objects.filter(user=request.user.profile).select_related('mealplan')
    paginator = Paginator(saved, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'meals/saved_mealplans.html', {'saved_mealplans': page_obj})

@login_required
def unsave_mealplan(request, pk):
    mealplan = get_object_or_404(MealPlan, pk=pk)

    # Get or 404 the SavedMeals object for the logged-in user and this meal plan
    saved_meal = get_object_or_404(SavedMeals, user=request.user.profile, mealplan=mealplan)

    saved_meal.delete()

    return redirect('saved_mealplans')


async def get_external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://externalapi.com/nutrition')
        return response.json()

class MealPlanListView(generics.ListCreateAPIView):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MealPlan.objects.all()

    def perform_create(self, serializer):
        """
        Create a new MealPlan instance and ensure it's saved correctly.
        """
        print("Validated Data:", serializer.validated_data)

        meal_plan = serializer.save()

        print("Meal Plan Created:", meal_plan)
        return meal_plan

class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom method to save the comment with the authenticated user.
        """
        # Automatically assign the authenticated user to the comment
        serializer.save(user=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class MealPlanDetailView(RetrieveAPIView):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer
    permission_classes = [IsAuthenticated]