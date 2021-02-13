
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'analyst'

urlpatterns = [
    path('analystPage', views.analystPage.as_view(),name = 'analystPage'),
]