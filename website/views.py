from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

from website.models import Profile


class HomeView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html', {'title': 'About'})


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Profile


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html', {'form': UserRegisterForm()})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # pragma: no cover
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
        return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')
