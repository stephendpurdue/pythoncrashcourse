"""Defines URL patterns for learning_logs."""

from django.urls import include, path
from django.contrib import admin
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # Topic page
    path('', views.topics, name='topics')
]