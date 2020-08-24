from django.urls import path

from . import bot_client, views

urlpatterns = [
    path('', views.index, name='index')
]
