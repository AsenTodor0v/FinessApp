from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('NutriPage.homepage.urls')),
    path('users/', include('NutriPage.users.urls')),
    path('meals/', include('NutriPage.meals.urls')),
]
