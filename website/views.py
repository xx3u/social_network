from django.shortcuts import render
# from django.shortcuts import redirect, reverse
from django.views.generic import ListView, View
from django.contrib.auth.forms import UserCreationForm

from website.models import Image


class HomeView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'home.html'


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     return redirect(reverse('login'))

        return render(request, 'register.html', {'form': form})
