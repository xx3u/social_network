from django.views.generic import ListView

from .models import Profile


class HomeView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'home.html'
