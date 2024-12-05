from rest_framework import serializers

from NutriPage.users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

    def validate_user(self, value):
        if not value:
            raise serializers.ValidationError("A valid user must be provided.")
        return value

