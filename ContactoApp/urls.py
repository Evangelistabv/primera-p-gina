from django.contrib import admin
from django.urls import path
from ContactoApp import views
urlpatterns = [
	path('', views.contacto,name='contacto'),
]
