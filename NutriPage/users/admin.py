from django.contrib import admin

from NutriPage.users.models import CustomUser, Profile



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')