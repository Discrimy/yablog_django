from django.urls import path, include

from yaurl import views

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),

    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('redirect/<shorted_id>/', views.shorted_url_redirect, name='redirect'),
]
