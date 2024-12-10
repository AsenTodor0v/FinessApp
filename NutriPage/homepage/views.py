from django.db.models import Q
from django.views.generic import ListView, TemplateView

from NutriPage.homepage.models import MissionStatement, ContactInformation
from NutriPage.meals.models import MealPlan


# Create your views here.
class HomepageView(ListView):
    template_name = 'index.html'
    model = MealPlan
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


class AboutUsView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mission_statement'] = MissionStatement.objects.first()
        context['contact_info'] = ContactInformation.objects.all()
        return context

class ContactInformationView(ListView):
    model = ContactInformation
    template_name = 'about_us.html'
    context_object_name = 'contact_info'
    queryset = ContactInformation.objects.all()