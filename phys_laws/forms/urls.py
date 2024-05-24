from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from . import views

app_name = 'forms'

urlpatterns = [
    path('', views.form0, name='form0'),
    path('<str:name>/', views.resp0, name='resp0'),
]
