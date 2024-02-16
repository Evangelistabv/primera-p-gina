from django.contrib import admin
from django.urls import path
from ServiciosApp import views
urlpatterns = [
    path('', views.servicios,name='servicios'),
]