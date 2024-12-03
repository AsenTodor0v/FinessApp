from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from NutriPage.users.models import Profile, CustomUser

UserModel = get_user_model()

class DetailUserForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','email', 'bio', 'profile_picture']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'profile_picture','role']

class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = 'readonly'
            self.fields[field].disabled = 'disabled'


class ProfileForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']