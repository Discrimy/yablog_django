from django.urls import path

from yaurl import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('redirect/<shorted_id>', views.shorted_url_redirect, name='redirect'),
]
