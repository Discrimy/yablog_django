from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin


class ProfileView(LoginRequiredMixin, SingleObjectMixin, ListView):
    template_name = 'users/profile.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(User.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object
        return context

    def get_queryset(self):
        return self.object.post_set.all()
