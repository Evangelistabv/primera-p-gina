from django.contrib import admin
from django.urls import path
from MiTiendaApp import views
urlpatterns = [
    path('', views.home,name='Home'),

    path('registro',views.VRegistro.as_view(), name="registro"),

    path('cerrar_sesion',views.cerrar_sesion, name="cerrar_sesion"),

    path('logear',views.logear, name="logear"),

]
