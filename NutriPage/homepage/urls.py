from django.urls import path

from NutriPage.homepage.views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),

]
