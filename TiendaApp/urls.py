from django.contrib import admin
from django.urls import path
from TiendaApp import views
urlpatterns = [
    path('', views.tienda,name='tienda'),
    path("agregar/<int:producto_id>/", views.agregar, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]