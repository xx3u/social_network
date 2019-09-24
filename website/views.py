from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, View
from django.contrib.auth.forms import UserCreationForm

from website.models import Image, CustomUser


class HomeView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'home.html'


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser


class RegisterView(View):  # pragma: no cover
    def get(self, request):
        return render(request, 'register.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})
