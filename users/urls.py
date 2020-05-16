from django.urls import path, include

from users.views import ProfileView

urlpatterns = [
    path('registration/', include('django.contrib.auth.urls')),
    path('<int:pk>/profile', ProfileView.as_view(), name='profile'),
]
