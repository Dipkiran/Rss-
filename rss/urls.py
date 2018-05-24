from django.contrib import admin
from django.urls import include, path

from . import views

app_name='rss'

urlpatterns = [
    path('', views.index, name='index'),
]
