from django.contrib.auth import get_user_model
from rest_framework import serializers

from NutriPage.users.models import Profile

AppUserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['user', 'profession', 'bio']

    def validate_user(self, value):
        if not value:
            raise serializers.ValidationError("A valid user must be provided.")
        return value


class AppUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False)

    class Meta:
        model = AppUserModel
        fields = '__all__'
