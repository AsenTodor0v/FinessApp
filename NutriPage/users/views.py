from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView

from NutriPage.users.forms import DetailUserForm, EditUserForm, DeleteProfileForm, ProfileForm
from NutriPage.users.models import Profile

UserModel = get_user_model()

class ProfileView(LoginRequiredMixin,DetailView):
    template_name = 'logged/profile_page.html'
    model = Profile
    form_class = DetailUserForm

    def get_object(self, queryset=None):
        return Profile.objects.first()

class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'logged/edit_profile.html'
    success_url = reverse_lazy('profile')
    form_class = EditUserForm

    def get_object(self, queryset=None):
        return Profile.objects.first()

def logout_view(request):
    logout(request)
    return redirect('homepage')

class ProfileLoginView(UserPassesTestMixin, LoginView):
    template_name = 'logout/login_page.html'
    success_url = reverse_lazy('homepage')

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('homepage')

def register(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = ProfileForm()
    return render(request, 'logout/create-profile.html', {'form': form})


# not sure!!!

@login_required
def delete_author_page(request):
    author = request.user
    form = DeleteProfileForm(instance=author)

    if request.method == 'POST':
        author.delete()
        return redirect('homepage')

    context = {
        'author': author,
        'form': form,
    }

    return render(request, 'logged/delete_profile.html', context)