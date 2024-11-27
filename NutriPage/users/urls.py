from django.urls import path

from NutriPage.users import views
from NutriPage.users.views import ProfileView, ProfileEditView, ProfileLoginView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-edit/', ProfileEditView.as_view(), name='edit-profile'),
    path('logout/', views.logout_view, name='logout-profile'),
    path('login/', ProfileLoginView.as_view(), name='login-profile'),
    path('profile-delete/', views.delete_author_page, name='delete-profile'),
    path('register/', views.register, name='register'),
]
