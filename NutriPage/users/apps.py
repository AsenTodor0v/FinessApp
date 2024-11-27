from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NutriPage.users'

    def ready(self):
        import NutriPage.users.signals