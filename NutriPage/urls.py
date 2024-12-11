from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('NutriPage.homepage.urls')),
    path('users/', include('NutriPage.users.urls')),
    path('meals/', include('NutriPage.meals.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)