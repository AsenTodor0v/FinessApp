from django.contrib import admin

from NutriPage.users.models import Role, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')



@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')

