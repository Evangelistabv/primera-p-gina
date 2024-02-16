import os
import sys
sys.path.append("/Users/cochiloco/Desktop/proyecto_django/MiTienda")
from django.contrib import admin
from django.urls import path
from BlogApp import views
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MiTienda.settings')
import django
django.setup()
urlpatterns = [
	path('', views.blog,name='blog'),
	path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),

]