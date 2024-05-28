from django.contrib import admin
from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    # path('', views.law_list, name='law_list'),
    path('', views.LawsListView.as_view(), name='law_list'),
    path('<int:pk>/', views.law_detail, name='law_detail'),
    path('law_add/', views.law_add, name='law_add'),
    path('<int:pk>/edit/', views.law_add, name='edit'),
    path('<int:pk>/delete/', views.law_delete, name='law_delete'),
]
