from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.
from django.views.generic import DetailView


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'users/profile.html'
    model = User
