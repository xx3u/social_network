from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, View
from django.contrib.auth.forms import UserCreationForm

from django.views import View

from website.models import Image


class HomeView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'home.html'


def logout_view(request):
    logout(request)
    return redirect('logout')


# def login_view(request):
#     form = LoginForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username,
#                                 password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#     return HttpResponseRedirect('/')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html', { 'form': UserCreationForm() })

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, 'register.html', { 'form': form })
