from django.urls import path

from NutriPage.homepage.views import HomepageView, AboutUsView, ContactInformationView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactInformationView.as_view(), name='contact_information'),
]
