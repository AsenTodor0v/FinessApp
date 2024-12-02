from django.urls import path

from NutriPage.homepage.views import HomepageView, AboutUsView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('about_us/', AboutUsView.as_view(), name='about-us'),
]
