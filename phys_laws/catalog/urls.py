from django.contrib import admin
from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.law_list, name='law_list'),
]