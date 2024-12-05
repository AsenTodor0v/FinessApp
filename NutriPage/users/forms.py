from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re
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

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError('Password must contain at least one digit.')
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError('Password must contain at least one uppercase letter.')
        if not any(char in '!@#$%^&*()_+' for char in password1):
            raise forms.ValidationError('Password must contain at least one special character.')
        if len(password1) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password1